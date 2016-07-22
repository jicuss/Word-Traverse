import unittest

from lib.recursive_approach.recursive_word_traverse import WordTraverse


class TestWordTraverse(unittest.TestCase):

    def setUp(self):
        self.wt = WordTraverse()

    def test_assert_identify_options(self):
        self.assertEqual(self.wt.identify_possible_options('thequickbrownfoxjumpsoverthelazydog'),['i', 'a', 'th', 'he', 'ic', 'kb', 'br', 'ow', 'ox', 'so', 'el', 'la', 'do', 'the', 'qui', 'bro', 'row', 'own', 'fox', 'ump', 'dog', 'brow', 'jump', 'umps', 'over', 'vert', 'lazy', 'quick', 'brown', 'jumps', 'overt'])
        return True

    def test_quickbrown(self):
        options = self.wt.identify_possible_options('thequickbrownfoxjumpsoverthelazydog')
        self.assertIn('the quick brown fox jumps over the lazy dog',self.wt.find_solutions('thequickbrownfoxjumpsoverthelazydog',options,[]))

        return True

    def test_flatten_array(self):
        a = [[[[['jo sh']]]], ['josh']]
        self.assertEqual(flatten_array(a),['jo sh','josh'])

if __name__ == '__main__':
    unittest.main()
