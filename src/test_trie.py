
import pytest


@pytest.fixture
def trie():
    """Return initialized trie."""
    from trie import Trie
    trie = Trie()
    return trie


def test_init(trie):
    """Test init gives the trie an empty dict."""
    assert trie.dict == {}


def test_insert_inserts_word(trie):
    """Test insert correctly inserts single word."""
    trie.insert('word')
    assert trie.dict == {'w': {'o': {'r': {'d': {'$': {}}}}}}


def test_insert_inserts_distinct_words(trie):
    """Test insert correctly inserts two totally unlike words."""
    trie.insert('wood')
    trie.insert('app')
    for word in ['wood', 'app']:
        cur_dict = trie.dict
        for char in word:
            assert char in cur_dict
            cur_dict = cur_dict[char]


def test_insert_inserts_similar_words(trie):
    """Test insert correctly inserts similar words."""
    trie.insert('flan')
    trie.insert('flog')
    for char in ['flan', 'flog']:
        cur_dict = trie.dict
        for char in 'flan':
            assert char in cur_dict
            cur_dict = cur_dict[char]
    assert len(trie.dict) == 1
    assert len(trie.dict['f']) == 1


def test_insert_inserts_subword_of_existing_word(trie):
    """Test insert correctly inserts a subword of word already in trie."""
    trie.insert('google')
    trie.insert('goo')
    end_of_flog = trie.dict['g']['o']['o']
    assert '$' in end_of_flog and 'g' in end_of_flog
