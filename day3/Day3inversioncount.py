P = [30, 45, 25, 60, 20]
length=len(P)
count=0
for i in range(length-1):
    for j in range(i+1,(length)):
        if P[i]>P[j]:
            count=count+1
print("The inversion count is :",count)