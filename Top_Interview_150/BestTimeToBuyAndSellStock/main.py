def solution(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0  

    for price in prices:
        if price < min_price:
            min_price = price
            
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit
    
    return max_profit


# Case 1
print("Case 1 result:")
print(solution([7,1,5,3,6,4]))

# Case 2
print("Case 2 result:")
print(solution([7,6,4,3,1]))

# Case 3
print("Case 3 result:")
print(solution([1]))