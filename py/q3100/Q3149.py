"""
 * 给你一个数组 nums ，它是 [0, 1, 2, ..., n - 1] 的一个 排列 。
 * 对于任意一个 [0, 1, 2, ..., n - 1] 的排列 perm ，其 分数 定义为：
 * score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|
 * 返回具有 最低 分数的排列 perm 。如果存在多个满足题意且分数相等的排列，则返回其中
 * 字典序 最小 的一个。
 * 提示：
 * 1、2 <= n == nums.length <= 14
 * 2、nums 是 [0, 1, 2, ..., n - 1] 的一个排列。
 * 链接：https://leetcode.cn/problems/find-the-minimum-cost-array-permutation/
"""
import bisect
from functools import cache
from typing import List


class Solution:

    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # perm的旋转顺序不影响最终结果，所以最终结果perm[0] 一定 为0
        INF = 0x3c3c3c3c3c

        @cache
        def dfs(mark, idx, lst):
            if idx == n:
                return abs(lst - nums[0]), []
            ret_v, ret_p = INF, []
            for i in range(n):
                if mark & (1 << i): continue
                vv = abs(lst - nums[i])
                v, p = dfs(mark | (1 << i), idx + 1, i)
                v += vv
                if v < ret_v:
                    ret_p = [i] + p
                    ret_v = v
            return ret_v, ret_p

        ans_v, ans = dfs(1, 1, 0)
        return [0] + ans


if __name__ == '__main__':
    # [0,1,2]
    print(Solution().findPermutation([2, 1, 0]))
    # [0,2,1]
    print(Solution().findPermutation([0, 2, 1]))
    # [0,1,2]
    print(Solution().findPermutation([1, 0, 2]))
