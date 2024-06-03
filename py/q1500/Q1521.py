"""
 * Winston 构造了一个如上所示的函数 func 。
 * 他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r) - target| 最小的 l 和 r 。
 * 请你返回 |func(arr, l, r) - target| 的最小值。
 * 请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、1 <= arr[i] <= 10^6
 * 3、0 <= target <= 10^7
 * 链接：https://leetcode.cn/problems/find-a-value-of-a-mysterious-function-closest-to-target/
"""

from typing import List

#
# @lc app=leetcode.cn id=1521 lang=python3
#
# [1521] 找到最接近目标值的函数值
#

# @lc code=start


class Solution:

    def closestToTarget(self, arr: List[int], target: int) -> int:
        val_set = {}
        ans = 0x3c3c3c3c3c
        for v in arr:
            val_set = {vv & v for vv in val_set} | {v}
            ans = min(ans, min([abs(target - vv) for vv in val_set]))
        return ans


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().closestToTarget([9, 12, 3, 7, 15], target=5))
    # 999999
    print(Solution().closestToTarget([1000000, 1000000, 1000000], target=1))
    # 0
    print(Solution().closestToTarget([1, 2, 4, 8, 16], target=0))
