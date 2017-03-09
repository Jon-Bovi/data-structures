
class Trie(object):
    """Trie tree implemented with embedded dictionaries."""

    def __init__(self):
        """Initialize root dictionary."""
        self.dict = {}

    def insert(self, string):
        """Insert a string into the trie."""
        cur_dict = self.dict
        for char in string:
            if char in cur_dict:
                cur_dict = cur_dict[char]
            else:
                cur_dict[char] = {}
                cur_dict = cur_dict[char]
        if '$' not in cur_dict:
            cur_dict['$'] = {}
