def length_of_longest_substring(s):
    seen_chars = set() 
    left = 0 
    max_length = 0  
    for right in range(len(s)):
        while s[right] in seen_chars:
            seen_chars.remove(s[left]) 
            left += 1  
        seen_chars.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))     
print(length_of_longest_substring("pwwkew"))   
