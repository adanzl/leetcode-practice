"""
 * 给你两个长度为 n 、下标从 0 开始的整数数组 nums1 和 nums2 ，另给你一个下标从 1 开始的二维数组 queries ，其中 queries[i] = [xi, yi] 。
 * 对于第 i 个查询，在所有满足 nums1[j] >= xi 且 nums2[j] >= yi 的下标 j (0 <= j < n) 中，
 * 找出 nums1[j] + nums2[j] 的 最大值 ，如果不存在满足条件的 j 则返回 -1 。
 * 返回数组 answer ，其中 answer[i] 是第 i 个查询的答案。
 * 提示：
 * 1、nums1.length == nums2.length 
 * 2、n == nums1.length 
 * 3、1 <= n <= 10^5
 * 4、1 <= nums1[i], nums2[i] <= 10^9 
 * 5、1 <= queries.length <= 10^5
 * 6、queries[i].length == 2
 * 7、xi == queries[i][1]
 * 8、yi == queries[i][2]
 * 9、1 <= xi, yi <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-sum-queries/
"""
import bisect
from typing import List


class Solution:

    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        nn = sorted([[n1, n2] for n1, n2 in zip(nums1, nums2)], reverse=True)  # 大->小
        n = len(queries)
        ans = [-1] * n
        qq = sorted([[q[0], q[1], i] for i, q in enumerate(queries)], reverse=True)  # 大->小
        ss = []  # 小->大
        i0, i1 = 0, 0
        for qx, qy, i in qq:
            while i0 < len(nn) and qx <= nn[i0][0]:  # 此处引入一个结论：如果y更大且sm更大，此时小的y就没用了， 单调栈应用
                y, sm = nn[i0][1], nn[i0][0] + nn[i0][1]
                while ss and ss[-1][0] <= y and ss[-1][1] <= sm:  # 新y,sm更大，删除旧的
                    ss.pop()
                if not ss or ss[-1][0] < y or ss[-1][1] < sm:  # 新y更大或者sm更大，插入
                    bisect.insort(ss, [y, sm])
                i0 += 1
            idx = bisect.bisect_left(ss, qy, key=lambda x: x[0])
            ans[i] = -1 if idx == len(ss) else ss[idx][1]
        return ans


if __name__ == '__main__':
    # [9,9,9]
    print(Solution().maximumSumQueries([3, 2, 5], nums2=[2, 3, 4], queries=[[4, 4], [3, 2], [1, 1]]))
    # [6,10,7]
    print(Solution().maximumSumQueries([4, 3, 1, 2], nums2=[2, 4, 9, 5], queries=[[4, 1], [1, 3], [2, 5]]))
    # [-1]
    print(Solution().maximumSumQueries([2, 1], nums2=[2, 3], queries=[[3, 3]]))
