"""
 * 链接：https://www.acwing.com/problem/content/4724/
"""

from bisect import bisect_left

# n = int(input())
arr = list(map(int, "10 8 5 3 50 45".split()))  # 2 1 0 -1 0 -1
arr = list(map(int, "10 3 1 10 11".split()))  # 1 0 -1 -1 -1
n = len(arr)
ans = [-1] * n
suf_min = [arr[n - 1]] * n  # 后缀min数组

for i in range(n - 2, -1, -1):
    suf_min[i] = min(suf_min[i + 1], arr[i])

for i in range(n):
    idx = bisect_left(suf_min, arr[i])
    ans[i] = max(idx - i - 2, -1)
print(' '.join(list(map(str, ans))))