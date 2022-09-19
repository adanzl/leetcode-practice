"""
 * 给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。
 * 用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。
 * 满足条件的二叉树一共有多少个？答案可能很大，返回 对 10^9 + 7 取余 的结果。
 * 提示：
 * 1 <= arr.length <= 1000
 * 2 <= arr[i] <= 10^9
 * arr 中的所有值 互不相同
"""

from collections import defaultdict
from typing import *


class Solution:

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        ans = 0
        MOD = int(1e9 + 7)
        dp = dict()
        arr.sort()
        for i, num in enumerate(arr):
            dp[num] = 1
            ans += 1
            for j in range(i):
                a, r = divmod(num, arr[j])
                if r == 0:
                    if a in arr:
                        d = dp.get(a) * dp.get(arr[j])
                        dp[num] += d
                        ans = (ans + d) % MOD
        return ans % MOD


if __name__ == '__main__':
    # 3
    print(Solution().numFactoredBinaryTrees([2, 4]))
    # 12
    print(Solution().numFactoredBinaryTrees([18, 3, 6, 2]))
    # 7
    print(Solution().numFactoredBinaryTrees([2, 4, 5, 10]))