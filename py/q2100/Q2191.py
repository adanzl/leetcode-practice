"""
 * 给你一个下标从 0 开始的整数数组 mapping ，它表示一个十进制数的映射规则，mapping[i] = j 表示这个规则下将数位 i 映射为数位 j 。
 * 一个整数 映射后的值 为将原数字每一个数位 i （0 <= i <= 9）映射为 mapping[i] 。
 * 另外给你一个整数数组 nums ，请你将数组 nums 中每个数按照它们映射后对应数字非递减顺序排序后返回。
 * 注意：
 * 1、如果两个数字映射后对应的数字大小相同，则将它们按照输入中的 相对顺序 排序。
 * 2、nums 中的元素只有在排序的时候需要按照映射后的值进行比较，返回的值应该是输入的元素本身。
 * 提示：
 * 1、mapping.length == 10
 * 2、0 <= mapping[i] <= 9
 * 3、mapping[i] 的值 互不相同 。
 * 4、1 <= nums.length <= 3 * 10^4
 * 5、0 <= nums[i] < 10^9
 * 链接：https://leetcode.cn/problems/sort-the-jumbled-numbers
"""

from typing import List

#
# @lc app=leetcode.cn id=2191 lang=python3
#
# [2191] 将杂乱无章的数字排序
#


# @lc code=start
class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def get_val(num):
            ret, i = 0, 0
            if num == 0:
                ret = mapping[0]
            while num:
                ret += mapping[num % 10] * (10**i)
                num //= 10
                i += 1
            return ret

        return [v[2] for v in sorted([[get_val(num), i, num] for i, num in enumerate(nums)])]


# @lc code=end

if __name__ == '__main__':
    # [99,7686,2212638,97012948,84234023]
    print(Solution().sortJumbled([5, 6, 8, 7, 4, 0, 3, 1, 9, 2], [7686, 97012948, 84234023, 2212638, 99]))
    # [338,38,991]
    print(Solution().sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]))
    # [123,456,789]
    print(Solution().sortJumbled([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums=[789, 456, 123]))
