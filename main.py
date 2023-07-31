from tkinter import *
from pygame import mixer

window = Tk()

mixer.init()

window.geometry("600x600")
window.title("Python Music Player")

text_label = Label(window, text="Play Button")
text_label.pack()

def play_music():
    mixer.music.load("cardinal-37075.mp3")
    mixer.music.play()
    print("Music is playing")


def stop_music():
    mixer.music.stop()
    print("Music is stopped")


play_photo = PhotoImage(file="play.png")
play_button = Button(window, image=play_photo, command=play_music)
play_button.pack()

stop_photo = PhotoImage(file="stop.png")
stop_button = Button(window, image=stop_photo, command=stop_music)
stop_button.pack()


window.mainloop()