def solution(prices: list[int]) -> int:
    min_price = float('inf')
    all_profit = 0  

    for price in prices:
        if price < min_price:
            min_price = price
            
        profit = price - min_price

        if profit > 0:
            all_profit += profit
            min_price = price

    
    return all_profit


# Case 1
print("Case 1 result:")
print(solution([7,1,5,3,6,4]))

# Case 2
print("Case 2 result:")
print(solution([1,2,3,4,5]))

# Case 3
print("Case 3 result:")
print(solution([7,6,4,3,1]))