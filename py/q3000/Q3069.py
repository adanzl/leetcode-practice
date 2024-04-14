"""
 * 给你一个下标从 1 开始、包含 不同 整数的数组 nums ，数组长度为 n 。
 * 你需要通过 n 次操作，将 nums 中的所有元素分配到两个数组 arr1 和 arr2 中。
 * 在第一次操作中，将 nums[1] 追加到 arr1 。在第二次操作中，将 nums[2] 追加到 arr2 。
 * 之后，在第 i 次操作中：
 * 如果 arr1 的最后一个元素 大于 arr2 的最后一个元素，就将 nums[i] 追加到 arr1 。否则，将 nums[i] 追加到 arr2 。
 * 通过连接数组 arr1 和 arr2 形成数组 result 。
 * 例如，如果 arr1 == [1,2,3] 且 arr2 == [4,5,6] ，那么 result = [1,2,3,4,5,6] 。
 * 返回数组 result 。
 * 提示：
 * 1、3 <= n <= 50
 * 2、1 <= nums[i] <= 100
 * 3、nums中的所有元素都互不相同。
 * 链接：https://leetcode.cn/problems/distribute-elements-into-two-arrays-i/
"""
from typing import List


class Solution:

    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2


if __name__ == '__main__':
    # [2,3,1]
    print(Solution().resultArray([2, 1, 3]))
    # [5,3,4,8]
    print(Solution().resultArray([5, 4, 3, 8]))
