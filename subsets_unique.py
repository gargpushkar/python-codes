A = [1, 2, 1]

def get_unique_subsets(input, output, ans_list, hash_map):
    if len(input) == 0:
        output_str = "".join(map(str, output))
        if output_str in hash_map:
            return
        hash_map[output_str] = 1
        ans_list.append(output)
        return
    elem = input[0]
    input = input[1:]
    output1 = output[::]
    output2 = output[::]
    output2.append(elem)
    get_unique_subsets(input, output1, ans_list, hash_map)
    get_unique_subsets(input, output2, ans_list, hash_map)
    return ans_list

s = set()
print(get_unique_subsets(A, [], [], {}))