from .solution import WordDictionary


def test_word_dictionary_example1():
    word_dict = WordDictionary()
    word_dict.add_word("bad")
    word_dict.add_word("dad")
    word_dict.add_word("mad")
    assert word_dict.search("pad") == False
    assert word_dict.search("bad") == True
    assert word_dict.search(".ad") == True
    assert word_dict.search("b..") == True
