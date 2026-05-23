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
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.add_song("song1")
        >>> musicPlayer.playlist
        ['song1']

        """
        
        self.playlist.append(song)

    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.remove_song("song1")
        >>> musicPlayer.playlist
        ['song2']

        """
        
        self.playlist.remove(song)

    def current_song(self):
        """
        Returns the current song in the playlist.
        :return: True if the current song was found, False if there was no current song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song()
        'song1'

    def play(self):
        """
        :return: The current song in the playlist, or False if there is no current song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.play()
        'song1'

        """
        
        if self.current_song:
            return self.current_song
        else:
            return False

    def stop(self):
        """
        :return: True if the current song was stopped, False if there was no current song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.stop()
        True

        """
        
        if self.current_song:
            self.current_song = None
            return True
        else:
            return False

    def switch_song(self):
        """
        :return: True if the next song was switched to, False if there was no next song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.switch_song()
        True

        """
        
        if self.current_song:
            self.current_song = self.playlist[0]
            return True
        else:
            return False

    def previous_song(self):
        """
        :return: True if the previous song was switched to, False if there was no previous song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song2"
        >>> musicPlayer.previous_song()
        True

        """
        
        if self.current_song:
            self.current_song = self.playlist[self.playlist.index(self.current_song) - 1]
            return True
        else:
            return False

    def set_song(self, song):
        """
        :param song: The song to set the current song to.
        :return: True if the current song was set, False if there was no current song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.set_song("song2")
        True

        """
        
        if self.current_song:
            self.current_song = song
            return True
        else:
            return False

    def volume(self):
        """
        :return: True if the volume was found, False if there was no current volume.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.volume()
        50

        """
        
        return self.volume

    def set_volume(self, volume):
        """
        :param volume: The volume to set the music player to,int.
        :return: True if the volume was set, False if the volume was invalid.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.set_volume(50)
        >>> musicPlayer.volume
        50

        """
        
        if volume >= 0 and volume <= 100:
            self.volume = volume
            return True
        else:
            return False

    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.shuffle()
        True

        """
        
        
        return False