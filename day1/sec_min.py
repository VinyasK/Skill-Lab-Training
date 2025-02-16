total_num=int(input("Enter total Elements: "))
numbers=[]
for i in range(total_num):
    num=int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Sec_min:",numbers[1])