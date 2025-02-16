def count_words(paragraph):
    paragraph = paragraph.lower()
    words = paragraph.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
input_paragraph = "the cat and the hat"
output = count_words(input_paragraph)
print(output)  