import pygame
import tkinter as tk
from tkinter import filedialog

#function of music player
class MusicPlayer:
    
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
        self.file_path = None
        self.current_index = 0
        self.playlist = []

    def load_music(self, file_path):
        pygame.mixer.music.load(file_path) #select music

    def play_music(self):
        pygame.mixer.music.play() #play music

    def pause_music(self):
        pygame.mixer.music.pause() #pause music

    def stop_music(self):
        pygame.mixer.music.stop() #stop music
    
    def play_next_music(self):
        if self.current_index + 1 < len(self.playlist): 
            self.current_index += 1 
            self.load_music(self.playlist[self.current_index])
            self.play_music()

class MusicPlayerInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.music_player = MusicPlayer()

        self.create_widgets()

    def create_widgets(self):
        # Create a label to display the selected file path
        self.file_label = tk.Label(self.root, text="No file selected")
        self.file_label.pack(pady=10)

        # Create buttons for file selection and music control
        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play music", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause music", command=self.pause_music)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.play_next_music)
        self.next_button.pack(pady=5)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.file_label.config(text=file_path)
            self.music_player.file_path = file_path #type: ignore
            self.music_player.load_music(file_path)

    def play_music(self):
        if self.music_player.file_path:
            self.music_player.play_music()

    def pause_music(self):
        if self.music_player.file_path:
            self.music_player.pause_music()
    
    def stop_music(self):
        if self.music_player.file_path:
            self.music_player.stop_music()
    
    def play_next_music(self):
        if self.music_player.playlist:
            self.music_player.play_next_music()
    
    def start(self):
        self.root.mainloop()

# Usage
interface = MusicPlayerInterface()
interface.start()
