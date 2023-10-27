import math
def jump_search(data_list, search):
    n = len(data_list)
    step = int(math.sqrt(n))
    prev = 0
    current = prev + step
    while current < n-1 and data_list[current] < search: 
        prev = current
        current = current + step
    if current > n-1:
        current = n-1
    for i in range(prev, current+1):
        if data_list[i] == search:
            return True
    return False
print(jump_search([2,2,4,5,6,7,7,8], 5))