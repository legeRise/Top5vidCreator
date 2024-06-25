# Auto Video Maker

Auto Video Maker is a Python tkinter application that can generate YouTube videos.

## Video Sample
Here is a video sample created by Auto Video Maker:

[video sample](https://github.com/legerise/ytshortmaker/raw/master/done/Top%205%20Programming%20Languages.mp4)


## Usage

### Clone Repository

Clone this repository using:

```bash
git clone https://github.com/legeRise/ytshortmaker.git
```

```bash
cd ytshortmaker
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

![Auto Video Maker Interface](https://github.com/legerise/ytshortmaker/raw/master/assets/interface.png)

### How to Use

1. **Step 1 - Pic Keywords**: Enter comma-separated keywords (e.g., programminglanguageicons, javascript,python,java,c++,c).
   
2. **Display Keywords**: Enter display names for images (e.g., "Top 5 Programming Languages", "JavaScript"). Each "display keyword" corresponds to a "pic keyword". For example:

   - **Pic Keyword**: `programminglanguageicons`
     - **Display Keyword**: "Top 5 Programming Languages"

   This means that images associated with the `programminglanguageicons` keyword will have the overlay text "Top 5 Programming Languages" displayed on them.

3. Click the **Download Images** button to download images based on the provided keywords.

4. Click the **Make Video** button to assemble the downloaded images into a video.

5. Optionally, check the **TitleBar** and click **Text on Video** to add a title bar and text overlays.

6. By the end of the process, the video will be saved in the `done/` folder with the title based on the first display keyword (e.g., Top 5 Programming Languages).

Note: Each keyword searches for images related to that keyword.

### Note

I know this could have been a one-click video maker button. This was just a beginner curiosity project, and I'm glad it works somehow.
``` 

This markdown code block includes all the headings, subheadings, instructions, and notes as per your instructions.
