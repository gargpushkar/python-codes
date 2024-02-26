A = [1, 2, 3, 4, 5]
target = 16

def has_valid_subset(inpt, otpt, target, bool_list):
    if otpt == target:
        bool_list[0] = True
        return
    if len(inpt) == 0:
        return
    elem = inpt[0]
    inpt = inpt[1:]
    otpt1 = otpt
    otpt2 = otpt
    otpt2 += elem
    has_valid_subset(inpt, otpt1, target, bool_list)
    has_valid_subset(inpt, otpt2, target, bool_list)
    return bool_list[0]

print(has_valid_subset(A, 0, target, [False]))