def remove_duplicates(input_string):
    result = ""
    for char in input_string:
        if char not in result:
            result += char 
    return result
input_string = "banana"
output = remove_duplicates(input_string)
print(output) 