from collections import deque

def min_stock_prices(prices, k):
    result = []
    dq = deque()  
    
    for i in range(len(prices)):
       
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and prices[dq[-1]] > prices[i]:
            dq.pop()
        
        dq.append(i)

        if i >= k - 1:
            result.append(prices[dq[0]])
    
    return result

prices = [120, 110, 115, 100, 105, 98, 102]
k = 3
print(min_stock_prices(prices, k))  
