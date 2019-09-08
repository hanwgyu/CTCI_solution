# 테스트 결과 정확성: 42.9, 효율성: 50.0

def solution(food_times, k):
    a = []
    for food, time in enumerate(food_times):
        a.append((time, food+1))
    a.sort()
    
    idx = 0
    blocks = a[idx][0]*(len(food_times)-idx)
    while k >= blocks:
        k, idx = k-blocks, idx+1
        if idx >= len(food_times):
            return -1
        blocks = (a[idx][0]-a[idx-1][0])*(len(food_times)-idx)
    block = len(food_times)-idx
    while k >= block:
        k = k-block
    new_a = [e[1] for e in a[idx:]]
    new_a.sort()
    return new_a[k%len(new_a)]
