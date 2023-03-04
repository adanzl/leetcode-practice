"""
 * 给你一个整数数组 nums ，返回其中 按位与三元组 的数目。
 * 按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：
 * 1、0 <= i < nums.length
 * 2、0 <= j < nums.length
 * 3、0 <= k < nums.length
 * 4、nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、0 <= nums[i] < 2^16
 * 链接：https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/
"""
from collections import Counter
from typing import List


class Solution:

    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter(x & y for x in nums for y in nums)
        return sum(c for x, c in cnt.items() for y in nums if x & y == 0)


if __name__ == '__main__':
    # 12
    print(Solution().countTriplets([2, 1, 3]))
    # 27
    print(Solution().countTriplets([0, 0, 0]))
