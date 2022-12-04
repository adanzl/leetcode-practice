"""
 * 链接：https://www.acwing.com/problem/content/4614/
"""


from collections import Counter, defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
r = defaultdict(Counter)
for num in arr:
    for i in range(1, 11):
        r[i][num * 10**i % k] += 1
# print(r)
ans = 0
for num in arr:
    i, nn = 0, num
    while nn:
        i += 1
        nn //= 10
    idx = (k - num % k) % k
    # print(i, num, idx, r[i][idx])
    ans += r[i][idx] - (1 if num * 10**i % k == idx else 0)
print(ans)