import mysql.connector as c
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import OptionMenu
from tkinter import messagebox
import os
import shutil
import time
from pygoogle_image import image as pi
from helperFunctions import imgdownloader,bestChoice,makeVideo,titleBar,textOnVideo

class AutoVideoMaker:
    def __init__(self,root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root = root
        self.root.title("Auto Video Maker")
        self.root.geometry(f"{400}x{520}")   # <width>x<height>+<x_offset>+<y_offset>
        self.root.minsize(400,520)
        self.root.maxsize(400,520)


        # background image
        self.bgImg = ImageTk.PhotoImage(file=r"1.jpg")
        label_image1 =  tk.Label(self.root,image=self.bgImg)
        label_image1.place(x=0,y=0,width=400,height=520)


        # frame for register
        frame = tk.Frame(self.root,bg="white")
        frame.place(x=30,y=30,width=340,height=450)


    # step 1:    img downloader button
        # Title pic box
        name = tk.Label(frame,text="Pic keywords",font=("times new roman",13,"bold"),fg="black",bg="white")
        name.place(x=20, y=30)
        #input box
        self.top5 = ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.top5.place(x=130,y=30,width=150)


        # display name box
        name = tk.Label(frame,text="Display Names",font=("times new roman",13,"bold"),fg="black",bg="white")
        name.place(x=10, y=70)
        #input box
        self.display = ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.display.place(x=130,y=70,width=150)

        # ImgdownloaderMulti
        name1 = tk.Button(frame,command=self.imgdownloader, text="Image Dowloader", font=("times new roman", 15, "bold"), fg="white", bg="green",activeforeground="green",activebackground="yellow")
        name1.place(x=100, y=120)

        # clear box
        clear = tk.Button(frame, text="X", font=("times new roman", 13, "bold"),fg="green", bg="white", activeforeground="white", activebackground="green",borderwidth=0,command=self.clear)
        clear.place(x=300, y=30,height=27)


    #_______________________________________________________________________________________________________________________

        # Checkbox 1
        self.reverse = tk.BooleanVar()
        checkbox1 = tk.Checkbutton(frame, text="Reverse", font=("Arial", 12), bg="white", fg="blue", activeforeground="green", selectcolor="yellow",variable=self.reverse)
        checkbox1.place(x=115, y=170)

        name2 = tk.Button(frame,command=self.bestChoice, text="Best Choice", font=("times new roman", 15, "bold"), fg="white", bg="green",activeforeground="green",activebackground="yellow")
        name2.place(x=120, y=200)

    #____________________________________________________________________________________________________________________________________

        # makevideo
        name3 = tk.Button(frame,command=self.makeVideo, text="Make Video", font=("times new roman", 15, "bold"), fg="white", bg="green",activeforeground="green",activebackground="yellow")
        name3.place(x=120, y=270)

    #____________________________________________________________________________________________________________________________________

        # name4 = tk.Button(frame,command=self.titleBar, text="Title Bar", font=("times new roman", 15, "bold"), fg="white", bg="green",activeforeground="green",activebackground="yellow")
        # name4.place(x=135, y=320)
    #_________________________________________________________________________________________________________________________________

        # Text on video

        # checkbox 2 - titlebar
        self.titlebar = tk.BooleanVar()
        checkbox2 = tk.Checkbutton(frame, text="TitleBar", font=("Arial", 12), bg="white", fg="blue", activeforeground="green", selectcolor="yellow",variable=self.titlebar)
        checkbox2.place(x=110, y=340)

        # #Checkbox 3 - reverse
        # self.reverse1 = tk.BooleanVar()
        # checkbox3 = tk.Checkbutton(frame, text="Reverse", font=("Arial", 12), bg="white", fg="blue", activeforeground="green",selectcolor="yellow",variable=self.reverse1)
        # checkbox3.place(x=110, y=340)



        name5 = tk.Button(frame,command=self.TextOnVideo, text="Text On Video", font=("times new roman", 15, "bold"), fg="white", bg="green",activeforeground="green",activebackground="yellow")
        name5.place(x=110, y=370)

#__________________________________________________________
    def clear(self):
        self.top5.delete(0,tk.END)
        self.display.delete(0,tk.END)
#__________________________________________________________
    def imgdownloader(self):
        top5 = self.top5.get()
        display = self.display.get()

        imgdownloader(top5,display)

#___________________________________________________________
    def bestChoice(self):
        reverse= self.reverse.get()
        if reverse:
            bestChoice(reverse)
        else:
            bestChoice(False)


    def makeVideo(self):
        makeVideo()
#_________________________________________________

    def TextOnVideo(self):
        titlebar = self.titlebar.get()
        reverse = self.reverse.get()
        print(titlebar)
        print(reverse)
        textOnVideo(titlebar,reverse)





if __name__ == '__main__':
    root = tk.Tk()
    app = AutoVideoMaker(root)
    root.mainloop()







