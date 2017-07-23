
from stack import Stack


class Trie(object):
    """Trie tree implemented with embedded dictionaries."""

    def __init__(self):
        """Initialize root dictionary."""
        self._dict = {}
        self._size = 0

    def insert(self, string):
        """Insert a string into the trie."""
        subtrie = self._dict
        for letter in string:
            if letter in subtrie:
                subtrie = subtrie[letter]
            else:
                subtrie[letter] = {}
                subtrie = subtrie[letter]
        if '$' not in subtrie:
            self._size += 1
            subtrie['$'] = {}

    def contains(self, string):
        """Return whether string in in trie."""
        subtrie = self._dict
        for letter in string:
            if letter not in subtrie:
                return False
            subtrie = subtrie[letter]
        return '$' in subtrie

    @property
    def size(self):
        """Return size of trie."""
        return self._size

    def remove(self, string):
        """Remove string from trie, if string not in trie, raise exception."""
        dicts = []
        subtrie = self._dict
        try:
            for letter in string:
                dicts.append(subtrie)
                subtrie = subtrie[letter]
            subtrie.pop('$')
            self._size -= 1
        except KeyError:
            raise KeyError('"' + string + '" not in trie.')
        if not dicts[-1][string[-1]]:
            for i in range(-1, -len(dicts) - 1, -1):
                dicts[i].pop(string[i])
                if dicts[i]:
                    break

    def autocomplete(self, string, n=5):
        """Return first n words that partially match given string."""
        matches = self.traversal(string)
        n_matches = []
        try:
            for i in range(n):
                n_matches.append(next(matches))
        except (StopIteration, TypeError) as e:
            pass
        return n_matches

    def traversal(self, start):
        """Return all words starting with start."""
        subtrie = self._dict
        for letter in start:
            try:
                subtrie = subtrie[letter]
            except KeyError:
                return
        for word in self._depth_first_traverse(subtrie, start):
            yield word

    def _depth_first_traverse(self, subtrie, word):
        """Yield words contained in given trie."""
        for letter in subtrie:
            if letter == '$':
                yield word
            else:
                for w in self._depth_first_traverse(subtrie[letter], word + letter):
                    yield w
