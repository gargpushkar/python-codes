# Tasks for Profit
# You are given a list of tasks, each having a deadline and associated profit if completed within the deadline. Each task takes 1 unit of time to complete. What is the maximum profit you can make?

# Example:
# Tasks (deadline, profit): [(4, 20), (2, 10), (2, 40), (1, 30)]
# Output: 90
# Explanation: Order of Tasks: 4, 3, 1


tasks = [(4, 20), (2, 10), (2, 40), (1, 30)]

max_deadline = -1
tasks.sort(key=lambda x : x[1], reverse=True)
for i in tasks:
    max_deadline = max(max_deadline, i[0])

time_list = [-1]*(max_deadline+1)
profit = 0

for i in tasks:
    curr_deadline = i[0]
    curr_profit = i[1]
    for j in range(curr_deadline, 0, -1):
        if time_list[j] == -1:
            profit += curr_profit
            time_list[j] = 1
            break
print(profit)