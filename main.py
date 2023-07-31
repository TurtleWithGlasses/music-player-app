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
        paused
    except:
        try:
            mixer.music.load(file_name)
            mixer.music.play()
        except:
            tkinter.messagebox.showerror(title="File Error", message="File not found")
    else:
        mixer.music.unpause()


def stop_music():
    mixer.music.stop()

def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)

def pause_music():
    global paused
    paused = True
    mixer.music.pause()

def rewind_music():
    play_music()


frame = Frame(window)
frame.pack(padx=10, pady=10)


play_photo = PhotoImage(file="play.png")
play_button = Button(frame, image=play_photo, command=play_music)
play_button.grid(row=0, column=0, padx=10)

stop_photo = PhotoImage(file="stop.png")
stop_button = Button(frame, image=stop_photo, command=stop_music)
stop_button.grid(row=0, column=1, padx=10)

pause_photo = PhotoImage(file="pause.png")
pause_button = Button(frame, image=pause_photo, command=pause_music)
pause_button.grid(row=0, column=2, padx=10)

bottom_frame = Frame(window)
bottom_frame.pack()

rewind_photo = PhotoImage("rewind-arrows.png")
rewind_button = Button(bottom_frame, image=rewind_photo, command=rewind_music)
rewind_button.grid(row=0, column=0)

scale = Scale(bottom_frame, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(50)
scale.grid(row=0, column=1)


window.mainloop()