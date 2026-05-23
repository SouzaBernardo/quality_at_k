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
        """
        if song not in self.playlist:
            self.playlist.append(song)
            self.current_song = song
            self.volume = random.randint(50, 100)
        else:
            print("Error: song already in the playlist")

    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        :return: None
        """
        if song == self.current_song:
            print("Error: song already in the playlist")
        else:
            self.current_song = None
            self.playlist.remove(song)
            self.volume = random.randint(50, 100)

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.play()
       'song1'

        """
        return self.play_song(self.playlist, self.current_song)


    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_song is None:
            return False
        
        # Get the current song from the playlist
        current_song = self.playlist[self.current_song]
        
        # Stop the song
        current_song.stop()
        
        # Set the current song to the first song in the playlist
        self.playlist.insert(0, current_song)
        
        # Set the current song to None
        self.current_song = None
        
        # Set the volume to 0
        self.volume = 0

    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """
        next_song = self.playlist.pop(0)
        if next_song is None:
            return False
        
        self.current_song = next_song
        self.volume = random.randint(50, 100)
        
        print("Next song: ", next_song)

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        next_song = self.playlist.pop(0)
        if next_song is None:
            return False
        
        self.current_song = next_song
        self.volume = random.randint(50, 100)
        
        print("Previous song: ", next_song)

    def set_volume(self, volume):
        """
        Sets the volume of the music player,ifthe volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to,int.
        :return: True if the volume was set, False if the volume was invalid.
        """
        if volume < 0 or volume > 100:
            print("Invalid volume value, please enter between 0 and 100")
            return False
        
        self.volume = volume
        print("Volume set to: ", self.volume)

