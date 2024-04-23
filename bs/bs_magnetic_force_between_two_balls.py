# 1552. Magnetic Force Between Two Balls

# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

 

# Example 1:
# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

# Example 2:
# Input: position = [5,4,3,2,1,1000000000], m = 2
# Output: 999999999
# Explanation: We can use baskets 1 and 1000000000.

position = [269826447,974181916,225871443,189215924,664652743,592895362,754562271,335067223,996014894,510353008,48640772,228945137]
m = 3

def is_safe(mid):
    last_pos = position[0]
    no_of_balls = 1
    for i in position:
        if i-last_pos >= mid:
            last_pos = i
            no_of_balls += 1
        if no_of_balls == m:
            return True
    # print(no_of_balls)
    return False

position.sort()
left = 0
right = position[-1]
ans = -1
while left <= right:
    mid = left + (right-left)//2
    if is_safe(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)