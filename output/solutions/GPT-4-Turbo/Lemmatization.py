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