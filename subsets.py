A = "aab"

def get_subsets(I, O, ANS):
    if len(I) == 0:
        ANS.append(O)
        return
    elem = I[0]
    OP1 = O[::]
    OP2 = O[::]
    OP2.append(elem)
    I = I[1:]
    get_subsets(I, OP1, ANS)
    get_subsets(I, OP2, ANS)
    return ANS

print(get_subsets(A, [], []))
