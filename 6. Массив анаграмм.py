def group_anagrams(strings):
    anagrams = {}
    for word in strings:
        key = "".join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values())
