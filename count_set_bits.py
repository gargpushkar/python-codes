# Count Set Bits
# Given a positive integer n, count the number of set bits in the binary representation of n.

n = 59

arr = []
while(n):
    if n%2 == 0:
        arr.append(0)
    else:
        arr.append(1)
    n//=2

print(arr[::-1])

# 2nd way
n=59
str_num = ""
while(n):
    if n&1:
        str_num += "1"
    else:
        str_num += "0"
    n >>= 1

print(str_num[::-1])
