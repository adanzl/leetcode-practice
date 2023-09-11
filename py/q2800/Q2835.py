"""
 * 给你一个下标从 0 开始的数组 nums ，它包含 非负 整数，且全部为 2 的幂，同时给你一个整数 target 。
 * 一次操作中，你必须对数组做以下修改：
 * 1、选择数组中一个元素 nums[i] ，满足 nums[i] > 1 。
 * 2、将 nums[i] 从数组中删除。
 * 3、在 nums 的 末尾 添加 两个 数，值都为 nums[i] / 2 。
 * 你的目标是让 nums 的一个 子序列 的元素和等于 target ，请你返回达成这一目标的 最少操作次数 。如果无法得到这样的子序列，请你返回 -1 。
 * 数组中一个 子序列 是通过删除原数组中一些元素，并且不改变剩余元素顺序得到的剩余数组。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 2^30
 * 3、nums 只包含非负整数，且均为 2 的幂。
 * 4、1 <= target < 2^31
 * 链接：https://leetcode.cn/problems/minimum-operations-to-form-subsequence-with-target-sum/
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:

    def minOperations(self, nums: List[int], target: int) -> int:
        h = [num.bit_length() - 1 for num in nums]
        heapify(h)
        ans = 0
        pre = -1
        for i in range(target.bit_length()):
            if target & (1 << i):
                if not h:
                    return -1
                while h:
                    v = heappop(h)
                    if v >= i:
                        ans += v - i
                        for j in range(i + 1, v):
                            heappush(h, j)
                        break
                    else:
                        if v == pre:
                            heappush(h, v + 1)
                            pre = -1
                        else:
                            pre = v
                else:
                    return -1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minOperations([1, 32, 1, 2], target=12))
    # -1
    print(Solution().minOperations([1, 32, 1], target=35))
    # 1
    print(Solution().minOperations([1, 2, 8], target=7))
