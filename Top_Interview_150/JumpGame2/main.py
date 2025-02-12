def solution(nums: list[int]) -> int:
    n = len(nums) # размер массива
    steps = 0 # количество шагов
    current_end = 0 # маскимальный индекс, на который мы можем прыгнуть с начальной позиции
    farthest = 0 # маскимальный индекс, на который мы можем прыгнуть с текущей позиции

    for i in range(n-1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end: 
            steps += 1
            current_end = farthest  

            if current_end >= n-1:
                break
        
        print(current_end)

    return steps     


# Case 1
print("Case 1 result:")
print(solution([2,3,1,1,4]))

# Case 2
print("Case 2 result:")
print(solution([2,3,0,1,4]))

# Case 3
print("Case 3 result:")
print(solution([0]))