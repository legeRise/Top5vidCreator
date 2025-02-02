# Auto Video Maker

Auto Video Maker is a Python tkinter application that can generate YouTube videos.
 
## Video Sample
Here is a video sample created by Auto Video Maker:

[video sample](https://github.com/legerise/ytshortmaker-tkinter-app/raw/master/done/Top%205%20Programming%20Languages.mp4)

### An another Note(2 Feb, 2025)
If you are really interested in generating such videos, consider improved version of this project [youtube-shorts-generator](https://github.com/legeRise/youtube-shorts-generator.git) this was more of a fun project and expects a lot from you

## Usage 

### Clone Repository

Clone this repository using:

```bash
git clone https://github.com/legeRise/ytshortmaker-tkinter-app.git
```

```bash
cd ytshortmaker-tkinter-app
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

```bash
venv\scripts\activate
```

### Install Dependencies

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Launch Application

To launch the GUI application, run:

```bash
python autovideomaker.py
```

### Application Interface

![Auto Video Maker Interface](https://github.com/legerise/ytshortmaker-tkinter-app/raw/master/assets/interface.png)

### How to Use

1. **Step 1 - Pic Keywords**: Enter comma-separated keywords (e.g., programminglanguageicons, javascript,python,java,c++,c). 

   **Note: Each keyword searches for images related to that keyword.**
   


2. **Display Keywords**: Enter display names for images (e.g., Top 5 Programming Languages,JavaScript,Python,Java,C++,C). Each "display keyword" is the overlay text for the corresponding "pic keyword". So in the above example:

   - **Pic Keyword**: `programminglanguageicons`
     - **Display Keyword**: "Top 5 Programming Languages"

   This setup means that image downloaded against the  `programminglanguageicons` keyword will display the overlay text "Top 5 Programming Languages".

   so doing this
   
   ![Auto Video Maker Interface](https://github.com/legerise/ytshortmaker-tkinter-app/raw/master/assets/instruction.png)

   will result in this,

   ![Auto Video Maker Interface](https://github.com/legerise/ytshortmaker-tkinter-app/raw/master/assets/result.png)
   
4. Click the **Image Downloader** (which could have been named "download images", My Bad!) button to download images based on the provided keywords.

5. Click the **Make Video** button once the downloading part completes.

6. Finally, click **Text on Video** (check the **TitleBar** if your keywords had the titlebar)  to add a title bar and text overlays.

7. By the end of the process, the video will be saved in the `done/` folder with the title based on the first display keyword (e.g., Top 5 Programming Languages). 

### Note

I know this could have been a one-click video maker instead of having to click through 3-4 buttons. There was definitely room for improvement. But, this started as a beginner project out of curiosity, besides, I'm surprised it still works! So, Have Fun 🤷‍♂️


### Another Note 

As of 25/06/2024 it was working (Python 3.11)



