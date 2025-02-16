Numbers= [111, 222, 333, 4444, 666,555]
unique_digits = [] 
for num in Numbers:  
    for digit in str(num): 
        digit = int(digit)  
        if digit not in unique_digits:  
            unique_digits.append(digit)
unique_digits=sorted(unique_digits)            
print(unique_digits)
