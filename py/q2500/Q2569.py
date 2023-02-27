"""
 * 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
 * 1、操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成 0 。l 和 r 下标都从 0 开始。
 * 2、操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。
 * 3、操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
 * 请你返回一个数组，包含所有第三种操作类型的答案。
 * 提示：
 * 1、1 <= nums1.length,nums2.length <= 10^5
 * 2、nums1.length = nums2.length
 * 3、1 <= queries.length <= 10^5
 * 4、queries[i].length = 3
 * 5、0 <= l <= r <= nums1.length - 1
 * 6、0 <= p <= 10^6
 * 7、0 <= nums1[i] <= 1
 * 8、0 <= nums2[i] <= 10^9
 * 链接：https://leetcode.cn/problems/handling-sum-queries-after-update/
"""
from typing import List


class Solution:

    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(nums2)
        x = int(''.join(map(str, nums1[::-1])), 2)

        ans = []
        for op, l, r in queries:
            if op == 1:
                y = (1 << (r - l + 1)) - 1
                y <<= l
                x ^= y
            elif op == 2:
                s += l * x.bit_count()
            else:
                ans.append(s)
        return ans


if __name__ == '__main__':
    # [3]
    print(Solution().handleQuery([1, 0, 1], nums2=[0, 0, 0], queries=[[1, 1, 1], [2, 1, 0], [3, 0, 0]]))
    # [5]
    print(Solution().handleQuery([1], nums2=[5], queries=[[2, 0, 0], [3, 0, 0]]))
    #
    # print(Solution().handleQuery())