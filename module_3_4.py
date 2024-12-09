def single_root_words(root_words, *other_words):
    same_words = []
    root_words_lower = root_words.lower()
    for value in other_words:
        if root_words_lower in value.lower():
            same_words.append(value)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)