import os 
import subprocess
import tkinter as tk
from PIL import Image,ImageTk
from functionalityClass import videoFunctions

func = videoFunctions()
class appGui:
    def __init__(self,root):
        self.root = root
        self.root.title("Auto Video Maker")
        self.root.geometry(f"{400}x{520}")   # <width>x<height>+<x_offset>+<y_offset>
        self.root.minsize(400,520)
        self.root.maxsize(400,520)

        # background image
        self.bgImg = ImageTk.PhotoImage(file=r"assets\1.jpg")
        label_image1 =  tk.Label(self.root,image=self.bgImg)
        label_image1.place(x=0,y=0,width=400,height=520)

        # frame for register
        frame = tk.Frame(self.root,bg="white")
        frame.place(x=30,y=30,width=340,height=480)
#_______________________________________________Email_____________________________________________________________________

    # Title pic box
    def mylabel(self,text,x,y,size=13):
        label = tk.Label(text=text,font=("times new roman",size,"bold"),fg="black",bg="white")
        label.place(x=x, y=y)

#_______________________________________________________
    def mybutton(self,text,x,y,command=None):
        name5 = tk.Button(command=command, text=text, font=("times new roman", 15, "bold"), fg="white", bg="green",activeforeground="green",activebackground="yellow")
        name5.place(x=x, y=y)

#_______________________________________________________
    def check(self,text,x,y,variable,command=None):
        ask = tk.Checkbutton(text=text, font=("Arial", 12), bg="white", fg="blue", activeforeground="green", selectcolor="yellow",variable=variable, command=command)
        ask.place(x=x,y=y)
#_______________________________________________________
# create an image button

    def iconButton(self,image,command,x,y):
        icon = Image.open(f"{image}").resize((34, 40), Image.ANTIALIAS)
        icon_class_tk = ImageTk.PhotoImage(icon)
        # Create and display the folder icon button
        img_button = tk.Button(image=icon_class_tk, command=command, bg='white', borderwidth=0)
        img_button.image = icon_class_tk  # Keep a reference to the image to prevent it from being garbage collected
        img_button.place(x=x, y=y)

#_______________________________________________________

    def toggle_button(self,x,y):
        ask  = self.ask.get()
        if ask:
            self.myself.place(x=x, y=y, width=150)
            self.myselfbutton.place(x=x+25, y=y+40)
        else:
            self.myself.place_forget()
            self.myselfbutton.place_forget()

    #________________________________________________________
    def downloadyourself(self):
        query = self.myself.get()
        func.download_yourself(query)
#_________________________________________________________
    def openfolders(self,folder):
        current = os.getcwd()
        if folder=='images':
            images = os.path.join(current, 'images')
            if os.path.exists(images):
                if os.name == 'nt':  # Windows
                    subprocess.Popen(['explorer', images])
        if folder=='done':
            done = os.path.join(current, 'done')
            if os.path.exists(done):
                if os.name == 'nt':  # Windows
                    subprocess.Popen(['explorer', done])


#__________________________________________________________
    def clicked(self,ex,ey,bx=280,by=465):
        self.askemail.place(x=ex,y=ey)
        self.sendemail.place(x=bx,y=by)

    def email(self):
        receiverEmail=self.askemail.get()

        with open('createdVids.txt') as f:
            a = f.readlines()
        paths = [i.strip('\n') for i in a]

        func.email(receiverEmail,video_paths=paths)


#__________________________________________________________
    def XClear(self,x,y,hide=False,*boxes):
        clear = tk.Button(text="X", font=("times new roman", 15, "bold"), fg="green", bg="white", activeforeground="green",activebackground="white", borderwidth=0, command=lambda: app.clear(boxes))
        if not hide:
            clear.place(x=x, y=y, height=27)
        else:
            clear.place_forget()

                   #___________Clear Functionality__________________
    def clear(self,boxIndex):
        for box in boxIndex:
            box.delete(0,tk.END)
#__________________________________________________________
    def imgdownloader(self,top5,display):
        top =top5.get()
        disp = display.get()
        func.imgdownloader(top,disp)

#___________________________________________________________

    def makeVideo(self):
        reverse = self.reverse.get()
        if reverse:
            func.bestChoice(reverse)
        else:
            func.bestChoice(False)
        func.makeVideo()
#_________________________________________________

    def textOnVideo(self):

        titleBar = self.titlebar.get()
        reverse = self.reverse.get()
        func.textOnVideo(titleBar,reverse)
#_______________________________________________________________________________________________________________________
