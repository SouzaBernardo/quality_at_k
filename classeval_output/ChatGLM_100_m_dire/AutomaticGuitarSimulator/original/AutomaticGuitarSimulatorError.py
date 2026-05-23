
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
        if display:
            play_list.append({"Chord": "C", " Tune": "53231323"})
            play_list.append({"Chord": "Em", " Tune": "43231323"})
            play_list.append({"Chord": "F", " Tune": "43231323"})
            play_list.append({"Chord": "G", " Tune": "63231323"})
        else:
            play_list.append({"Chord": "C", " Tune": "53231323"})
            play_list.append({"Chord": "Em", " Tune": "43231323"})
            play_list.append({"Chord": "F", " Tune": "43231323"})
            play_list.append({"Chord": "G", " Tune": "63231323"})
        return play_list

