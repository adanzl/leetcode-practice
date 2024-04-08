"""
 * 链接：https://codeforces.com/problemset/problem/1692/F
"""

from typing import Counter


def func(n, nums):
    if n < 3: return False
    cnt = Counter()
    for num in nums:
        cnt[num % 10] += 1

    def f(suf, c):
        if c == 1:
            return cnt[suf] > 0
        for k, v in cnt.items():
            if v == 0: continue
            if k > suf: continue
            cnt[k] -= 1
            if f(suf - k, c - 1):
                return True
            cnt[k] += 1

        return False

    ans = f(3, 3) or f(13, 3) or f(23, 3)
    return 'YES' if ans else 'NO'


if __name__ == '__main__':
    # arr_list = ['20 22 19 84', '1 11 1 2022', '1100 1100 1100 1111', '12 34 56 78 90', '1 9 8 4', '16 38 94 25 18 99']
    # for arr in arr_list:
    #     a = list(map(int, arr.split()))
    #     print(func(len(a), a))
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = map(int, input().split())
        print(func(n, arr))
