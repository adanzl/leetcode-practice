"""
 * 给你两个正整数：n 和 target 。
 * 如果数组 nums 满足下述条件，则称其为 美丽数组 。
 * 1、nums.length == n.
 * 2、nums 由两两互不相同的正整数组成。
 * 3、在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。
 * 返回符合条件的美丽数组所可能具备的 最小 和，并对结果进行取模 10^9 + 7。
 * 提示：
 * 1、1 <= n <= 10^9
 * 2、1 <= target <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/
"""


#
# @lc app=leetcode.cn id=2834 lang=python3
# @lc code=start
class Solution:

    def minimumPossibleSum(self, n: int, k: int) -> int:
        m = min(k // 2, n)
        return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2 % (10**9 + 7)


# @lc code=end

if __name__ == '__main__':
    # 156198582
    print(Solution().minimumPossibleSum(39636, 49035))
    # 4
    print(Solution().minimumPossibleSum(2, 3))
    # 8
    print(Solution().minimumPossibleSum(3, 3))
    # 1
    print(Solution().minimumPossibleSum(1, 1))
