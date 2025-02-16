def first_non_duplicate(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    for char in word:
        if char_count[char]==1:
            return char            
    return -1
word = input("Enter word: ")
result = first_non_duplicate(word)
print(result)  