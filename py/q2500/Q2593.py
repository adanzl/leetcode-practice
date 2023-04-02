"""
 * 给你一个数组 nums ，它包含若干正整数。
 * 一开始分数 score = 0 ，请你按照下面算法求出最后分数：
 * 1、从数组中选择最小且没有被标记的整数。如果有相等元素，选择下标最小的一个。
 * 2、将选中的整数加到 score 中。
 * 3、标记 被选中元素，如果有相邻元素，则同时标记 与它相邻的两个元素 。
 * 4、重复此过程直到数组中所有元素都被标记。
 * 请你返回执行上述算法后最后的分数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/find-score-of-an-array-after-marking-all-elements/
"""
from heapq import heapify, heappop
from typing import List


class Solution:

    def findScore(self, nums: List[int]) -> int:
        h = [[num, i] for i, num in enumerate(nums)]
        heapify(h)
        ans = 0
        idx_set = set()
        while h:
            num, i = heappop(h)
            if i in idx_set: continue
            ans += num
            idx_set.add(i)
            idx_set.add(i + 1)
            idx_set.add(i - 1)
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().findScore([2, 1, 3, 4, 5, 2]))
    # 5
    print(Solution().findScore([2, 3, 5, 1, 3, 2]))
