from moviepy.editor import ImageSequenceClip
import os
from PIL import Image
import shutil
import time
from moviepy.editor import ImageClip, concatenate_videoclips
from moviepy.video.fx.crop import crop



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
        resized_image_path = os.path.join('resized',resized_image_path)


        resized_image.save(resized_image_path)
        resized_image_paths.append(resized_image_path)
    return resized_image_paths



def create_video_from_photos(duration_per_photo, output_file, photo_file='imgPaths.txt'):
    with open(photo_file, 'r') as f:
        photo_paths = f.read().splitlines()

    resized_paths = resize_images(photo_paths)

    clip = ImageSequenceClip(resized_paths, durations=duration_per_photo)
    clip.write_videofile(output_file, codec='libx264', fps=24)



time.sleep(1)
if os.path.exists('resized'):
    shutil.rmtree('resized')  # removes a whole folder and everything in it. Better then os.remove()

time.sleep(1)
os.mkdir('resized')
create_video_from_photos([2, 2, 2, 2, 2, 2], 'output.mp4')
