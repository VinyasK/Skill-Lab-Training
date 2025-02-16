Sales = [10, 20, 15, 30, 25]
prefix_sum = []
sum=0
for sale in Sales:
    sum=sum+sale
    prefix_sum.append(sum)

print("PrefixSum[] =", prefix_sum)
