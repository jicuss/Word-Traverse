import re


class WordTraverseDictionary():
    def __init__(self, dictionary_path='../../dictionary/wordsEn.txt'):
        self.load_dictionary(dictionary_path)

    def load_dictionary(self, dictionary_path):
        ''' load a dictionary of possible words, default is an english reference '''
        self.dictionary = []
        with open(dictionary_path, 'r') as f:
            for line in f.readlines():
                self.dictionary.append(re.sub(r'\r|\n', '', line))

    def check_valid_word(self, word):
        if word in self.dictionary:
            return True