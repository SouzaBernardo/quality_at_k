class AutomaticGuitarSimulator: 
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text



    def interpret(self, display=False):
        
        play_list = []
        for i in self.play_text.split():
            if i.isalpha():
                play_list.append({'Chord': i, 'Tune': self.play_text[self.play_text.index(i):self.play_text.index(i) + 3]})
                self.play_text = self.play_text[self.play_text.index(i) + 3:]
            else:
                play_list.append({'Chord': i, 'Tune': self.play_text[self.play_text.index(i):self.play_text.index(i) + 2]})
                self.play_text = self.play_text[self.play_text.index(i) + 2:]
        if display:
            print(play_list)
        return play_list


    def display(self, key, value):
        
        return "Normal Guitar Playing -- Chord: {}, Play Tune: {}".format(key, value)