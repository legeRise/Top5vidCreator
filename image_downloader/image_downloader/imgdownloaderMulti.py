from pygoogle_image import image as pi
import os
import shutil
import time


current = os.getcwd()


top5 = input('1. AddTitlePic 2.Enter Top 5(separated by commas): ').split(',')
display = input('1. Display Title 2.Display Names: ').split(',')


with open('display.txt', 'w') as f:
    for name in display:
        f.write(f'{name}\n')

time.sleep(1)
if os.path.exists('images'):
    shutil.rmtree('images')
time.sleep(1)
os.mkdir('images')

with open('names.txt', 'w') as f:
    for image in top5:
        image_name = image.replace(" ", "")  # Remove spaces from the image name
        f.write(f'{image_name}\n')
        print(f'downloading {image} images...')
        pi.download(image, limit=4)
        changed = os.getcwd() + f'\images\{image_name}'
        print(changed)
        os.chdir(changed)
        files = os.listdir()
        os.remove(files[0])
        os.remove(files[1])
        print('Download Complete...')
        os.chdir(current)


#BestStreetFoods,Tacos_streetfood, Poutine_streetFood, Gelato_streetFood, Gyro_streetFood, Samosa_streetfood
#Top 5 Delicious Street Foods,Tacos, Poutine, Gelato, Gyro, Samosa

#CalloFDutyMobile,iFerg(LukeFergie),Godzly(AustinLiddie),Bobby_PlaysCod(RobertJohnson),ParkerTheSlayer(ParkerFerrell),LittleB(BradyMarshall)