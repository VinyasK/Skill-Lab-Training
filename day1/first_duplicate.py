total_num=int(input("Enter total Elements: "))
numbers=[]
for i in range(total_num):
    num=int(input("Enter number: "))
    numbers.append(num)
for i in numbers:
    if numbers.count(i)>1:
        print("First duplicate: ",i)    
        break