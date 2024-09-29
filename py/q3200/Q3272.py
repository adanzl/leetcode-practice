"""
 * 给你两个 正 整数 n 和 k 。
 * 如果一个整数 x 满足以下条件，那么它被称为 k 回文 整数 。
 * 1、x 是一个 回文整数 。
 * 2、x 能被 k 整除。
 * 如果一个整数的数位重新排列后能得到一个 k 回文整数 ，那么我们称这个整数为 好 整数。
 * 比方说，k = 2 ，那么 2020 可以重新排列得到 2002 ，2002 是一个 k 回文串，所以 2020 是一个好整数。
 * 而 1010 无法重新排列数位得到一个 k 回文整数。
 * 请你返回 n 个数位的整数中，有多少个 好 整数。
 * 注意 ，任何整数在重新排列数位之前或者之后 都不能 有前导 0 。比方说 1010 不能重排列得到 101 。
 * 提示：
 * 1、1 <= n <= 10
 * 2、1 <= k <= 9
 * 链接：https://leetcode.cn/problems/find-the-count-of-good-integers/
"""
import math
from typing import Counter

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def countGoodIntegers(self, n: int, k: int) -> int:
        nn = math.ceil(n / 2)
        total = 10**nn
        hash = set()
        f = n & 1
        ans = 0
        for v in range(total):
            if v % 10 == 0: continue
            val = v
            for i in range(nn - f):
                v, r = divmod(v, 10)
                val += r * 10**(n - i - 1)
            if val % k: continue
            h_s = ''.join(sorted(list(str(val))))
            if h_s in hash:
                continue
            hash.add(h_s)
            cnt = Counter(str(val))
            ans += math.factorial(n) // math.prod([math.factorial(v) for v in cnt.values()])
            if cnt['0']:
                cnt['0'] -= 1
                ans -= math.factorial(n - 1) // math.prod([math.factorial(v) for v in cnt.values()])
        return ans


if __name__ == '__main__':
    # 27
    print(Solution().countGoodIntegers(3, 5))
    # 41457024
    print(Solution().countGoodIntegers(10, 1))
    # 2
    print(Solution().countGoodIntegers(1, 4))
    # 2468
    print(Solution().countGoodIntegers(5, 6))
