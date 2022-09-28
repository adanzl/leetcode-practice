"""
 * 我们有一个非负整数数组 arr 。
 * 对于每个（连续的）子数组 sub = [arr[i], arr[i + 1], ..., arr[j]] （ i <= j），我们对 sub 中的每个元素进行按位或操作，获得结果 arr[i] | arr[i + 1] | ... | arr[j] 。
 * 返回可能结果的数量。 多次出现的结果在最终答案中仅计算一次。
 * 提示：
 * 1 <= nums.length <= 5 * 10^4
 * 0 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/bitwise-ors-of-subarrays/
"""

from typing import *


class Solution:

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all, line = set(), set()
        for v in arr:
            line = {num | v for num in line}
            line.add(v)
            all |= line
        return len(all)


if __name__ == '__main__':
    # 6
    print(Solution().subarrayBitwiseORs([1, 2, 4]))
    # 1
    print(Solution().subarrayBitwiseORs([0]))
    # 3
    print(Solution().subarrayBitwiseORs([1, 1, 2]))
