
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
        chords = self.play_text.split()
        for chord in chords:
            chord_dict = {}
            chord_dict['Chord'] = chord[:2] if len(chord) > 1 else chord[0]
            chord_dict['Tune'] = chord[2:]
            play_list.append(chord_dict)
        if display:
            for chord_dict in play_list:
                self.display(chord_dict['Chord'], chord_dict['Tune'])
        return play_list
    

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        """
        print("Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value))
    