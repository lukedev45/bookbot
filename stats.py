def num_of_words(text):
    words = text.split()
    return len(words)

def num_of_characters(text):
    characters = {}
    for char in text.lower():
        characters[char] = characters.get(char, 0) + 1
    return characters

def sort_characters(char_dict):
    """Convert a char->count dict to a sorted list of dicts.

    Each item in the returned list is a dict: {"char": <char>, "num": <count>}.
    The list is sorted from greatest to least by the "num" value using .sort()
    and a helper function as the key.
    """
    items = []
    for c, n in char_dict.items():
        items.append({"char": c, "num": n})

    def _num_key(entry):
        return entry["num"]

    items.sort(key=_num_key, reverse=True)
    return items