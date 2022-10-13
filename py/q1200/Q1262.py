"""
 * 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
 * 提示：
 * 1、1 <= nums.length <= 4 * 10^4
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/greatest-sum-divisible-by-three/
"""
from typing import List


class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        r = [0, 0, 0]
        for num in nums:
            nr = r.copy()
            nr[num % 3] = max(nr[num % 3], r[0] + num)
            if r[1]: nr[(num + 1) % 3] = max(r[1] + num, nr[(num + 1) % 3])
            if r[2]: nr[(num + 2) % 3] = max(r[2] + num, nr[(num + 2) % 3])
            r = nr
        return r[0]


if __name__ == '__main__':
    # 18
    print(Solution().maxSumDivThree([3, 6, 5, 1, 8]))
    # 0
    print(Solution().maxSumDivThree([4]))
    # 12
    print(Solution().maxSumDivThree([1, 2, 3, 4, 4]))
