import tkinter.messagebox
from tkinter import *
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox

window = Tk()

mixer.init()

window.geometry("600x600")
window.title("Python Music Player")

menubar = Menu(window)
window.config(menu=menubar)


def browse_file():
    global file_name
    file_name = filedialog.askopenfilename()

def show_help():
    tkinter.messagebox.showinfo("Help", "This is an app created by someone")


submenu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="Open", command=browse_file)
submenu1.add_command(label="Exit", command=window.destroy)

submenu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu2)
submenu2.add_command(label="Help", command=show_help)


def play_music():
    try:
        mixer.music.load(file_name)
        mixer.music.play()
    except:
        tkinter.messagebox.showerror("File Not Found")


def stop_music():
    mixer.music.stop()

def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)



play_photo = PhotoImage(file="play.png")
play_button = Button(window, image=play_photo, command=play_music)
play_button.pack()

stop_photo = PhotoImage(file="stop.png")
stop_button = Button(window, image=stop_photo, command=stop_music)
stop_button.pack()

scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(50)
scale.pack()



window.mainloop()