def group_anagrams(words):
    anagrams = {}  
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []  
        anagrams[sorted_word].append(word)  
    return list(anagrams.values())  
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))  
