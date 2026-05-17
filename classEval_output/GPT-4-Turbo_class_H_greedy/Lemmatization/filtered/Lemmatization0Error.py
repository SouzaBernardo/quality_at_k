class Lemmatization:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        sentence = self.remove_punctuation(sentence)
        pos_tagged = pos_tag(word_tokenize(sentence))
        lemmatized_words = [self.lemmatizer.lemmatize(word, pos=self.get_wordnet_pos(tag)) for word, tag in pos_tagged]
        return lemmatized_words

    def get_pos_tag(self, sentence):
        sentence = self.remove_punctuation(sentence)
        pos_tagged = pos_tag(word_tokenize(sentence))
        return [tag for word, tag in pos_tagged]

    def remove_punctuation(self, sentence):
        return sentence.translate(str.maketrans('', '', string.punctuation))

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return 'a'
        elif treebank_tag.startswith('V'):
            return 'v'
        elif treebank_tag.startswith('N'):
            return 'n'
        elif treebank_tag.startswith('R'):
            return 'r'
        else:
            return 'n'

In the code above, I have completed the class `Lemmatization`. The `lemmatize_sentence` method removes punctuation, tokenizes the sentence, tags each word with its part of speech, and then lemmatizes each word based on its part of speech. The `get_pos_tag` method removes punctuation, tokenizes the sentence, and then tags each word with its part of speech. The `remove_punctuation` method removes all punctuation from the input sentence. The `get_wordnet_pos` method is a helper method that converts treebank tags to wordnet tags, which are used by the WordNetLemmatizer.