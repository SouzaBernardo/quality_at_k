
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
        
        play_list = []
        for i in self.play_text.split():
            play_list.append({'Chord': i[0], 'Tune': i[1:]})
        if display:
            print(play_list)
        return play_list


    def display(self, key, value):
        
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"
