class AutomaticGuitarSimulator: 
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
        for line in self.play_text.splitlines():
            if line.strip():
                chords = line.split()
                play_list.append({'Chord': chords[0], 'Tune': chords[1]})
        if display:
            self.display(key='Chord', value=play_list[0]['Chord'])
            self.display(key='Tune', value=play_list[0]['Tune'])
            for item in play_list[1:]:
                self.display(key='Chord', value=item['Chord'])
                self.display(key='Tune', value=item['Tune'])
        return play_list

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323
        """