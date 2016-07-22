'''
    This is a short benchmarking script. Not the most elegant approach.

'''
# Todo: Flesh this out a bit better
import timeit

from lib.recursive_approach.recursive_word_traverse import WordTraverse
from lib.breadth_first_approach.word_traverse_dictionary import WordTraverseDictionary
from lib.breadth_first_approach.word_traverse_node import WordTraverseNode
from lib.breadth_first_approach.word_traverse_queue import WordTraverseQueue


def recursive_approach():
    wt = WordTraverse()
    options = wt.identify_possible_options('thequickbrownfoxjumpsoverthelazydog')
    wt.find_solutions('thequickbrownfoxjumpsoverthelazydog',options,[])


def breadth_first():
    dictionary = WordTraverseDictionary()
    queue = WordTraverseQueue(dictionary)
    queue.define_string_to_traverse('thequickbrownfoxjumpsoverthelazydog')
    queue.run()

def time_word_traverse_approaches():
    # time the recursive approach
    timeit.timeit('recursive_approach()', number=100, setup="from test_approach_benchmark import *")

    # time the breadth first approach
    timeit.timeit('breadth_first()', number=100, setup="from test_approach_benchmark import *")


