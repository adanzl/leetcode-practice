"""
 * 给你一个数组 nums ，数组中只包含非负整数。定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。
 * 比方说 rev(123) = 321 ， rev(120) = 21 。我们称满足下面条件的下标对 (i, j) 是 好的 ：
 * 1、0 <= i < j < nums.length
 * 2、nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
 * 请你返回好下标对的数目。由于结果可能会很大，请将结果对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/count-nice-pairs-in-an-array/
"""
from typing import Counter, List


class Solution:

    def countNicePairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        MOD = 10**9 + 7
        for num in nums:
            rev = 0
            nn = num
            while num:
                rev *= 10
                rev += num % 10
                num //= 10
            d = nn - rev
            ans += cnt[d]
            cnt[d] += 1
        return ans % MOD


if __name__ == '__main__':
    # 2
    print(Solution().countNicePairs([42, 11, 1, 97]))
    # 4
    print(Solution().countNicePairs([13, 10, 35, 24, 76]))
