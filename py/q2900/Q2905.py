"""
 * 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，以及整数 indexDifference 和整数 valueDifference 。
 * 你的任务是从范围 [0, n - 1] 内找出  2 个满足下述所有条件的下标 i 和 j ：
 * 1、abs(i - j) >= indexDifference 且
 * 2、abs(nums[i] - nums[j]) >= valueDifference
 * 返回整数数组 answer。如果存在满足题目要求的两个下标，则 answer = [i, j] 
 * 否则，answer = [-1, -1] 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。
 * 注意：i 和 j 可能 相等 。
 * 提示：
 * 1、1 <= n == nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= indexDifference <= 10^5
 * 4、0 <= valueDifference <= 10^9
 * 链接：https://leetcode.cn/problems/find-indices-with-index-and-value-difference-ii/
"""
import bisect
from typing import List


class Solution:

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ss = []
        for i, num in enumerate(nums):
            if i >= indexDifference:
                bisect.insort(ss, (nums[i - indexDifference], i - indexDifference))
                g_i = bisect.bisect_left(ss, num + valueDifference, key=lambda x: x[0])
                if g_i < len(ss):
                    return [ss[g_i][1], i]
                s_i = bisect.bisect_right(ss, num - valueDifference, key=lambda x: x[0])
                if s_i > 0:
                    return [ss[s_i - 1][1], i]
        return [-1, -1]


if __name__ == '__main__':
    # [0,2]
    print(Solution().findIndices([0, 4, 7, 2], 2, 7))
    # [0,1]
    print(Solution().findIndices([2, 7, 0], 0, 4))
    # [0,3]
    print(Solution().findIndices([5, 1, 4, 1], indexDifference=2, valueDifference=4))
    # [0,0]
    print(Solution().findIndices([2, 1], indexDifference=0, valueDifference=0))
    # [-1,-1]
    print(Solution().findIndices([1, 2, 3], indexDifference=2, valueDifference=4))
