"""
 * 给你一个下标从 1 开始、长度为 n 的整数数组 nums 。
 * 现定义函数 greaterCount ，使得 greaterCount(arr, val) 返回数组 arr 中 严格大于 val 的元素数量。
 * 你需要使用 n 次操作，将 nums 的所有元素分配到两个数组 arr1 和 arr2 中。在第一次操作中，将 nums[1] 追加到 arr1 。
 * 在第二次操作中，将 nums[2] 追加到 arr2 。之后，在第 i 次操作中：
 * 1、如果 greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr1 。
 * 2、如果 greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr2 。
 * 3、如果 greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]) ，将 nums[i] 追加到元素数量较少的数组中。
 * 4、如果仍然相等，那么将 nums[i] 追加到 arr1 。
 * 连接数组 arr1 和 arr2 形成数组 result 。例如，如果 arr1 == [1,2,3] 且 arr2 == [4,5,6] ，那么 result = [1,2,3,4,5,6] 。
 * 返回整数数组 result 。
 * 提示：
 * 1、3 <= n <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/
"""
import bisect
from typing import List


class Solution:

    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]]
        s1, s2 = [nums[0]], [nums[1]]
        for i in range(2, n):
            i0, i1 = bisect.bisect_right(s1, nums[i]), bisect.bisect_right(s2, nums[i])
            v = len(arr1) - i0 - len(arr2) + i1
            if v > 0:
                arr1.append(nums[i])
                bisect.insort(s1, nums[i])
            elif v < 0:
                arr2.append(nums[i])
                bisect.insort(s2, nums[i])
            else:
                if len(arr2) < len(arr1):
                    arr2.append(nums[i])
                    bisect.insort(s2, nums[i])
                else:
                    arr1.append(nums[i])
                    bisect.insort(s1, nums[i])
        return arr1 + arr2


if __name__ == '__main__':
    # [5,3,1,2,14]
    print(Solution().resultArray([5, 14, 3, 1, 2]))
    # [2,3,1,3]
    print(Solution().resultArray([2, 1, 3, 3]))
    # [3,3,3,3]
    print(Solution().resultArray([3, 3, 3, 3]))
