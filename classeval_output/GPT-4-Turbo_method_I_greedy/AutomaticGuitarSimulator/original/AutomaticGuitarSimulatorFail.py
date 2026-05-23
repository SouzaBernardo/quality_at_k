
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
        :return:list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively
        """
        play_list = []
        chords = self.play_text.split()
        for chord in chords:
            chord_name = ''.join([i for i in chord if not i.isdigit()])
            tune = ''.join([i for i in chord if i.isdigit()])
            play_list.append({'Chord': chord_name, 'Tune': tune})
    
        if display:
            for item in play_list:
                print(f"Chord: {item['Chord']}, Tune: {item['Tune']}")
    
        return play_list
    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"
