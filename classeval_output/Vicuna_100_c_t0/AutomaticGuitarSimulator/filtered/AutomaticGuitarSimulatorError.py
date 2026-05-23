class AutomaticGuitarSimulator:
    """
    This class is an automatic guitar simulator that can interpret and play based on the input guitar sheet music.
    """

    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play\_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return:list of dict, The dict includes two fields, Chore and Tune, which are letters and numbers, respectively
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play\_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

        """
        chords = self.play\_text.split()
        chord\_dict = {}
        for chord in chords:
            chord\_dict[chord] = None

        tunes = []
        for i in range(len(chords)):
            if chord\_dict[chords[i]] is not None:
                tunes.append(chords[i])
            else:
                tunes.append(chords[i])

        for i in range(len(tunes)):
            tune = tunes[i]
            chord = chord\_dict[tune]
            if display:
                print(f"Normal Guitar Playing -- Chord: {chord}, Play Tune: {tune}")
            else:
                print(f"Chord: {chord}, Play Tune: {tune}")

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return:None
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
        chord = key
        tune = value
        self.display(chord, tune)

# Create an instance of the class
context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
# Call the interpret method
play\_list = context.interpret(display = False)
# Call the display method
context.display("C", "53231323")
# Call the display method again
context.display("Em", "43231323")
# Call the display method again
context.display("F", "43231323")
# Call the display method again
context.display("G", "63231323")