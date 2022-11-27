"""
 * 链接：https://www.acwing.com/problem/content/4727/
"""
from collections import Counter
# n, k = map(int, input().split())
# num = input()
n, k = 8, 4
num = '22294777'  # 2 22274777
n, k = 3, 2
num = '531'  # 2 331
cnt = Counter(num)
for c in cnt.values():
    if c >= k:
        print(0)
        print(num)
        exit()
ans_cost = 0x3c3c3c3c
t_num = []
for t in range(10):
    t_cost = 0
    nx = sorted(list(range(10)), key=lambda x: (abs(t - x), -x))
    cc = k
    for i in nx:
        nn = min(cnt[str(i)], cc)
        cc -= nn
        t_cost += abs(i - t) * nn
        if cc == 0: break
    if t_cost == ans_cost: t_num.append(t)
    if t_cost < ans_cost:
        ans_cost = t_cost
        t_num = [t]

ans = []
for t in t_num:
    nx = sorted(list(range(10)), key=lambda x: (abs(t - x), -x))
    cc = k
    ans_num = list(num)
    for i in nx:
        nn = min(cnt[str(i)], cc)
        cc -= nn
        if cc == 0:
            cn = 0
            if t > i:
                for j in range(n - 1, -1, -1):
                    if str(i) == ans_num[j]:
                        ans_num[j] = str(t)
                        cn += 1
                    if cn == nn: break
            else:
                for j in range(n):
                    if str(i) == ans_num[j]:
                        ans_num[j] = str(t)
                        cn += 1
                    if cn == nn: break
            break
        else:
            for j in range(n):
                if str(i) == ans_num[j]:
                    ans_num[j] = str(t)
    ans.append(ans_num)

print(ans_cost)
print("".join(min(ans)))
