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



photo = PhotoImage(file="play.png")
play_button = Button(window, image=photo, command=play_music)
play_button.pack()


window.mainloop()