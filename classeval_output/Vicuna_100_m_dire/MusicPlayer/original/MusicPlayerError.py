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
        else:
            print("Song not found in the playlist.")

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.play()
        'song1'

    def stop(self):
        if self.current_song:
            self.current_song.stop()
            self.current_song = None
            return True
        else:
            return False

    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.switch_song()
        True

    def previous_song(self):
        if self.current_song is not None:
            if len(self.playlist) > 0:
                self.current_song = self.playlist.pop(0)
                self.play(self.current_song)
                return True
            else:
                return False
        else:
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