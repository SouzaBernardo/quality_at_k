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
        """
        Adds a song to the playlist.
        :param song: The song to add to the playlist, str.
        """
        self.playlist.append(song)
    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        """
        if song in self.playlist:
            self.playlist.remove(song)
    
    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        """
        if self.current_song:
            print(f"Playing {self.current_song}")
            return self.current_song
        else:
            print("No song is currently selected.")
            return False
    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_song is not None:
            self.current_song = None
            return True
        else:
            return False
    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """
        if self.current_song is None or self.current_song not in self.playlist:
            return False
    
        current_index = self.playlist.index(self.current_song)
    
        # Check if there is a next song
        if current_index + 1 < len(self.playlist):
            self.current_song = self.playlist[current_index + 1]
            return True
        else:
            return False
    
    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if self.current_song is None or self.playlist.index(self.current_song) == 0:
            return False
        else:
            self.current_song = self.playlist[self.playlist.index(self.current_song) - 1]
            return True
    
    def set_volume(self, volume):
        """
        Sets the volume of the music player, if the volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to, int.
        :return: True if the volume was set, False if the volume was invalid.
        """
        if 0 <= volume <= 100:
            self.volume = volume
            return True
        else:
            return False
    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        if len(self.playlist) > 0:
            random.shuffle(self.playlist)
            return True
        else:
            return False
