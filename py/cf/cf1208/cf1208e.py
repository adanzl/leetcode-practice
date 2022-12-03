"""
 * 链接：https://codeforces.com/problemset/problem/1208/E
"""

from collections import deque


def func(n, w, arr):
    ans = [0] * w
    for nums in arr:
        ln = nums[0]
        q = deque()
        l, r = -1, -1
        for i in range(w):
            nl, nr = max(ln - (w - i), 0), min(i, ln - 1)
            for j in range(r + 1, nr + 1):
                while q and nums[q[-1] + 1] < nums[j + 1]:
                    q.pop()
                q.append(j)
            while q and q[0] < nl:
                q.popleft()
            if nums[q[0] + 1] < 0 and (i >= ln or w - i - 1 >= ln):
                pass
            else:
                ans[i] += nums[q[0] + 1]
            l, r = nl, nr
    return ' '.join(map(str, ans))


if __name__ == '__main__':
    # n, w = map(int, input().split())
    # arr = [list(map(int, input().split())) for _ in range(n)]
    # print(func(n, w, arr))
    # -3088368140
    n, w = map(int, "5 1".split())
    arr = [list(map(int, i_s.split())) for i_s in ["1 -779041019", "1 -779041019", "1 -779041019", "1 -779041019", "1 -779041019"]]
    print(func(n, w, arr))
    # # 10 15 16
    # n, w = map(int, "3 3".split())
    # arr = [list(map(int, i_s.split())) for i_s in ["3 2 4 8", "2 2 5", "2 6 3"]]
    # print(func(n, w, arr))
    # # 7 8
    # n, w = map(int, "2 2".split())
    # arr = [list(map(int, i_s.split())) for i_s in ["2 7 8", "1 -8"]]
    # print(func(n, w, arr))
    # n, w = map(int, input().split())
    # ans = [0] * w
    # q = deque()
    # for _ in range(n):
    #     nums = list(map(int, input().split()))
    #     ln = nums[0]
    #     l, r = -1, -1
    #     q.clear()
    #     for i in range(w):
    #         nl, nr = max(ln - (w - i), 0), min(i, ln - 1)
    #         for j in range(r + 1, nr + 1):
    #             while q and nums[q[-1] + 1] < nums[j + 1]:
    #                 q.pop()
    #             q.append(j)
    #         while q and q[0] < nl:
    #             q.popleft()
    #         if nums[q[0] + 1] < 0 and (i >= ln or w - i - 1 >= ln):
    #             pass
    #         else:
    #             ans[i] += nums[q[0] + 1]
    #         l, r = nl, nr
    # print(' '.join(map(str, ans)))
