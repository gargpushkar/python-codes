# Exponentiation With Modulus
# Given three numbers x, y and z, Calculate (xy) % z.

# Note: % is the modulo operator for finding remainder.

# For example- if x, y and z are 3, 4 and 5 respectively:
# (x**y) % z
# (3**4) % 5 = 1

x = 5
y = 4
z = 3

# Brute
ans = 1
while(y):
    ans = ans*x
    y-=1

print(ans%z)

# Optimized
res = 1
x = x%z
while(y):
    if y&1:     # y is odd
        res = (res*x)%z
    y = y>>1
    x = (x*x)%z

print(res)