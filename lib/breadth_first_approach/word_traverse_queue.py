from lib.breadth_first_approach.word_traverse_node import WordTraverseNode


class WordTraverseQueue():
    def __init__(self, dictionary):
        self.queue = []
        self.rejects = []
        self.results = []
        self.dictionary = dictionary

    def add_item_to_queue(self, node):
        if isinstance(node, WordTraverseNode):
            self.queue.insert(0, node)
        else:
            raise (TypeError, 'Not Valid Node')

    def define_string_to_traverse(self, string_to_traverse):
        # inserts at the beginning so the last item is the most urgent
        self.add_item_to_queue(WordTraverseNode(self.dictionary, string_to_traverse, []))

    def run(self):
        # grab the last item in the queue
        while self.queue != []:
            node = self.queue.pop()
            if node.check_validity():
                self.results.append(node)
            else:
                for suffix in node.look_possible_suffixes():
                    self.add_item_to_queue(suffix)