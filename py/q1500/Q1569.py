"""
 * 给你一个数组 nums 表示 1 到 n 的一个排列。我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉查找树（BST）。
 * 请你统计将 nums 重新排序后，统计满足如下条件的方案数：重排后得到的二叉查找树与 nums 原本数字顺序得到的二叉查找树相同。
 * 比方说，给你 nums = [2,1,3]，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。数组 [2,3,1] 也能得到相同的 BST，但 [3,2,1] 会得到一棵不同的 BST 。
 * 请你返回重排 nums 后，与原数组 nums 得到相同二叉查找树的方案数。
 * 由于答案可能会很大，请将结果对 10^9 + 7 取余数。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= nums.length
 * 3、nums 中所有数 互不相同 。
 * 链接：https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/
"""
from collections import defaultdict
from functools import cache
from math import comb
from typing import List


class Solution:

    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        g = defaultdict(lambda: [-1, -1])
        cnt = defaultdict(lambda: [0, 0])
        for i in range(1, n):
            v, p = nums[0], g[nums[0]]
            while True:
                flag = 0 if nums[i] < v else 1
                cnt[v][flag] += 1
                if p[flag] == -1:
                    p[flag] = nums[i]
                    break
                else:
                    v = p[flag]
                    p = g[v]

        calc = lambda a, b: comb(a + b - 1, b - 1)  # a个有序元素插b个空格 <=> b个元素可重复的插入a+1个空格中

        @cache
        def f(num):
            if num == -1 or sum(cnt[num]) == 1 or not cnt[num]: return 1
            lv, rv = f(g[num][0]), f(g[num][1])
            v = lv * rv * calc(cnt[num][0], cnt[num][1] + 1) % MOD
            return v

        return f(nums[0]) - 1


if __name__ == '__main__':
    # 5
    print(Solution().numOfWays([3, 4, 5, 1, 2]))
    # 1
    print(Solution().numOfWays([2, 1, 3]))
    # 19
    print(Solution().numOfWays([3, 1, 2, 5, 4, 6]))
    # 216212978
    print(Solution().numOfWays([9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]))
