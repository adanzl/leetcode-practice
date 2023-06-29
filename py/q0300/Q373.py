"""
 * 给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
 * 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
 * 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
 * 提示:
 * 1、1 <= nums1.length, nums2.length <= 10^5
 * 2、-10^9 <= nums1[i], nums2[i] <= 10^9
 * 3、nums1 和 nums2 均为升序排列
 * 4、1 <= k <= 1000
 * 链接：https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [[nums1[i] + nums2[0], i, 0] for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, [nums1[i] + nums2[j + 1], i, j + 1])
        return ans


if __name__ == '__main__':
    # [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]
    print(Solution().kSmallestPairs([1, 1, 2], nums2=[1, 2, 3], k=10))
    # [1,3],[2,3]
    print(Solution().kSmallestPairs([1, 2], nums2=[3], k=3))
    # [1,2],[1,4],[1,6]
    print(Solution().kSmallestPairs([1, 7, 11], nums2=[2, 4, 6], k=3))
    # [1,1],[1,1]
    print(Solution().kSmallestPairs([1, 1, 2], nums2=[1, 2, 3], k=2))
