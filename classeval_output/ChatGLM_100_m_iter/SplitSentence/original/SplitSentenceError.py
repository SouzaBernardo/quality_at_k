import re
class SplitSentence:  
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """



    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        """
        sentences = sentences_string.split(" ")
        sentences = [sentence.strip() for sentence in sentences]
        return sentences

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        """
        # Split the sentence into words using the'split' method and remove any trailing whitespace
        words = sentence.split(" ")
        words = [word.strip() for word in words]

        # Count the number of words in the sentence
        word_count = len(words)

        # Return the number of words in the sentence
        return word_count

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        """
        # Split the sentences into words using the'split' method and remove any trailing whitespace
        sentences = sentences_string.split(" ")
        sentences = [sentence.strip() for sentence in sentences]

        # Create a dictionary to store the sentence length and word count
        sentence_lengths = {}

        # Loop through each sentence and count the number of words
        for sentence in sentences:
            # Split the sentence into words using the'split' method and remove any trailing whitespace
            words = sentence.split(" ")
            words = [word.strip() for word in words]

            # Check if the sentence is the longest sentence in the file
            if sentence_lengths.get(sentence, 0):
                # If it is, add the sentence length to the dictionary
                sentence_lengths[sentence] = len(words)
            else:
                # If it isn't, add the word count to the dictionary
                sentence_lengths[sentence] = word_count

        # Return the number of words in the longest sentence
        return sentence_lengths.get(sentence, 0) + word_count