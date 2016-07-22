'''
    Word Traverse Example
    Objective: Give a string consisting of multiple words that are non deliminated, find all possible combinations of words that satisfy that string
    Example: thequickbrownfoxjumpsoverthelazydog => ['The quick brown fox jumps over the lazy dog']
'''

import re
from lib.array_operations import flatten_array


class WordTraverse():

    def __init__(self,dictionary_path='../../dictionary/wordsEn.txt'):
        self.load_dictionary(dictionary_path)

    def load_dictionary(self,dictionary_path):
        ''' load a dictionary of possible words, default is an english reference '''
        self.dictionary = []
        with open(dictionary_path, 'r') as f:
            for line in f.readlines():
                self.dictionary.append(re.sub(r'\r|\n', '', line ))

    def identify_possible_options(self,string):
        ''' return an array of words contained in the input string '''
        word_length = 1
        matches = []

        while word_length <= len(string):
            index_start = 0
            index_end =  index_start + word_length

            while index_end <= len(string):
                word = string[index_start:index_end]
                if word in self.dictionary:
                    if word not in matches:
                        matches.append(word)
                index_start += 1
                index_end += 1

            word_length += 1

        return matches

    def find_solutions(self,parent_string, dictionary, working_array):
        '''
        :param parent_string: the complete string to work on, IE  sometimesifart
        :param previous_string: the prevent portion of the string to evaluate. IE sometimes
        :param dictionary: an array of possible words to test
        :return:
        '''
        matches = []
        final_matches = []
        previous_string = ''.join(working_array)
        for word in dictionary:
            regexp = r'' + previous_string + word
            if re.match(regexp, parent_string):
                matches.append(word)

        for m in matches:
            new_working_array = list(working_array)
            new_working_array.append(m)
            response = self.find_solutions(parent_string, dictionary, new_working_array)
            if response:
                final_matches.append(response)

        if previous_string == parent_string:
            final_matches.append(' '.join(working_array))

        if final_matches != []:
            return flatten_array(final_matches)

