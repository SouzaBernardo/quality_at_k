class AutomaticGuitarSimulator:  
    """
    This class is an automatic guitar simulator that can interpret and play based on the input guitar sheet music.
    """

    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text



    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return:list of dict, The dict includes two fields, Chore and Tune, which are letters and numbers, respectively
        """
        play_list = []
        if display:
            print(play_list)
        else:
            play_list = self.play_text.split()
             Chore = play_list[0].split()[0]
             Tune = int(play_list[1].split()[1])
            play_list.append({"Chord": Chore, " Tune": Tune})
        return play_list

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return:None
        >>> context = Automatic GuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
        play_list = self.interpret(display=True)
        for item in play_list:
            print(f"{item['Chord']}: {item[' Tune']}")