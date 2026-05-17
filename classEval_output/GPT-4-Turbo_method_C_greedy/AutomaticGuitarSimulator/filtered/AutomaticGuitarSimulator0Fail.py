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
        score_list = self.play_text.split()
        for score in score_list:
            chord = ''.join([i for i in score if not i.isdigit()])
            tune = ''.join([i for i in score if i.isdigit()])
            play_dict = {'Chord': chord, 'Tune': tune}
            play_list.append(play_dict)
            if display:
                self.display(chord, tune)
        return play_list
    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"