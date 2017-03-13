
import pytest

WORDS = ['wood', 'wired', 'women', 'word', 'alien', 'allen', 'okra', 'okay', 'wombat']
TRAVERSALS = [
    ['', ['wood', 'wired', 'women', 'word', 'alien', 'allen', 'okra', 'okay', 'wombat']],
    ['w', ['wood', 'wired', 'women', 'word', 'wombat']],
    ['wo', ['wood', 'women', 'word', 'wombat']],
    ['wom', ['women', 'wombat']],
    ['woo', ['wood']],
    ['wood', ['wood']],
    ['ok', ['okra', 'okay']],
    ['okaydokay', []],
]


@pytest.fixture
def trie():
    """Return empty trie."""
    from trie import Trie
    trie = Trie()
    return trie


@pytest.fixture
def filled_trie(trie):
    """Return trie with words."""
    for word in WORDS:
        trie.insert(word)
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
    end_of_goo = trie._dict['g']['o']['o']
    assert '$' in end_of_goo and 'g' in end_of_goo


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


def test_size_of_empty(trie):
    """Test size method returns 0 for empty trie."""
    assert trie.size == 0


def test_size_of_non_empty(filled_trie):
    """Test size of trie equals number of words in trie."""
    assert filled_trie.size == len(WORDS)


def test_size_after_inserting_same_word(filled_trie):
    """Test size stays same if word already in trie inserted again."""
    filled_trie.insert('wood')
    assert filled_trie.size == len(WORDS)


def test_size_after_removal(filled_trie):
    """Test size decreases by one after one word is removed."""
    filled_trie.remove('wood')
    assert filled_trie.size == len(WORDS) - 1


@pytest.mark.parametrize('start, matches', TRAVERSALS)
def test_traversals(start, matches, filled_trie):
    """Test various traversals on trie."""
    for match in list(filled_trie.traversal(start)):
        assert match in matches


@pytest.mark.parametrize('start, matches', TRAVERSALS)
def test_autocomplete(start, matches, filled_trie):
    """Test autocomplete returns first n matches."""
    if matches:
        for n in range(len(matches) + 2):
            result = filled_trie.autocomplete(start, n)
            assert len(result) == min(n, len(matches))
            for word in result:
                assert start in word
