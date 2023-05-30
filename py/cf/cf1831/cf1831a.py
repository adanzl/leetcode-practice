"""
 * 链接：https://codeforces.com/contest/1831/problem/A
"""


def func(n, arr):
    nums = [i for i in range(1, n + 1)]
    ans = []
    for num in arr:
        ans.append(str(n - nums[num - 1] + 1))
    return ans


if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        n = int(input())
        arr = map(int, input().split())
        print(" ".join(func(n, arr)))
    # print(" ".join(func(5, [1, 2, 4, 5, 3])))  # 1 2 4 3 5
    # print(" ".join(func(2, [1, 2])))  # 2 1
    # print(" ".join(func(1, [1])))  # 1
    # print(" ".join(func(3, [3, 2, 1])))  # 1 2 3
    # print(" ".join(func(4, [1, 4, 3, 2])))
