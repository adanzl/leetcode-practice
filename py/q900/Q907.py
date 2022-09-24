"""
 * 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
 * 由于答案可能很大，因此 返回答案模 10^9 + 7 。
 * 提示：
 * 1、1 <= arr.length <= 3 * 10^4
 * 2、1 <= arr[i] <= 3 * 10^4
 * 链接：https://leetcode.cn/problems/sum-of-subarray-minimums/
"""

from typing import *
from collections import *


class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        ans, n = 0, len(arr)
        q = deque()
        r = [0] * n
        for i in range(n - 1, -1, -1):
            while q and arr[i] < arr[q[-1]]:
                q.pop()
            r[i] = q[-1] if q else n
            q.append(i)
        q.clear()
        for i in range(n):
            while q and arr[i] <= arr[q[-1]]:
                q.pop()
            v = q[-1] if q else -1
            ans = (ans + arr[i] * (r[i] - i) * (i - v)) % MOD
            q.append(i)
        return ans


if __name__ == '__main__':
    # 21
    print(Solution().sumSubarrayMins([3, 1, 2, 1, 4]))
    # 17
    print(Solution().sumSubarrayMins([3, 1, 2, 4]))
    # 21
    print(Solution().sumSubarrayMins([3, 1, 2, 1, 4]))
    # 21
    print(Solution().sumSubarrayMins([3, 1, 2, 1, 4]))
    # 444
    print(Solution().sumSubarrayMins([11, 81, 94, 43, 3]))
