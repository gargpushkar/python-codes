# 1231. Divide Chocolate

sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 5
# sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
# sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4]
k = 6

def is_valid(mid):
    total = 0
    no_of_cuts = 1
    for i in sweetness:
        total += i
        if total > mid:
            total = i
            no_of_cuts += 1
        if no_of_cuts > k+1:
            return False
    return True

left = max(sweetness)
right = sum(sweetness)

while left <= right:
    mid = left + (right-left)//2
    if is_valid(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)