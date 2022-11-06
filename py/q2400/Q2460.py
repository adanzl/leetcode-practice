"""
 * 给你一个下标从 0 开始的数组 nums ，数组大小为 n ，且由 非负 整数组成。
 * 你需要对数组执行 n - 1 步操作，其中第 i 步操作（从 0 开始计数）要求对 nums 中第 i 个元素执行下述指令：
 * 如果 nums[i] == nums[i + 1] ，则 nums[i] 的值变成原来的 2 倍，nums[i + 1] 的值变成 0 。否则，跳过这步操作。
 * 在执行完 全部 操作后，将所有 0 移动 到数组的 末尾 。
 * 例如，数组 [1,0,2,0,0,1] 将所有 0 移动到末尾后变为 [1,2,1,0,0,0] 。
 * 返回结果数组。
 * 注意 操作应当 依次有序 执行，而不是一次性全部执行。
 * 提示：
 * 1、2 <= nums.length <= 2000
 * 2、0 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/apply-operations-to-an-array/
"""
from typing import List


class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        ans = [num for num in nums if num]
        return ans + [0] * (n - len(ans))


if __name__ == '__main__':
    # [1,4,2,0,0,0]
    print(Solution().applyOperations([1, 2, 2, 1, 1, 0]))
