"""
 * 链接：https://www.acwing.com/problem/content/4620/
"""


# x = a - x^a
# a=0 时 x=1；a=1 时 x任意
def bit_count(x):
    ret = 0
    while x:
        if x & 1: ret += 1
        x >>= 1
    return ret


T = int(input())
for _ in range(T):
    a = int(input())
    print(1 << bit_count(a))
