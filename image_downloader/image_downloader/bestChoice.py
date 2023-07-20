import os
import random
current =os.getcwd()
folder = 'images'

allimgfolders =os.listdir(folder)


with open('names.txt', 'r') as f:
    names = f.read().splitlines()

print('Before: ',names)
ask =  input('Want to Reverse? (y or n): ')
first = names[0]
if ask=='y':
    names.pop(0)
    names.reverse()
    names.insert(0, first)


print('After: ',names)



with open('imgPaths.txt','w') as writer:

    for name in names:
        for img in allimgfolders:
            if name==img:
                new_path =os.path.join(current,f'images\{img}')
                all_new =os.listdir(new_path)
                #print(all_new)  # inside each image folder
                random_path = os.path.join(new_path,random.choice(all_new)) # randomly selects image
                writer.write(f'{random_path}\n')

