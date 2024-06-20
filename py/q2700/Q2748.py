"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 如果下标对 i、j 满足 0 ≤ i < j < nums.length ，如果 nums[i] 的 第一个数字 和 nums[j] 的 最后一个数字 互质 ，
 * 则认为 nums[i] 和 nums[j] 是一组 美丽下标对 。
 * 返回 nums 中 美丽下标对 的总数目。
 * 对于两个整数 x 和 y ，如果不存在大于 1 的整数可以整除它们，则认为 x 和 y 互质 。
 * 换而言之，如果 gcd(x, y) == 1 ，则认为 x 和 y 互质，其中 gcd(x, y) 是 x 和 y 的 最大公因数 。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、1 <= nums[i] <= 9999
 * 3、nums[i] % 10 != 0
 * 链接：https://leetcode.cn/problems/number-of-beautiful-pairs
"""

from math import gcd
from typing import List

#
# @lc app=leetcode.cn id=2748 lang=python3
#
# [2748] 美丽下标对的数目
#


# @lc code=start
class Solution:

    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            n1 = int(str(nums[i])[0])
            for j in range(i + 1, n):
                n2 = int(str(nums[j])[-1])
                if gcd(n1, n2) == 1:
                    ans += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 5
    print(Solution().countBeautifulPairs([2, 5, 1, 4]))
    # 5
    print(Solution().countBeautifulPairs([11, 21, 12]))
