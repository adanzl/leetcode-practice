"""
 * 给你一个正整数 n 。
 * 请你将 n 的值替换为 n 的 质因数 之和，重复这一过程。
 * 注意，如果 n 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。
 * 返回 n 可以取到的最小值。
 * 提示：2 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
"""


class Solution:

    def smallestValue(self, n: int) -> int:

        def func(x):
            # 分解质因数
            p = 2
            num = x
            p_map = {}
            while p * p <= num:
                if num % p == 0:
                    x = 0
                    while num % p == 0:
                        num //= p
                        x += 1
                    p_map[p] = p_map.get(p, 0) + x
                else:
                    p += 1
            if num > 1:
                p_map[num] = 1
            # =================================
            ret = 0
            for p, x in p_map.items():
                ret += p * x
            return ret

        ans = n
        while True:
            v = func(ans)
            if v == ans: break
            ans = v
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().smallestValue(15))
    # 3
    print(Solution().smallestValue(3))