
class WordNode:
    def __init__(self, word_info):
        self.name, self.meta = word_info
        self.definitions = {}

    def add_definition(self, synset):
        self.definitions[synset.name()] = synset.definition()

    def __str__(self):
        return str((self.name, *self.meta))
        
    def __hash__(self):
        return hash((self.name, *self.meta))

class MetaNode(WordNode):
    def __init__(self, name, opposites=None):
        super(MetaNode, self).__init__((name, ('meta',)))
        self.opposites = opposites if opposites is not None else []


    