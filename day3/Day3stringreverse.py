word=input("Enter string: ")
new_list=[]
for i in range(len(word)-1,-1,-1):
        new_list.append(word[i])
word=''.join(new_list)        
print(word)