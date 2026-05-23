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
        :return: True if the song was successfully removed, False otherwise.
        """
        if song in self.playlist:
            self.playlist.remove(song)
            print(" song " + song + " was removed from playlist")
            return True
        else:
            print(" cannot remove song " + song + " from playlist")
            return False

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
        if self.current_song:
            return self.current_song
        random.shuffle(self.playlist)
        current_song = self.playlist[0]
        if current_song:
            self.current_song = current_song
            print(f"Played {current_song}.")
        else:
            print("No song in playlist.")

    def stop(self):
        """
        Stops the current song in the playlist.
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
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.switch_song()
        True
        """
        next_song = self.playlist.index(self.current_song)
        if next_song == -1:
            return False
        self.playlist.append(self.current_song)
        return True

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song2"
        >>> musicPlayer.previous_song()
        True
        """
        if self.playlist:
            prev_song = self.playlist[-1]
            if prev_song:
                self.playlist.remove(prev_song)
                self.current_song = prev_song
                return True
        else:
            return False

    def set_volume(self, volume):
        """
        Sets the volume of the music player,ifthe volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to,int.
        :return: True if the volume was set, False if the volume was invalid.
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
        if self.playlist is not empty:
            random.shuffle(self.playlist)
            return True
        else:
            return False