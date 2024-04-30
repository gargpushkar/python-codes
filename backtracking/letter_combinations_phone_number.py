# Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

digits = "23"
hash_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

def solve(i, output_list, ans):
    if len(output_list) == len(digits):
        if output_list:
            ans.append("".join(output_list))
        return
    
    for char in hash_map[str(digits[i])]:
        output_list.append(char)
        solve(i+1, output_list, ans)
        output_list.pop()
ans = []
solve(0, [], ans)
print(ans)