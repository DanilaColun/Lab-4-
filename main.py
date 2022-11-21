# var 2, Колун Дэнилэ Васильевич R3138 373732


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from itertools import count
from KEY2 import key_code
import pygame


# FUNCTION TO DIVIDE THE GIF ANIMATION AND MAKE IT PLAY
class ImageLabel(tk.Label):

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


# FUNCTION TO MAKE KEY GENERATOR WORKING
def key_result():
    key_output.configure(text=key_code())


# MUSIC PLAYING IN THE BACKGROUND
def music_track():
    pygame.mixer.music.load("track.mp3")
    pygame.mixer.music.play(-1)


# WINDOW AND OTHER THINGS
root = tk.Tk()
pygame.mixer.init()
root.title("KeyGenerator")
root.geometry("1920x1080")
lblgif = ImageLabel(root)
lblgif.pack()


# THE BACKGROUND ANIMATION
bg = tk.PhotoImage(lblgif.load("GIFKA.gif"))
lbl_bg = tk.Label(root, image=bg)
lbl_bg.place(x=0, y=0)


# THE FRAME WHICH IS IN THE MIDDLE
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")


# THE TEXT IN THE MIDDLE OF THE FRAME
lbl_key = tk.Label(frame, text="ULTRA KEY GENERATOR TERRARIA", font=("Arial", 20), fg="#000000")
lbl_key.grid(column=0, row=0, padx=10, pady=15)


# KEY GENERATOR OUTPUT
key_output = tk.Label(frame, font=("Arial", 20))
key_output.grid(column=0, row=1, padx=10, pady=10)


# BUTTON IN THE BOTTOM
btn_gen = tk.Button(frame, text="Click to generate your key!", font=("Arial", 15), command=key_result)
btn_gen.grid(column=0, row=2, pady=15)


music_track()
root.mainloop()