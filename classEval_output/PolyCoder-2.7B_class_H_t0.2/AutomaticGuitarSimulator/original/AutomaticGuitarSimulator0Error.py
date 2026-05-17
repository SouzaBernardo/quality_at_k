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
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

        """


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
        return "%s %s" % (key, value)

    def play(self, key, value):
        """
        Play chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.play("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
        return "%s %s" % (key, value)

    def play_text(self, text):
        """
        Play the music score with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param text:str, score to be played
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.play_text("C")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
        return self.play_text_with_chord_and_tune(text, self.play_text)

    def play_text_with_chord_and_tune(self, text, play_text):
        """
        Play the music score with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param text:str, score to be played
        :param play_text:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.play_text_with_chord_and_tune("C")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
        return play_text % (text, self.play_text)


class GuitarSimulator(object):
    """
    This class is a guitar simulator that can interpret and play based on the input guitar sheet music.
    """

    def __init__(self, text):
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
        >>> context = GuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

        """


    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = GuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
        return "%s %s" % (key, value)

    def play(self, key, value):
        """
        Play chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = GuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.play("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
        return "%s %s" % (key, value)

    def play_text(self, text):
