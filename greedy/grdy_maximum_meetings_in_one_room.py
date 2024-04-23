# https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1
# Maximum Meetings in One Room
# There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is the start time of meeting i and F[i] is the finish time of meeting i. The task is to find the maximum number of meetings that can be accommodated in the meeting room. You can accommodate a meeting if the start time of the meeting is strictly greater than the finish time of the previous meeting. Print all meeting numbers.

# Note: If two meetings can be chosen for the same slot then choose meeting that finishes earlier.

# Example 1:
# Input:
# N = 6
# S = {1,3,0,5,8,5}
# F = {2,4,6,7,9,9} 
# Output:
# {1,2,4,5}
# Explanation:
# We can attend the 1st meeting from (1 to 2), then the 2nd meeting from (3 to 4), then the 4th meeting from (5 to 7), and the last meeting we can attend is the 5th from (8 to 9). It can be shown that this is the maximum number of meetings we can attend.

# Example 2:
# Input:
# N = 1
# S = {3}
# F = {7}
# Output:
# {1}
# Explanation:
# Since there is only one meeting, we can attend the meeting.

N = 1
S = [3]
F = [7]
N = 6
S = [1,3,0,5,8,5]
F = [2,4,6,7,9,9]

arr = []
for i in range(N):
    arr.append([S[i], F[i], i+1])         # 0 index is start time, 1 index is finish time, 2 index is index of original order before sorting.

arr.sort(key= lambda x:x[1])


ans = [arr[0][2]]
count = 1
end_time = arr[0][1]
for i in range(1, N):
    if end_time < arr[i][0]:
        count += 1
        end_time = arr[i][1]
        ans.append(arr[i][2])

# print(count)
print(sorted(ans))
