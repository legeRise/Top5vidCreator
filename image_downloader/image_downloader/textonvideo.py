import cv2
import os
import textwrap

#________________________________________________________________
def add_text_with_shadow(frame, text, position, font, font_scale, thickness, shadow_color, shadow_offset):
    # Add shadow text
    shadow_position = (position[0] + shadow_offset[0], position[1] + shadow_offset[1])
    cv2.putText(frame, text, shadow_position, font, font_scale, shadow_color, thickness, cv2.LINE_AA)



#_________________________________________________________________
def arrange():   # arranges  items in reverse order for 5 4 3 2 1  type of video
    with open('display.txt', 'r') as f:
        actual = f.read().splitlines()

    print('Before: ', actual)
    ask = input('Want to Reverse? (y or n): ')

    first = actual[0]
    if ask == 'y':
        actual.pop(0)
        actual.reverse()
        actual.insert(0, first)

    print('After: ', actual)
    return actual
#_____________________________________________________

def colorname(color_name):
    import webcolors
    try:
        rgb = webcolors.name_to_rgb(color_name)
        # Swap red and blue color values
        rgb = (rgb[2], rgb[1], rgb[0])
        return rgb
    except ValueError:
        return (0, 0, 0)  # Default to black if color name is not found
#______________________________________________________________________
def add_timestamp(frame,text, **text_properties):

    # Access individual properties of text_properties dictionary
    font = text_properties.get("font", cv2.FONT_HERSHEY_SIMPLEX)
    font_scale = text_properties.get("font_scale", 1.5)
    color = text_properties.get("color", (0,255,255))
    thickness = text_properties.get("thickness", 2)
    offset = text_properties.get("offset", (0, 0))
    line_type = text_properties.get("line_type", cv2.LINE_AA)

    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

#SUMMARY: this part just makes a list(wrapped_lines) of strings : # 1. len of list is total number of wrapped lines   2. And Each string represents text on each line
    wrapped_lines = []
    words = text.split(' ')
    current_line = ''
    for word in words:
        (line_width, _), _ = cv2.getTextSize(current_line + ' ' + word, font, font_scale, thickness)
        if line_width <= frame_width:
            current_line += ' ' + word
        else:
            wrapped_lines.append(current_line.strip())
            current_line = word
    if current_line:
        wrapped_lines.append(current_line.strip())   #to this point list of splitted text is returned means if text was wrapped into 3 lines then this list will have 3 elements

# SUMMMARY: these lines are just finding  text,width,text_height and line spacing of text on screen
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness) #so basically getTextSize() function takes  "Text(content), "fontScale(size of text)","font( type of font)  and thickness  ) and based on these inputs returns text height and width ...means how would it look like when placed on screen and also it returns another thing baseline offset that we don't need so we ignore it by storing it in "_" that is a convention
    line_spacing = int(text_height * 1.5)  # Adjust the line spacing as needed   2 would inceasing line spacing 1 would decrese it is obvious


# SUMMARY: Calculates where exactly text is placed vertically( y-axis)  by performing following calculations  # not actually drawing
    y = int((frame_height + text_height) / 2)  # first it adds frame_height(the full screen) and text_height and divides it by 2 to find midpoint
    y= y+ offset[1]  # then for further up and down of text positioning it adds offset[1] which is height if it is a positive number text goes down, else up
    y = y - (len(wrapped_lines) * line_spacing) # as the number of lines maybe more, we multiply [spacing height * total lines] which will help us take text upward and more place for down lines
    # so  basically y - (len(wrapped_lines) * line_height) this line kind acts as a negative offset value


# SUMMARY: this part is where the text is actually is drawn on screen
    for textLine in wrapped_lines: # wrapped_lines is just a list of strings mentioned above
        (textline_width, _), _ = cv2.getTextSize(textLine, font, font_scale, thickness)  # we know get size returns width,height and baseline offset and in this case we just need width so using "_" convention to discard others
        x = int((frame_width - textline_width) / 2) + offset[0] # this line is calculating where exactly the text is placed horizontally (x-axis)

        """Draws shadow text   """
        add_text_with_shadow(frame, textLine, (x, y), font, font_scale,thickness,shadow_color,shadow_offset)
        """Draws Main text   """
        cv2.putText(frame, textLine, (x, y), font, font_scale, color, thickness, line_type) # and finally this function draws text on video by taking follwing arguments: 1. frame(screen/full_image)  2. textline(put this func in loop if more than one lines)3. (x,y) coordinates that we calculated above.  and the other text properties like font, thickness etc and finally draws the text
        y += line_spacing  # and after text is placed on first line ...next it decides the position of next line by adding "line_spacing to y
        # in other words we can say that  in next line coordinates in putText()-> (x,y) == ( x, y+line_spacing)

# end______of ___________func


def put_text_on_video(video_path, output_path, text_properties):
    # Open the video file
    video = cv2.VideoCapture(video_path)  # videoCapture() converts it into a video object so all func like pause resume play can be applied to this video

    # Get video properties using get() func:  get() has some pre-defined attributes that when passed as arguments, it returns their value
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # * is used in unpacking iterables so, *'mp4v' is easy way to pass. the other way is separately passing 4 characters like 'm','p','4','v'
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height)) # it makes an empty video continer with the specified name and path for the video
    # ...and the following code keeps modifying each frame and storing in it


    actual =arrange()   # arranges  items in reverse order for 5 4 3 2 1  type of video

    timestamps = [
        {"text": f"5. {actual[1]}", "start_time": 2.0, "end_time": 4.0},
        {"text": f"4. {actual[2]}", "start_time": 4.0, "end_time": 6.0},
        {"text": f"3. {actual[3]}", "start_time": 6.0, "end_time": 8.0},
        {"text": f"2. {actual[4]}", "start_time": 8.0, "end_time": 10.0},
        {"text": f"1. {actual[5]}", "start_time": 10.0, "end_time": 12.0},
    ]
    # Read and process each frame of the video
    frame_count = 0
    current_timestamp = None

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        #step1:  These lines just find out the starting frame and ending frame for timestamp
        if current_timestamp is None or frame_count >= current_timestamp["end_frame"]:  # checks if current_timestamp is none means initially started ..or if frame count is going above the end frame count (means displaying-duration of previous timestamp has ended)...because in both cases we need a new time frame(start and end)
            if timestamps:   # means  if timestamps list isn't empty
                current_timestamp = timestamps.pop(0)  # first time it retrieves first element then removes it from list..next time a new first element is retrieved and so on
                current_timestamp["start_frame"] = int(current_timestamp["start_time"] * fps) # we have fps: 24 and start_time: but to put time_stamp on current location we need start_frame so for that : fps* start_time= start_frame
                current_timestamp["end_frame"] = int(current_timestamp["end_time"] * fps)  # similarly for end_frame : end_time* fps


        if current_timestamp and frame_count >= current_timestamp["start_frame"]:
            add_timestamp(frame, current_timestamp["text"], **text_properties)  # passing properties using **kwargs

        output_video.write(frame)  # Write the frame with added text to the output video

        # Display the resulting frame (optional)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame_count += 1

    video.release()  # leaves the input video
    output_video.release() # releases/or finalizes the output video
    cv2.destroyAllWindows()  # destroy all windows created by opencv
#end_________of_____________func

if __name__ == '__main__':

    # step 1: Specify the input video path,output video path and Define the text properties

    # input video path
    input_video_path = "final_output.mp4"

    # output videopath
    with open('display.txt',) as f:
        titleName =f.readline()  #  f.readline reads the first line in display.txt file which in this case is 'title name' user wants
        wholepath = os.path.join(os.getcwd(),'done')
    output_video_path = os.path.join(wholepath,f'{titleName.strip()}.mp4')

    # text properties
    text_properties = {
        "font": cv2.FONT_HERSHEY_SIMPLEX,    #cv2.FONT_HERSHEY_TRIPLEX
        "font_scale": 1.5,
        "color": colorname("yellow"),  # Red color (BGR)
        "thickness": 5,
        "offset": (0, 50),  # Move text 10 pixels to the right and 10 pixels up
        "line_type": cv2.LINE_AA
    }
    shadow_color = colorname("black")
    shadow_offset = (6,6)

    # step 2: Call the function which takes input video path, output video path and text properties as input
    put_text_on_video(input_video_path, output_video_path, text_properties)

