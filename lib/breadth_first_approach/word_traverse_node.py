import json


class WordTraverseNode():
    def __init__(self, dictionary, full_string, word_array):
        self.dictionary = dictionary
        self.full_string = full_string
        self.word_array = word_array

    def depth(self):
        return len(self.word_array)

    def concatted_word_array(self):
        return ''.join(self.word_array)

    def possible_suffixes(self):
        prefix = self.concatted_word_array()
        suffix = self.full_string.replace(prefix, '')
        possible_options = []

        for n in range(0, len(suffix)):
            possible_options.append(suffix[0:n + 1])

        return possible_options

    def valid_suffixes(self):
        valid_options = filter(lambda x: self.dictionary.check_valid_word(x), self.possible_suffixes())
        return valid_options

    def check_validity(self):
        if self.full_string == self.concatted_word_array():
            return True

    def look_possible_suffixes(self):
        if self.check_validity():
            return []
        else:
            response = []
            for word in self.valid_suffixes():
                new_word_array = list(self.word_array)
                new_word_array.append(word)
                response.append(WordTraverseNode(self.dictionary, self.full_string, new_word_array))

            return response

    def __str__(self):
        return json.dumps({'full_string': self.full_string, 'word_array': self.word_array}, sort_keys=True)