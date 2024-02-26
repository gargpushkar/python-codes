A = "ABC"

def get_permutations(input_list, output_str, ans_list):
    if len(input_list) == 0:
        ans_list.append(output_str)
        return
    elem = input_list[0]
    input_list = input_list[1:]
    output_str1 = output_str
    output_str2 = output_str
    output_str1 += f"{elem}"
    output_str2 += f" {elem}"
    get_permutations(input_list, output_str2, ans_list)
    get_permutations(input_list, output_str1, ans_list)
    return ans_list

# print(get_permutations(A[1:], A[0], []))


A = "ab"
def get_permutations_with_case_change(input_list, output_str, ans_list):
    if len(input_list) == 0:
        ans_list.append(output_str)
        return

    elem = input_list[0]
    input_list = input_list[1:]
    output_str1 = output_str + elem
    output_str2 = output_str + elem.upper()
    get_permutations_with_case_change(input_list, output_str1, ans_list)
    get_permutations_with_case_change(input_list, output_str2, ans_list)
    return ans_list

# print(get_permutations_with_case_change(A, "", []))


A = "a111b2"
def letter_case_permutation(input_list, output_str, ans_list):
    if len(input_list) == 0:
        ans_list.append(output_str)
        return
    elem = input_list[0]
    input_list = input_list[1:]
    if elem.isalpha():
        output_str1 = output_str + elem.lower()
        output_str2 = output_str + elem.upper()
        letter_case_permutation(input_list, output_str1, ans_list)
        letter_case_permutation(input_list, output_str2, ans_list)
    else:
        output_str1 = output_str + elem
        letter_case_permutation(input_list, output_str1, ans_list)
    return ans_list

print(letter_case_permutation(A, "", []))