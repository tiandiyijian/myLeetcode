_end = '_end_'


class Trie:
    def __init__(self):
        self.root = {}

    def make_trie(self, *words):
        root = self.root
        for word in words:
            current_dict = root
            for i in range(len(word)-1, -1, -1):
                current_dict = current_dict.setdefault(word[i], {})
            current_dict[_end] = True

    def in_trie(self, word):
        current_dict = self.root
        for i in range(len(word)-1, -1, -1):
            current_dict = current_dict.get(word[i], None)
            if not current_dict:
                return False
        return current_dict.get(_end, False)

    def insert(self, word):
        current_dict = self.root
        for i in range(len(word)-1, -1, -1):
            current_dict = current_dict.setdefault(word[i], {})
        current_dict[_end] = True

    def remove(self, word):
        current_dict = self.root
        for i in range(len(word)-1, -1, -1):
            current_dict = current_dict.get(word[i], None)
            if not current_dict:
                return
        current_dict[_end] = False


if __name__ == "__main__":
    t = Trie()
    t.make_trie('ly', 'lyx')
    print(t.in_trie('lyy'))
