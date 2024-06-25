from guiClass import appGui
import tkinter as tk
from tkinter import ttk



if __name__ == '__main__':

    root = tk.Tk()
    app = appGui(root)

    # input box for  "pic keywords" and "display names"
    top5 = ttk.Entry(root, font=("times new roman", 15, "bold"))
    top5.place(x=160, y=60, width=150)
    display = ttk.Entry(root, font=("times new roman", 15, "bold"))
    display.place(x=160, y=100, width=150)

    # input ---labels and entry-boxes
    app.mylabel(text="Pic Keywords", x=40, y=60)
    app.mylabel(text="Display Names", x=40, y=100)

    # clear text in entry box  --- the function takes entry-box names as input
    app.XClear(330, 70, top5, display)

    # _________________________________________Step 1________________________________________________________
    # image downloader button
    app.mybutton(text="Image downloader", x=130, y=150, command=lambda: app.imgdownloader(top5, display))
    # image folder
    app.iconButton(r'assets\folder.png', command=lambda: app.openfolders('images'), x=310, y=150)

    # _________________________________________Step 2________________________________________________________
    # checkbox- reverse
    app.reverse = tk.BooleanVar()
    app.check(text="Reverse", x=145, y=200, variable=app.reverse)
    # Make Video button
    app.mybutton(text="Make Video", x=150, y=230, command=app.makeVideo)

    # _________________________________________Step 3________________________________________________________
    # checkbox - TitleBar
    app.titlebar = tk.BooleanVar()
    app.check(text="TitleBar", x=140, y=280, variable=app.titlebar)
    # Text On Video -Button
    app.mybutton(text="Text on Video", x=140, y=310, command=app.textOnVideo)
    # done folder
    app.iconButton(r'assets\folder.png', command=lambda: app.openfolders('done'), x=310, y=310)

    # _____________________________________Optional Option_________________________________________________________
    # checkbox - download yourself
    app.ask = tk.BooleanVar()
    app.check(text="download yourself", x=30, y=350, variable=app.ask, command=lambda: app.toggle_button(140, 380))

    # Download button after checkbox clicked
    app.myself = ttk.Entry(font=("times new roman", 15, "bold"))
    app.myselfbutton = tk.Button(command=app.downloadyourself, text="Download", font=("times new roman", 15, "bold"),
                                 fg="white", bg="green", activeforeground="green", activebackground="yellow")

    # gmail Button
    app.iconButton('assets\email.png', command=lambda: app.clicked(ex=90, ey=470), x=45, y=460)
    app.askemail = ttk.Entry(font=("times new roman", 15, "bold"), width=16)
    app.sendemail = tk.Button(command=app.email, text="Send", font=("times new roman", 15, "bold"), fg="white", bg="green",
                              activeforeground="green", activebackground="yellow")

    root.mainloop()
