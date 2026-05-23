import random
class MusicPlayer:  
    """
    This is a class as a music player that provides to play, stop, add songs, remove songs, set volume, shuffle, and switch to the next or previous song.
    """

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
        :return: None
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.add_song("song1")
        >>> musicPlayer.playlist
        ['song1']

    def remove_song(self, song):
        """
        Removes a song from the playlist.
    
        :param song: The song to remove from the playlist, str.
        """
        if song in self.playlist:
            self.playlist.remove(song)
            self.current_song = None
            self.volume = 50

    def play(self):
        """
        Plays the current song in the playlist.
    
        :return: The current song in the playlist, or False if there is no current song.
        """
        if self.current_song is None:
            return False
        self.playlist[0] = self.current_song
        self.current_song = None
        self.volume = random.randint(0, 100)
        self.play()

    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_song is None:
            return False
        self.current_song = None
        self.play()
        return True

    def switch_song(self):
        if self.playlist:
            self.current_song = self.playlist.pop(0)
            self.play()
            return True
        else:
            return False

    def previous_song(self):
        if self.playlist:
            self.current_song = self.playlist.pop(0)
            self.play()
            return True
        else:
            return False

    def set_volume(self, volume):
        """
        Sets the volume of the music player.
        
        :param volume: The volume to set the music player to, int.
        :return: True if the volume was set, False if the volume was invalid.
        """
        if 0 <= volume <= 100:
            self.volume = volume
            return True
        else:
            return False

    def shuffle(self):
        random.shuffle(self.playlist)