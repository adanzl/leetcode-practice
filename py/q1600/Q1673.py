"""
 * 给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。
 * 数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
 * 在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。 
 * 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、1 <= k <= nums.length
 * 链接：https://leetcode.cn/problems/find-the-most-competitive-subsequence/
"""
from typing import List


class Solution:

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        r = len(nums) - k
        for num in nums:
            while s and s[-1] > num and r:
                s.pop()
                r -= 1
            s.append(num)
        if r: s = s[:-r]
        return s


if __name__ == '__main__':
    # [8,80,2]
    print(Solution().mostCompetitive([71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], 3))
    # [2,6]
    print(Solution().mostCompetitive([3, 5, 2, 6], 2))
    # [2,3,3,4]
    print(Solution().mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
