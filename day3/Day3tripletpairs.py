def find_triplets_with_sum(arr, target_sum):
    n = len(arr)
    triplets = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    triplets.append((arr[i], arr[j], arr[k]))
    pairs=set(triplets)                

    return pairs
array_el = int(input("Enter array size: "))
target_sum = int(input("Enter sum: "))
array=[]
for i in range(array_el):
    print("Enter array elements")
    num=int(input())
    array.append(num)

result = find_triplets_with_sum(array, target_sum)
if result:
    count=0
    print("Triplets with the sum of", target_sum, "are:")
    for triplet in result:
        print(triplet)
        count+=1
    print("Number of pair: ",count)    

else:
    print("No triplets found with the sum of", target_sum)