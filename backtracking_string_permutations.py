# String Permutations
# Given a string s with distinct lowercase English characters, find all the permutations of s.

# Example:
# s: “abc”
# Permutations:
# “abc”
# “acb”
# “bac”
# “bca”
# “cab”
# “cba”

arr = "ABC"

# output = []

# def get_subsets(input_array, output_array, output_str):
#     if len(input_array) == 0:
#         output_array.append(output_str)
#         return
    
#     output_str1 = output_str + input_array[0]
#     output_str2 = output_str
#     get_subsets(input_array[1:], output_array, output_str1)
#     get_subsets(input_array[1:], output_array, output_str2)

# get_subsets(arr, output, "")
# print(output)


# Using Recursion
def permute(input_array, output_array, output_str):
    if len(input_array) == 0:
        output_array.append(output_str)
        return
    s = set()
    for i in range(len(input_array)):
        if input_array[i] not in s:
            s.add(input_array[i])
            new_input_array = input_array[::]
            elem = new_input_array.pop(i)
            new_output_str = output_str + elem
            permute(new_input_array, output_array, new_output_str)

# output_array = []
# permute(list(arr), output_array, "")
# print(output_array)


# Using Backtracking

def permute_back(input_array, starting_index, output_array):
    if starting_index == len(input_array)-1:
        output_array.append(input_array[::])
        return
    
    for i in range(starting_index, len(input_array)):
        input_array[starting_index], input_array[i] = input_array[i], input_array[starting_index]
        permute_back(input_array, starting_index+1, output_array)
        input_array[starting_index], input_array[i] = input_array[i], input_array[starting_index]


# def permute2(a, l, r): 
#     if l == r: 
#         print(a) 
#     else: 
#         for i in range(l, r): 
#             a[l], a[i] = a[i], a[l] 
#             permute2(a, l+1, r) 
#             a[l], a[i] = a[i], a[l]  # backtrack 
  
# permute2(list(arr), 0, len(arr))
output_array = []
permute_back([1, 2, 3, 4], 0, output_array)
print(output_array)