"""
 * 给你一个整数数组 nums 。
 * 数组 nums 的 唯一性数组 是一个按元素从小到大排序的数组，包含了 nums 的所有 非空子数组中 不同元素的个数。
 * 换句话说，这是由所有 0 <= i <= j < nums.length 的 distinct(nums[i..j]) 组成的递增数组。
 * 其中，distinct(nums[i..j]) 表示从下标 i 到下标 j 的子数组中不同元素的数量。
 * 返回 nums 唯一性数组 的 中位数 。
 * 注意，数组的 中位数 定义为有序数组的中间元素。如果有两个中间元素，则取值较小的那个。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/
"""
from typing import Counter, List


class Solution:

    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        tot = ((n + 1) * n // 2 + 1) // 2
        l, r = 1, 2**30

        def check(ln):
            l, r = 0, 0
            ret, cnt = 0, Counter()
            while r < n:
                while r < n and (nums[r] in cnt or len(cnt) < ln):
                    ret += r - l + 1
                    cnt[nums[r]] += 1
                    r += 1
                while l < r and len(cnt) == ln:
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0:
                        del cnt[nums[l]]
                    l += 1
            return ret

        while l <= r:
            mid = (l + r) // 2
            val = check(mid)
            if val < tot:  # 查找大于tot的最小值
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    # 4
    print(Solution().medianOfUniquenessArray([91, 64, 76, 18, 61, 55, 46, 93, 65, 99]))
    # 1
    print(Solution().medianOfUniquenessArray([36, 36, 36, 36, 36, 36, 36, 36]))
    # 1
    print(Solution().medianOfUniquenessArray([46, 73, 46, 46, 46]))
    # 1
    print(Solution().medianOfUniquenessArray([1, 2, 3]))
    # 2
    print(Solution().medianOfUniquenessArray([4, 3, 5, 4]))
    # 2
    print(Solution().medianOfUniquenessArray([3, 4, 3, 4, 5]))
