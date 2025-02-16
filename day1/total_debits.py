total_elements=int(input("Enter total Elements: "))
amount_list=[]
for i in range(total_elements):
    amount=int(input("Enter amount: "))
    amount_list.append(amount)
print(amount_list)
count=0  
for i in range(total_elements):
    if (i==total_elements-1):
        break
    elif amount_list[i]>amount_list[i+1]:
        count=count+1
print("Total debits:",count)