
from pygoogle_image import image as pi

while True:
  a = input("Enter: ")
  pi.download(a, limit=6)
  n= input("Enter choice: ")
  if n=='q':
    exit()
