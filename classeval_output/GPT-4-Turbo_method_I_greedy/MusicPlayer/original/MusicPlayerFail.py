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
        else:
            print("The song is not in the playlist.")
    
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
        if self.current_song:
            print(f"Stopping {self.current_song}")
            self.current_song = None
            return True
        else:
            print("No song is currently playing.")
            return False
    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """
        if self.current_song in self.playlist:
            current_index = self.playlist.index(self.current_song)
            if current_index + 1 < len(self.playlist):
                self.current_song = self.playlist[current_index + 1]
                print(f"Switched to {self.current_song}")
                return True
            else:
                print("This is the last song in the playlist.")
                return False
        else:
            print("No song is currently selected.")
            return False
    
    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if self.current_song in self.playlist:
            current_index = self.playlist.index(self.current_song)
            if current_index - 1 >= 0:
                self.current_song = self.playlist[current_index - 1]
                print(f"Switched to {self.current_song}")
                return True
            else:
                print("This is the first song in the playlist.")
                return False
        else:
            print("No song is currently selected.")
            return False

    def set_volume(self, volume):
        """
        Sets the volume of the music player,ifthe volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to,int.
        :return: True if the volume was set, False if the volume was invalid.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.set_volume(50)
        >>> musicPlayer.volume
        50

        """
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"Volume set to {self.volume}")
            return True
        else:
            print("Invalid volume. Volume should be between 0 and 100.")
            return False
    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        if self.playlist:
            random.shuffle(self.playlist)
            print("Playlist has been shuffled.")
            return True
        else:
            print("The playlist is empty.")
            return False
