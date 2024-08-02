# Push Dominoes

# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
# You are given a string dominoes representing the initial state where:
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.

# Example 2:
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque()
        dominoes = list(dominoes)
        n = len(dominoes)
        for i in range(n):
            if dominoes[i] != '.':
                q.append([i, dominoes[i]])
        
        while q:
            indx, elem = q.popleft()
            if elem == "L":
                if indx > 0 and dominoes[indx - 1] == ".":
                    dominoes[indx - 1] = "L"
                    q.append([indx - 1, "L"])
            elif elem == "R":
                if indx + 1 < n and dominoes[indx + 1] == ".":
                    if indx + 2 < n and dominoes[indx + 2] == "L":
                        q.popleft()
                    else:
                        dominoes[indx + 1] = "R"
                        q.append([indx+1, "R"])
        return "".join(dominoes)
