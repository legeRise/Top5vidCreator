import os
import shutil
import time

current= os.getcwd()

# Accept six names as input
display = input("Enter six names separated by commas: ").split(',')


with open('names.txt','w') as f:
    for i in display:
        f.write(f'{i}\n')

with open('display.txt','w') as f:
    for i in display:
        f.write(f'{i}\n')



# Clear the 'image' folder
image_folder = os.path.join(current,'images')  # Modify the path if needed
if os.path.exists(image_folder):
    time.sleep(1)
    shutil.rmtree(image_folder)
    #print(f"Removed folder: {image_folder}")

# Create the main 'image' folder
os.makedirs(image_folder)
#print(f"Created folder: {image_folder}")

# Create sub-folders inside the 'image' folder using names
for name in display:
    folder_path = os.path.join(image_folder, name)
    os.makedirs(folder_path)
    print(f"Created folder: {folder_path}")




path =os.path.join(current,'BardImages')
old_names =os.listdir('BardImages')

# renaming images to corresponding folders

for new_name,old_name in zip(display,old_names):
    os.chdir(path)
    os.rename(old_name,f"{new_name}.jpg")



# moving images
os.chdir(current)
for name in display:
    old = os.path.join(path,f'{name}.jpg')
    new =os.path.join(image_folder,name)
    shutil.move(old,new)



#5 Must-Watch Post-Apocalyptic Series,The Walking Dead,The Last of Us,Station Eleven,Sweet Tooth,The 100
#Top 5 Most Dangerous Horror Movies,The Exorcist,The Conjuring,The Shining,Hereditary,The Ring