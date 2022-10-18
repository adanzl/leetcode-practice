"""
 * 给你一个由 正 整数组成的数组 nums 。
 * 你必须取出数组中的每个整数，反转其中每个数位，并将反转后得到的数字添加到数组的末尾。这一操作只针对 nums 中原有的整数执行。
 * 返回结果数组中 不同 整数的数目。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/count-number-of-distinct-integers-after-reverse-operations/
"""
from typing import List


class Solution:

    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        for num in nums:
            s.add(int(str(num)[::-1]))
        return len(s)


if __name__ == '__main__':
    # 6
    print(Solution().countDistinctIntegers([1, 13, 10, 12, 31]))
    # 1
    print(Solution().countDistinctIntegers([2, 2, 2]))
