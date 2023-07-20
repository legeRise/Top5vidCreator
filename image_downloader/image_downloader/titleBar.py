import cv2

#title
with open('display.txt','r') as f:
    title = f.readline().strip()

#__________________________funcions____________________________________________
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
title_font_scale = 2
title_text_color = colorname("Black")  # White color
title_bg_color = colorname("yellow")  # Green color
title_thickness = 2
title_offset_top = 380
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
    cv2.imshow("Frame", frame)

    # Press 'q' to stop the video processing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()
