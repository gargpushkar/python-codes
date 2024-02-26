# Print N-bit binary numbers having more 1s than 0s
# Given a positive integer N, the task is to find all the N bit binary numbers having more than or equal 1’s than 0’s for any prefix of the number.

# Example 1:

# Input:  N = 2
# Output: 11 10
# Explanation: 11 and 10 have more than 
# or equal 1's than 0's
# Example 2:

# Input:  N = 3
# Output: 111 110 101
# Explanation: 111, 110 and 101 have more 
# than or equal 1's than 0's


N = 2
def get_n_bit_binary_number(no_1, no_0,  n, output_str, ans):
    if n == 0:
        ans.append(output_str)
        return
    if no_0 > no_1:
        return
    if no_1 == no_0:
        output_str1 = output_str + "1"
        no_1 += 1
        n -= 1
        get_n_bit_binary_number(no_1, no_0, n, output_str1, ans)
    else:
        n -= 1
        output_str1 = output_str + "1"
        output_str2 = output_str + "0"
        t_no_1  = no_1 + 1
        t_no_0  = no_0 + 1
        get_n_bit_binary_number(t_no_1, no_0, n, output_str1, ans)
        get_n_bit_binary_number(no_1, t_no_0, n, output_str2, ans)
    return ans

print(get_n_bit_binary_number(0, 0, N, "", []))