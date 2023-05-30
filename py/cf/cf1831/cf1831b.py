"""
 * 链接：https://codeforces.com/contest/1831/problem/B
"""

from collections import defaultdict


def func(n, a, b):
    c_a, c_b = defaultdict(int), defaultdict(int)
    ans = 1
    la, lb = 1, 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            la += 1
        else:
            c_a[a[i - 1]] = max(c_a[a[i - 1]], la)
            la = 1
        if b[i] == b[i - 1]:
            lb += 1
        else:
            c_b[b[i - 1]] = max(c_b[b[i - 1]], lb)
            lb = 1
    c_a[a[-1]] = max(c_a[a[-1]], la)
    c_b[b[-1]] = max(c_b[b[-1]], lb)
    for k, v in c_a.items():
        ans = max(ans, v + c_b[k])
    for k, v in c_b.items():
        ans = max(ans, v + c_a[k])
    return ans


if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(func(n, a, b))
    # print(func(1, [2], [2]))  # 2
    # print(func(3, [1, 2, 3], [4, 5, 6]))  # 1
    # print(func(2, [1, 2], [2, 1]))  # 2
    # print(func(5, [1, 2, 2, 2, 2], [2, 1, 1, 1, 1]))  # 5
    # print(func(6, [2, 2, 1, 2, 2, 1], [2, 2, 1, 2, 2, 1]))  # 4
