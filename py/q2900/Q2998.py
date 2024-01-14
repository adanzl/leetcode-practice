"""
 * 给你两个正整数 x 和 y 。
 * 一次操作中，你可以执行以下四种操作之一：
 * 1、如果 x 是 11 的倍数，将 x 除以 11 。
 * 2、如果 x 是 5 的倍数，将 x 除以 5 。
 * 3、将 x 减 1 。
 * 4、将 x 加 1 。
 * 请你返回让 x 和 y 相等的 最少 操作次数。
 * 提示：1 <= x, y <= 10^4
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-x-and-y-equal/
"""
from typing import Deque


class Solution:

    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        LIMIT = 0x3c3c3c3c3c3c
        N = max(x, y) + 10000
        ans = [LIMIT] * N
        ans[y] = 0
        q = Deque([y])
        while q:
            num = q.popleft()
            for nv in [num * 11, num * 5, num + 1, num - 1]:
                if nv >= N: continue
                if nv < 0: continue
                if ans[nv] != LIMIT: continue
                ans[nv] = ans[num] + 1
                q.append(nv)

        return ans[x]


if __name__ == '__main__':
    # 1766
    print(Solution().minimumOperationsToMakeEqual(2203, 3969))
    # 3
    print(Solution().minimumOperationsToMakeEqual(26, y=1))
    # 4
    print(Solution().minimumOperationsToMakeEqual(54, y=2))
    # 5
    print(Solution().minimumOperationsToMakeEqual(25, y=30))
