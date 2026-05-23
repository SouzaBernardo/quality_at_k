import random
class MusicPlayer: 
    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
        self.playlist = []
        self.current_song = None
        self.volume = 50



    def add_song(self, song):
        

        self.playlist.append(song)


    def remove_song(self, song):
        

        self.playlist.remove(song)


    def play(self):
        

        if self.current_song is None:
            return False
        else:
            return self.current_song


    def stop(self):


    def switch_song(self):


    def previous_song(self):


    def set_volume(self, volume):


    def shuffle(self):
