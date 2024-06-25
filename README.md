# Auto Video Maker

Auto Video Maker is a desktop application that allows users to create videos by downloading images based on specified keywords, and then assembling them into a video. Additional features include adding text overlays and title bars to the video, and the ability to send the final video via email.

## Features

- **Image Download**: Download images from the internet based on keywords.
- **Video Creation**: Assemble downloaded images into a video.
- **Text Overlay**: Add custom text overlays to the video.
- **Title Bar**: Add a title bar to the video.
- **Email Sharing**: Send the final video via email.
- **Manual Download**: Option to manually download images and add them to the video.

## Prerequisites

- Python 3.x
- Required Python packages:
  - tkinter
  - pillow
  - moviepy
  - opencv-python
  - smtplib
  - pygoogle_image

You can install the required packages using:

```bash
pip install pillow moviepy opencv-python pygoogle_image
```

## Usage

```markdown
### Run the Application:

```bash
python autovideomaker.py
```

### Interface Overview:

- **Pic Keywords**: Enter keywords for image searches, separated by commas.
- **Display Names**: Enter display names for images, separated by commas.
- **Image Downloader**: Download images based on the provided keywords.
- **Make Video**: Create a video from the downloaded images.
- **Text on Video**: Add text overlays to the video.
- **Send Email**: Send the final video to a specified email address.

### Steps:

1. **Enter the image keywords and display names.**
2. **Click the "Image Downloader" button to download images.**
3. **Click the "Make Video" button to assemble the images into a video.**
4. **Optional**: Check the "TitleBar" and click "Text on Video" to add a title bar and text overlays.
5. **Send Email**: Use the email button to send the final video.
```

## Directory Structure

```markdown
- `autovideomaker.py`: Main script to launch the GUI.
- `functionalityClass.py`: Contains functions for video creation and other features.
- `guiClass.py`: Handles the GUI components and interactions.
- `assets/`: Folder containing image assets like icons.
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
