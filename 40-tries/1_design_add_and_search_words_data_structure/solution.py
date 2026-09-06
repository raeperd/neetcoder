class WordDictionary:
    def __init__(self):
        raise NotImplementedError("Implement WordDictionary.__init__")

    def add_word(self, word: str) -> None:
        raise NotImplementedError("Implement WordDictionary.add_word")

    def search(self, word: str) -> bool:
        raise NotImplementedError("Implement WordDictionary.search")
