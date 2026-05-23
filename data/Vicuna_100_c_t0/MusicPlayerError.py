1. add\_song(self, song): This method should add a song to the playlist.
2. remove\_song(self, song): This method should remove a song from the playlist.
3. play(self): This method should play the current song in the playlist.
4. stop(self): This method should stop the current song in the playlist.
5. switch\_song(self): This method should switch to the next song in the playlist.
6. previous\_song(self): This method should switch to the previous song in the playlist.
7. set\_volume(self, volume): This method should set the volume of the music player.
8. shuffle(self): This method should shuffle the playlist.


>>> musicPlayer = MusicPlayer()
>>> musicPlayer.add_song("song1")
>>> musicPlayer.add_song("song2")
>>> musicPlayer.add_song("song3")
>>> musicPlayer.play()
'song1'
>>> musicPlayer.stop()
True
>>> musicPlayer.switch_song()
True
>>> musicPlayer.previous_song()
True
>>> musicPlayer.set_volume(75)
True
>>> musicPlayer.shuffle()
True