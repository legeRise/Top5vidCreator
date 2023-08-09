import os
import shutil
import time
from pygoogle_image import image as pi
import random
import cv2
from PIL import Image
from moviepy.editor import ImageClip, concatenate_videoclips


#_________________________________________________________________________________________________________
def imgdownloader(top5,display):
    current = os.getcwd()

    top5 = top5.split(",")
    top5 = [name.replace(" ", "") for name in top5]  # remove spaces
    print(top5)

    display = display.split(',')
    print(display)


    with open('display.txt', 'w') as f:   # saves title and names to be displayed
        for name in display:
            print(name)
            f.write(f'{name}\n')

    with open('names.txt', 'w') as f:    # saves titlepic keywords and search keywords
        for name in top5:
            print(name)
            f.write(f'{name}\n')

    time.sleep(1)
    if os.path.exists('images'):
        shutil.rmtree('images')
    time.sleep(1)
    os.mkdir('images')

    for image in top5:
        print(f'downloading {image} images...')
        pi.download(image, limit=4)
        changed = os.getcwd() + f'\images\{image}'
        print(changed)
        os.chdir(changed)
        files = os.listdir()
        os.remove(files[0])
        os.remove(files[1])
        print('Download Complete...')
        os.chdir(current)

#_______________________________________________________________________________________________________________________


def bestChoice(reverse):
    current = os.getcwd()
    folder = 'images'
    allimgfolders = os.listdir(folder)

    with open('names.txt', 'r') as f:
        names = f.read().splitlines()

    print('Before: ', names)
    ask = reverse
    first = names[0]
    if ask:
        names.pop(0)
        names.reverse()
        names.insert(0, first)

    print('After: ', names)

    with open('imgPaths.txt', 'w') as writer:
        for name in names:
            for img in allimgfolders:
                if name == img:
                    new_path = os.path.join(current, f'images\{img}')
                    all_new = os.listdir(new_path)
                    random_path = os.path.join(new_path, random.choice(all_new))
                    writer.write(f'{random_path}\n')

#_______________________________________________________________________________________________________________________

def  makeVideo():
    current = os.getcwd()

    target_height = 900
    target_width = int(target_height * (9/16))
    target = (target_width, target_height)


    def resize_images(photo_paths, target_size=target, target_format='jpeg'):
        resized_image_paths = []
        for path in photo_paths:
            image = Image.open(path)

            # Convert image format if necessary
            if image.format.lower() != target_format:
                new_path = os.path.splitext(path)[0] + '.' + target_format
                image = image.convert('RGB')  # Convert RGBA to RGB
                image.save(new_path)
                path = new_path

            resized_image = image.resize(target_size)
            resized_image_path = "resized_" + os.path.basename(path)
            resized_image_path = os.path.join('resized', resized_image_path)

            # Ensure image is in RGB mode
            if resized_image.mode != 'RGB':
                resized_image = resized_image.convert('RGB')

            resized_image.save(resized_image_path)
            resized_image_paths.append(resized_image_path)
        return resized_image_paths


    def create_video_from_photos(duration_per_photo, output_file, photo_file='imgPaths.txt'):
        with open(photo_file, 'r') as f:
            photo_paths = f.read().splitlines()

        resized_paths = resize_images(photo_paths)

        # Create ImageClip objects for each image with the specified durations
        image_clips = [ImageClip(path, duration=duration) for path, duration in zip(resized_paths, duration_per_photo)]

        # Concatenate the image clips to form the final video
        video_clip = concatenate_videoclips(image_clips, method="compose")

        # Write the video to the output file
        video_clip.write_videofile(output_file, codec='libx264', fps=24)


    time.sleep(1)
    if os.path.exists('resized'):
        shutil.rmtree('resized')  # removes a whole folder and everything in it. Better than os.remove()

    time.sleep(1)
    os.mkdir('resized')
    create_video_from_photos([2, 2, 2, 2, 2,2], 'output.mp4')


#_______________________________________________________________________________________________________________________


def titleBar(bg_color="yellow",text_color="black",fontSize=2,thickness=3):
    #Extract title text
    with open('display.txt','r') as f:
        title = f.readline().strip()

    def colorname(color_name):
        import webcolors
        try:
            rgb = webcolors.name_to_rgb(color_name)
            # Swap red and blue color values
            rgb = (rgb[2], rgb[1], rgb[0])
            return rgb
        except ValueError:
            return (0, 0, 0)  # Default to black if color name is not found


    # Load the video
    video_path = "output.mp4"
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the output video codec and create VideoWriter object
    output_path = "final_output.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Define title bar properties
    title_bar_height = 80
    title_text = title
    title_font = cv2.FONT_HERSHEY_SIMPLEX
    title_font_scale = fontSize
    title_text_color = colorname(text_color)
    title_bg_color = colorname(bg_color)
    title_thickness = thickness
    title_offset_top = 300
    title_offset_sides = 20
    title_text_max_width = width - 2 * title_offset_sides

    # Set the duration for which the title bar will be displayed (in seconds)
    title_duration = 1.4

    # Variables to keep track of elapsed time and title bar visibility
    start_time = cv2.getTickCount() / cv2.getTickFrequency()
    current_time = 0
    display_title_bar = True

    # Loop through each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Add title bar if it should be displayed
        if display_title_bar:
            frame[title_offset_top:(title_offset_top + title_bar_height),
            title_offset_sides:(width - title_offset_sides)] = title_bg_color

            # Fit title text within the title bar
            text_width, text_height = cv2.getTextSize(title_text, title_font, title_font_scale, title_thickness)[0]
            while text_width > title_text_max_width:
                title_font_scale -= 0.1
                text_width, text_height = cv2.getTextSize(title_text, title_font, title_font_scale, title_thickness)[0]

            # Add title text
            text_x = int((width - text_width) / 2)
            text_y = title_offset_top + int(title_bar_height / 2) + int(text_height / 2)
            cv2.putText(frame, title_text, (text_x, text_y), title_font, title_font_scale, title_text_color,
                        title_thickness, cv2.LINE_AA)

        # Calculate elapsed time
        current_time = (cv2.getTickCount() / cv2.getTickFrequency()) - start_time

        # Check if the duration has been exceeded
        if current_time >= title_duration:
            display_title_bar = False

        # Write the modified frame to the output video
        out.write(frame)

        # Display the resulting frame (optional)
        # cv2.imshow("Frame", frame)

        # Press 'q' to stop the video processing
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


#_______________________________________________________________________________________________________________________

def textOnVideo(title,reverse):

    def colorname(color_name):
        import webcolors
        try:
            rgb = webcolors.name_to_rgb(color_name)
            # Swap red and blue color values
            rgb = (rgb[2], rgb[1], rgb[0])
            return rgb
        except ValueError:
            return (0, 0, 0)  # Default to black if color name is not found

    def add_text_with_shadow(frame, text, position, font, font_scale, thickness, shadow_color, shadow_offset):
        # Add shadow text
        shadow_position = (position[0] + shadow_offset[0], position[1] + shadow_offset[1])
        cv2.putText(frame, text, shadow_position, font, font_scale, shadow_color, thickness, cv2.LINE_AA)


    def arrange():   # arranges  items in reverse order for 5 4 3 2 1  type of video
        with open('display.txt', 'r') as f:
            actual = f.read().splitlines()

        print('Before: ', actual)
        ask = reverse

        first = actual[0]
        if ask:
            actual.pop(0)
            actual.reverse()
            actual.insert(0, first)

        actual = [i for i in actual if i!=""]
        print('After: ', actual)
        return actual




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
            wrapped_lines.append(current_line.strip())
        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness) #so basically getTextSize() function takes  "Text(content), "fontScale(size of text)","font( type of font)  and thickness  ) and based on these inputs returns text height and width ...means how would it look like when placed on screen and also it returns another thing baseline offset that we don't need so we ignore it by storing it in "_" that is a convention
        line_spacing = int(text_height * 1.5)  # Adjust the line spacing as needed   2 would inceasing line spacing 1 would decrese it is obvious



        y = int((frame_height + text_height) / 2)
        y= y+ offset[1]
        y = y - (len(wrapped_lines) * line_spacing)

        for textLine in wrapped_lines:
            (textline_width, _), _ = cv2.getTextSize(textLine, font, font_scale, thickness)
            x = int((frame_width - textline_width) / 2) + offset[0]

            """Draws shadow text   """
            add_text_with_shadow(frame, textLine, (x, y), font, font_scale,thickness,shadow_color,shadow_offset)
            """Draws Main text   """
            cv2.putText(frame, textLine, (x, y), font, font_scale, color, thickness, line_type) # and finally this function draws text on video by taking follwing arguments: 1. frame(screen/full_image)  2. textline(put this func in loop if more than one lines)3. (x,y) coordinates that we calculated above.  and the other text properties like font, thickness etc and finally draws the text
            y += line_spacing


    def put_text_on_video(video_path, output_path, text_properties):

        # Open the video file
        video = cv2.VideoCapture(video_path)

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


            if current_timestamp is None or frame_count >= current_timestamp["end_frame"]:
                if timestamps:
                    current_timestamp = timestamps.pop(0)
                    current_timestamp["start_frame"] = int(current_timestamp["start_time"] * fps)
                    current_timestamp["end_frame"] = int(current_timestamp["end_time"] * fps)


            if current_timestamp and frame_count >= current_timestamp["start_frame"]:
                add_timestamp(frame, current_timestamp["text"], **text_properties)

            output_video.write(frame)  # Write the frame with added text to the output video

            # Display the resulting frame (optional)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            frame_count += 1

        video.release()  # leaves the input video
        output_video.release() # releases/or finalizes the output video
        cv2.destroyAllWindows()  # destroy all windows created by opencv


    # step 1: Specify the input video path,output video path and Define the text properties
    if title:
        titleBar()
        input_video_path = "final_output.mp4"
    else:
        input_video_path = "output.mp4"

    # output videopath
    with open('display.txt', ) as f:
        titleName = f.readline()  # f.readline reads the first line in display.txt file which in this case is 'title name' user wants
        wholepath = os.path.join(os.getcwd(), 'done')
    output_video_path = os.path.join(wholepath, f'{titleName.strip()}.mp4')
    print(output_video_path,"sdfsadfsafas")
    if not os.path.exists('done'):
        os.makedirs("done")


    # text properties
    text_properties = {
        "font": cv2.FONT_HERSHEY_SIMPLEX,  # cv2.FONT_HERSHEY_TRIPLEX
        "font_scale": 1.7,
        "color": colorname("yellow"),  # Red color (BGR)
        "thickness": 6,
        "offset": (0, 60),  # Move text 10 pixels to the right and 10 pixels up
        "line_type": cv2.LINE_AA
    }
    shadow_color = colorname("black")
    shadow_offset = (7, 7)

    # step 2: Call the function which takes input video path, output video path and text properties as input
    put_text_on_video(input_video_path, output_video_path, text_properties)














