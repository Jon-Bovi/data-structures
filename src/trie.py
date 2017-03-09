
class Trie(object):
    """Trie tree implemented with embedded dictionaries."""

    def __init__(self):
        """Initialize root dictionary."""
        self._dict = {}
        self.size = 0

    def insert(self, string):
        """Insert a string into the trie."""
        cur_dict = self._dict
        for char in string:
            if char in cur_dict:
                cur_dict = cur_dict[char]
            else:
                cur_dict[char] = {}
                cur_dict = cur_dict[char]
        if '$' not in cur_dict:
            self.size += 1
            cur_dict['$'] = {}

    def contains(self, string):
        """Return whether string in in trie."""
        cur_dict = self._dict
        for char in string:
            if char not in cur_dict:
                return False
            cur_dict = cur_dict[char]
        return '$' in cur_dict

    def size(self):
        """Return size of trie."""
        return self.size

    def remove(self, string):
        """Remove string from trie, if string not in trie, raise exception."""
        dicts = []
        cur_dict = self._dict
        try:
            for char in string:
                dicts.append(cur_dict)
                cur_dict = cur_dict[char]
            cur_dict.pop('$')
        except KeyError:
            raise ValueError('"' + string + '" not in trie.')
        if not dicts[-1][string[-1]]:
            for i in range(-1, -len(dicts) - 1, -1):
                dicts[i].pop(string[i])
                if dicts[i]:
                    break
