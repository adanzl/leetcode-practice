"""
 * 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
 * 如果存在，返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 3、0 <= k <= 10^5
 * 链接：https://leetcode-cn.com/problems/contains-duplicate-ii
"""
from typing import Counter, List


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = Counter()
        for i, num in enumerate(nums):
            if i > k: c[nums[i - k - 1]] -= 1
            if c[num] > 0: return True
            c[num] += 1
        return False


if __name__ == '__main__':
    # True
    print(Solution().containsNearbyDuplicate([99, 99], 2))
    # False
    print(Solution().containsNearbyDuplicate([1, 2, 1], 1))
    # True
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    # True
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    # True
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
    # False
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
