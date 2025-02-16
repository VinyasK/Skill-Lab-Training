def next_greater_recursive(prices, index=0):
    if index == len(prices):
        return []
    
    def find_next_greater(idx):
        if idx >= len(prices):  
            return -1  
        if prices[idx] > prices[index]:  
            return prices[idx]  
        return find_next_greater(idx + 1)  

    next_greater_value = find_next_greater(index + 1)
    
    return [next_greater_value] + next_greater_recursive(prices, index + 1)

print(next_greater_recursive([6, 8, 0, 1, 3]))  
print(next_greater_recursive([1, 3, 2, 4]))    
print(next_greater_recursive([10, 20, 30, 50])) 
print(next_greater_recursive([50, 40, 30, 10])) 
