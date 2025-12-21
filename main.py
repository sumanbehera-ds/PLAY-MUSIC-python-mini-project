import os
import pygame
import tkinter as tk
from tkinter import filedialog,messagebox

class MusicPlayer:
    def __init__(self,master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("700x400")

        self.play_button = tk.Button(self.master,text="play",command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.master,text="stop",command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.select_button =tk.Button(self.master,text="select music",command=self.select_music)
        self.select_button.pack(pady=5)

        self.music_file = ""

    def play_music(self):
        if self.music_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
        else:
            messagebox.showwarning("warning","please select a music file")

    def stop_music(self):
        pygame.mixer.music.stop()

    def select_music(self):
        self.music_file = filedialog.askopenfilename(initialdir=os.getcwd(),title="select music",
                                                     filetypes=[("mp3 files","*mp3")])
        

if __name__ =="__main__":
    root= tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()