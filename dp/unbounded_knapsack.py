N = 4
W = 8
values = [6, 1, 7, 7]
weights = [1, 3, 4, 5]

def solve(weights, values, W, N):
    if N == 0 or W == 0:
        return 0
    current_weight = weights[N-1]
    if current_weight <= W:
        profit_with_elem = values[N-1] + solve(weights, values, W-weights[N-1], N)
        profit_without_elem = solve(weights, values, W, N-1)
        return max(profit_with_elem, profit_without_elem)
    else:
        return solve(weights, values, W, N-1)
print(solve(weights, values, W, N))


t = [[-1 for _ in range(W+1)] for __ in range(N+1)]

def solve_memo(weights, values, W, N):
    if N == 0 or W == 0:
        return 0
    if t[N][W] != -1:
        return t[N][W]
    current_weight = weights[N-1]
    if current_weight <= W:
        profit_with_elem = values[N-1] + solve_memo(weights, values, W-weights[N-1], N)
        profit_without_elem = solve_memo(weights, values, W, N-1)
        t[N][W] = max(profit_with_elem, profit_without_elem)
        return t[N][W]
    else:
        t[N][W] = solve_memo(weights, values, W, N-1)
        return t[N][W]
print(solve_memo(weights, values, W, N))
print(t[N][W])



t = [[-1 for _ in range(W+1)] for __ in range(N+1)]

def solve_tab(weights, values, W, N):
    for i in range(N+1):
        t[i][0] = 0
    
    for i in range(W+1):
        t[0][i] = 0
    
    for i in range(1, N+1):
        for j in range(1, W+1):
            if weights[i-1] <= j:
                t[i][j] = max(t[i-1][j], values[i-1] + t[i][j-weights[i-1]])
            else:
                t[i][j] = t[i-1][j]
    return t[N][W]

print(solve_tab(weights, values, W, N))