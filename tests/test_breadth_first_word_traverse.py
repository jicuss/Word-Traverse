import unittest
import mock

from lib.breadth_first_approach.word_traverse_dictionary import WordTraverseDictionary
from lib.breadth_first_approach.word_traverse_node import WordTraverseNode
from lib.breadth_first_approach.word_traverse_queue import WordTraverseQueue

class TestWordTraverseDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = WordTraverseDictionary()

    def test_invalid_filename(self):
        self.assertRaises(IOError,lambda :self.dictionary.load_dictionary('bogus.txt'))
        return True

    def test_dictionary_loading(self):
        self.assertIn('the',self.dictionary.dictionary)
        self.assertIn('quick',self.dictionary.dictionary)
        self.assertIn('brown',self.dictionary.dictionary)
        self.assertIn('fox',self.dictionary.dictionary)
        self.assertIn('jumps',self.dictionary.dictionary)
        self.assertIn('over',self.dictionary.dictionary)
        self.assertIn('the',self.dictionary.dictionary)
        self.assertIn('lazy',self.dictionary.dictionary)
        self.assertIn('dog',self.dictionary.dictionary)
        return True

    def test_check_valid_word(self):
        self.assertTrue(self.dictionary.check_valid_word('quick'))
        self.assertTrue(self.dictionary.check_valid_word('brown'))
        self.assertTrue(self.dictionary.check_valid_word('fox'))
        self.assertFalse(self.dictionary.check_valid_word('newwes'))

class TestWordTraverseNode(unittest.TestCase):
    def setUp(self):
        self.mock_dictionary = mock.create_autospec(WordTraverseDictionary)
        self.word_traverse_node = WordTraverseNode(self.mock_dictionary,'thequick',['the'])

    def test_depth(self):
        self.assertEquals(self.word_traverse_node.depth(),1)
        self.word_traverse_node.word_array = []
        self.assertEquals(self.word_traverse_node.depth(),0)
        self.word_traverse_node.word_array = ['the','quick']
        self.assertEquals(self.word_traverse_node.depth(),2)
        return True

    def test_possible_suffixes(self):
        self.assertEquals(self.word_traverse_node.possible_suffixes(),["q", "qu", "qui", "quic", "quick"])

    def test_valid_suffixes(self):
        self.mock_dictionary.check_valid_word.side_effect = [False,False,False,False,True]
        self.assertEquals(self.word_traverse_node.valid_suffixes(),["quick"])

    def test_validity(self):
        self.assertFalse(self.word_traverse_node.check_validity())
        self.word_traverse_node.word_array = ['the','quick']
        self.assertTrue(self.word_traverse_node.check_validity())

    def test_concatted_word_array(self):
        self.word_traverse_node.word_array = ['the','quick']
        self.assertEquals(self.word_traverse_node.concatted_word_array(),'thequick')

    def test_look_possible_suffixes(self):
        self.mock_dictionary.check_valid_word.side_effect = [False,False,False,False,True]
        self.assertEquals(map(lambda x: x.__str__() ,self.word_traverse_node.look_possible_suffixes()),['{"full_string": "thequick", "word_array": ["the", "quick"]}'])
        pass


class TestWordTraverse(unittest.TestCase):
    def setUp(self):
        self.mock_dictionary = mock.create_autospec(WordTraverseDictionary)
        self.dictionary = WordTraverseDictionary()
        self.queue = WordTraverseQueue(self.mock_dictionary)
        self.queue.define_string_to_traverse('thequickbrownfox')
        pass

    def tearDown(self):
        pass

    def test_define_string_to_traverse(self):
        self.assertEquals(map(lambda x: x.__str__() ,self.queue.queue),['{"full_string": "thequickbrownfox", "word_array": []}'])

    def test_add_invalid_item_to_queue(self):
        self.assertRaises(TypeError,lambda : self.queue.add_item_to_queue('bogus'))

    def test_run(self):
        # need to use a real dictionary this time, create a new queue instance, pass it a real dictionary, verify looks good
        queue = WordTraverseQueue(self.dictionary)
        queue.define_string_to_traverse('thequickbrownfox')
        queue.run()
        results = []
        for result in queue.results:
            results.append(' '.join(result.word_array))
        self.assertIn('the quick brown fox',results)


    def test_run_two(self):
        # need to use a real dictionary this time, create a new queue instance, pass it a real dictionary, verify looks good
        queue = WordTraverseQueue(self.dictionary)
        queue.define_string_to_traverse('thequickbrownfoxjumpsoverthelazydog')
        queue.run()
        results = []
        for result in queue.results:
            results.append(' '.join(result.word_array))
        self.assertIn('the quick brown fox jumps over the lazy dog',results)

if __name__ == '__main__':
    unittest.main()

