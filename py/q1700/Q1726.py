"""
 * 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。
 * 其中 a、b、c 和 d 都是 nums 中的元素，且 a != b != c != d 。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 10^4
 * 3、nums 中的所有元素 互不相同
 * 链接：https://leetcode.cn/problems/tuple-with-same-product/
"""

from collections import Counter
from typing import List

#
# @lc app=leetcode.cn id=1726 lang=python3
#
# [1726] 同积元组
#


# @lc code=start
class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = Counter()
        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i - 1, -1, -1):
                ans += cnt[nums[i] * nums[j]] * 8
                cnt[nums[i] * nums[j]] += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 8
    print(Solution().tupleSameProduct([2, 3, 4, 6]))
    # 16
    print(Solution().tupleSameProduct([1, 2, 4, 5, 10]))