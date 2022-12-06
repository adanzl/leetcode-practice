"""
 * 给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。
 * 统计并返回 num 中的 中位数 等于 k 的非空子数组的数目。
 * 注意：
 * 1、数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
 * 2、例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
 * 子数组是数组中的一个连续部分。
 * 提示：
 * 1、n == nums.length
 * 2.1 <= n <= 10^5
 * 3、1 <= nums[i], k <= n
 * 4、nums 中的整数互不相同
 * 链接：https://leetcode.cn/problems/count-subarrays-with-median-k/
"""
from typing import Counter, List


class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 大于 k 相当于 +1，小于 k 相当于 -1
        # 先遍历右侧，再处理左侧。处理左侧的时候，cnt_l 加上右侧的数量
        n = len(nums)
        pos = nums.index(k)
        cnt_r = Counter({0: 1})
        ans = 0
        c = 0
        for i in range(pos + 1, n):
            c += 1 if nums[i] > k else -1
            cnt_r[c] += 1
        ans += cnt_r[0] + cnt_r[1]  # 向右侧扩展的中位数，奇偶都考虑了
        c = 0
        for i in range(pos - 1, -1, -1):
            c += 1 if nums[i] < k else -1
            ans += cnt_r[c] + cnt_r[c + 1]
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().countSubarrays([2, 3, 1], 3))
    # 13
    print(Solution().countSubarrays([5, 19, 11, 15, 13, 16, 4, 6, 2, 7, 10, 8, 18, 20, 1, 3, 17, 9, 12, 14], 6))
    # 3
    print(Solution().countSubarrays([3, 2, 1, 4, 5], 4))
    # 3
    print(Solution().countSubarrays([2, 5, 1, 4, 3, 6], 1))
    # 1
    print(Solution().countSubarrays([10, 3, 8, 5, 6, 7, 2, 9, 4, 1], 9))
