"""
 * Alice 有一个下标从 0 开始的数组 arr ，由 n 个正整数组成。
 * 她会选择一个任意的 正整数 k 并按下述方式创建两个下标从 0 开始的新整数数组 lower 和 higher ：
 * 1、对每个满足 0 <= i < n 的下标 i ，lower[i] = arr[i] - k
 * 2、对每个满足 0 <= i < n 的下标 i ，higher[i] = arr[i] + k
 * 不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 lower 和 higher 中出现的整数，但不知道每个整数属于哪个数组。
 * 请你帮助 Alice 还原原数组。
 * 给你一个由 2n 个整数组成的整数数组 nums ，其中 恰好 n 个整数出现在 lower ，剩下的出现在 higher ，还原并返回 原数组 arr 。
 * 如果出现答案不唯一的情况，返回 任一 有效数组。
 * 注意：生成的测试用例保证存在 至少一个 有效数组 arr 。
 * 提示：
 * 1、2 * n == nums.length
 * 2、1 <= n <= 1000
 * 3、1 <= nums[i] <= 10^9
 * 4、生成的测试用例保证存在 至少一个 有效数组 arr
 * 链接：https://leetcode.com/problems/recover-the-original-array/
"""

from typing import List, Deque

#
# @lc app=leetcode.cn id=2122 lang=python3
#
# [2122] 还原原数组
#


# @lc code=start
class Solution:

    def recoverArray(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(1, len(nums)):
            d = nums[i] - nums[0]
            if d & 1 or d == 0:
                continue
            lq = Deque(nums[:i])
            a = []
            for j in range(i, len(nums)):
                if lq and lq[0] + d == nums[j]:
                    a.append(lq[0] + d // 2)
                    lq.popleft()
                else:
                    lq.append(nums[j])
            if not lq:
                ans = a
                break
        return ans


# @lc code=end

if __name__ == '__main__':
    # [2,2]
    print(Solution().recoverArray([1, 1, 3, 3]))
    # [3,7,11]
    print(Solution().recoverArray([2, 10, 6, 4, 8, 12]))
    # [220]
    print(Solution().recoverArray([5, 435]))
