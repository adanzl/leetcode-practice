"""
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都是 n ，再给你一个正整数 k 。你必须从 nums1 中选一个长度为 k 的 子序列 对应的下标。
 * 对于选择的下标 i0 ，i1 ，...， ik - 1 ，你的 分数 定义如下：
 * 1、nums1 中下标对应元素求和，乘以 nums2 中下标对应元素的 最小值 。
 * 2、用公示表示： (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]) 。
 * 请你返回 最大 可能的分数。
 * 一个数组的 子序列 下标是集合 {0, 1, ..., n-1} 中删除若干元素得到的剩余集合，也可以不删除任何元素。
 * 提示：
 * n == nums1.length == nums2.length
 * 1 <= n <= 10^5
 * 0 <= nums1[i], nums2[j] <= 10^5
 * 1 <= k <= n
 * 链接：https://leetcode.cn/problems/maximum-subsequence-score/
"""
from heapq import heapify, heapreplace
from typing import List


class Solution:

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = sorted(list(zip(nums1, nums2)), key=lambda x: (x[1], x[0]))
        n = len(arr)
        h_suf = [arr[i][0] for i in range(n - k, n)]
        heapify(h_suf)
        sm = sum(h_suf)
        ans = sm * arr[n - k][1]
        for i in range(n - k - 1, -1, -1):
            if h_suf[0] < arr[i][0]:
                sm = sm - h_suf[0] + arr[i][0]
                heapreplace(h_suf, arr[i][0])
            ans = max(ans, arr[i][1] * sm)
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().maxScore([1, 4], [3, 1], 2))
    # 168
    print(Solution().maxScore([2, 1, 14, 12], [11, 7, 13, 6], 3))
    # 12
    print(Solution().maxScore([1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3))
    # 30
    print(Solution().maxScore([4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1))
