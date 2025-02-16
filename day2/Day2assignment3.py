Fuel = [5, 10, 3, 7, 8]
postfix_sum = []
sum = 0
for i in range(len(Fuel) - 1, -1, -1):  
    sum += Fuel[i]
    postfix_sum.append(sum)
postfix_sum.reverse()  
print("PostfixSum[] =", postfix_sum)
