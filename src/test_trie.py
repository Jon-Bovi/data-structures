
import pytest


@pytest.fixture
def trie():
    """Return initialized trie."""
    from trie import Trie
    trie = Trie()
    return trie


def test_init(trie):
    """Test init gives the trie an empty dict."""
    assert trie._dict == {}


def test_insert_inserts_word(trie):
    """Test insert correctly inserts single word."""
    trie.insert('word')
    assert trie._dict == {'w': {'o': {'r': {'d': {'$': {}}}}}}


def test_insert_inserts_distinct_words(trie):
    """Test insert correctly inserts two totally unlike words."""
    trie.insert('wood')
    trie.insert('app')
    for word in ['wood', 'app']:
        cur_dict = trie._dict
        for char in word:
            assert char in cur_dict
            cur_dict = cur_dict[char]


def test_insert_inserts_similar_words(trie):
    """Test insert correctly inserts similar words."""
    trie.insert('flan')
    trie.insert('flog')
    for word in ['flan', 'flog']:
        cur_dict = trie._dict
        for char in word:
            assert char in cur_dict
            cur_dict = cur_dict[char]
    assert len(trie._dict) == 1
    assert len(trie._dict['f']) == 1


def test_insert_inserts_subword_of_existing_word(trie):
    """Test insert correctly inserts a subword of word already in trie."""
    trie.insert('google')
    trie.insert('goo')
    end_of_flog = trie._dict['g']['o']['o']
    assert '$' in end_of_flog and 'g' in end_of_flog


def test_contains_true(trie):
    """Test contains returns true for word in trie."""
    trie.insert('word')
    assert trie.contains('word')


def test_contains_false(trie):
    """Test contains returns false for word not in trie."""
    trie.insert('word')
    assert trie.contains('worm') is False


def test_contains_subword_is_false(trie):
    """Test contains return false for a subword of word in trie."""
    trie.insert('floggin')
    assert trie.contains('flog') is False


def test_remove_single_word_trie(trie):
    """Test remove works on trie with only that word."""
    trie.insert('word')
    trie.remove('word')
    assert trie._dict == {}


def test_remove_exception(trie):
    """Test remove raises exception if trying to remove word not in trie."""
    with pytest.raises(ValueError):
        trie.insert('word')
        trie.remove('wor')


def test_remove_subword_of_larger_word(trie):
    """Test remove removes a word that is part of a larger word."""
    trie.insert('goo')
    trie.insert('goog')
    trie.remove('goo')
    assert trie._dict == {'g': {'o': {'o': {'g': {'$': {}}}}}}


def test_remove_on_larger_word(trie):
    """Test remove properly removes a word that shares letters with other words."""
    trie.insert('word')
    trie.insert('women')
    trie.remove('word')
    assert trie._dict == {'w': {'o': {'m': {'e': {'n': {'$': {}}}}}}}
