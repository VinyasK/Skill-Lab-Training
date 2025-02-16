def is_substring(main_string, sub_string):
    return sub_string in main_string
main_string = "Hello, world"
sub_string = "world"

if is_substring(main_string, sub_string):
    print("Yes, it is a substring.")
else:
    print("No, it is not a substring.")