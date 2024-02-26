n = 3

def get_balanced_paranthesis(open_count, closed_count, output_str, ans_list):
    if open_count == 0 and closed_count == 0:
        ans_list.append(output_str)
        return    
    if open_count == closed_count:
        output_str += '('
        get_balanced_paranthesis(open_count-1, closed_count, output_str, ans_list)
    else:
        if open_count > 0:
            output_str1 = output_str + "("
            output_str2 = output_str + ")"
            get_balanced_paranthesis(open_count-1, closed_count, output_str1, ans_list)
            get_balanced_paranthesis(open_count, closed_count-1, output_str2, ans_list)
        else:
            output_str2 = output_str + ")"
            get_balanced_paranthesis(open_count, closed_count-1, output_str2, ans_list)
    return ans_list

print(get_balanced_paranthesis(n, n, "", []))