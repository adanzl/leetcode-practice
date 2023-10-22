"""
 * 给你一个长度为 n 下标从 0 开始的整数数组 nums 。
 * 我们想将下标进行分组，使得 [0, n - 1] 内所有下标 i 都 恰好 被分到其中一组。
 * 如果以下条件成立，我们说这个分组方案是合法的：
 * 1、对于每个组 g ，同一组内所有下标在 nums 中对应的数值都相等。
 * 2、对于任意两个组 g1 和 g2 ，两个组中 下标数量 的 差值不超过 1 。
 * 请你返回一个整数，表示得到一个合法分组方案的 最少 组数。
 * 提示：
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-number-of-groups-to-create-a-valid-assignment/
"""
from collections import Counter
from typing import List


class Solution:

    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for g_len in range(min(cnt.values()) + 1, 0, -1):
            ans, valid = 0, True
            for ln in cnt.values():
                a, re = divmod(ln, g_len)
                if re != 0 and g_len - re > a + 1:
                    valid = False
                    break
                if re: a += 1
                ans += a
            if valid: return ans
        return len(nums)


if __name__ == '__main__':
    # 4
    print(Solution().minGroupsForValidAssignment([10, 10, 10, 3, 1, 1]))
    # 2
    print(Solution().minGroupsForValidAssignment([2, 3, 3, 3, 2, 3, 2, 3, 2]))
    # 5
    print(Solution().minGroupsForValidAssignment([1, 1, 3, 3, 1, 1, 2, 2, 3, 1, 3, 2]))
    # 2
    print(Solution().minGroupsForValidAssignment([3, 2, 3, 2, 3]))
