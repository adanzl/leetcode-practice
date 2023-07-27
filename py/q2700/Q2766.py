"""
 * 给你一个下标从 0 开始的整数数组 nums ，表示一些石块的初始位置。再给你两个长度 相等 下标从 0 开始的整数数组 moveFrom 和 moveTo 。
 * 在 moveFrom.length 次操作内，你可以改变石块的位置。在第 i 次操作中，你将位置在 moveFrom[i] 的所有石块移到位置 moveTo[i] 。
 * 完成这些操作后，请你按升序返回所有 有 石块的位置。
 * 注意：
 * 1、如果一个位置至少有一个石块，我们称这个位置 有 石块。
 * 2、一个位置可能会有多个石块。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= moveFrom.length <= 10^5
 * 3、moveFrom.length == moveTo.length
 * 4、1 <= nums[i], moveFrom[i], moveTo[i] <= 10^9
 * 5、测试数据保证在进行第 i 步操作时，moveFrom[i] 处至少有一个石块。
 * 链接：https://leetcode.cn/problems/relocate-marbles/
"""
from typing import List


class Solution:

    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        s = set(nums)

        for f, t in zip(moveFrom, moveTo):
            if f in s:
                s.remove(f)
                s.add(t)
        return sorted(s)


if __name__ == '__main__':
    # [2,7,15]
    print(Solution().relocateMarbles([5, 7, 8, 15], [5, 7, 8, 9], [9, 15, 2, 7]))
    # [5,6,8,9]
    print(Solution().relocateMarbles([1, 6, 7, 8], moveFrom=[1, 7, 2], moveTo=[2, 9, 5]))
    # [2]
    print(Solution().relocateMarbles([1, 1, 3, 3], moveFrom=[1, 3], moveTo=[2, 2]))
