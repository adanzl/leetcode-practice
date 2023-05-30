"""
 * 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
 * 你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。
 * 提示：
 * 1、m == mat.length
 * 2、n == mat.length[i]
 * 3、1 <= m, n <= 40
 * 4、1 <= k <= min(200, n ^ m)
 * 5、1 <= mat[i][j] <= 5000
 * 6、mat[i] 是一个非递减数组
 * 链接：https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
"""
from functools import cache
from heapq import heappush, heapreplace
from typing import List


class Solution:

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        l, r = 0, 0
        m, n = len(mat), len(mat[0])
        for line in mat:
            l += line[0]
            r += line[-1]

        @cache
        def count(target, row):
            if row == m: return 1
            cnt = 0
            for i in range(n):
                if mat[row][i] > target: break
                cnt += count(target - mat[row][i], row + 1)
                if cnt > k:  # 剪枝，没有这个会超时
                    break
            return cnt

        ans = 0
        while l <= r:
            mid = (l + r) // 2
            cnt = count(mid, 0)
            if cnt >= k:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans

    def kthSmallest1(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        h = [0]
        for i in range(m):
            hh = []
            for j in range(n):
                for v in h:
                    vv = v - mat[i][j]
                    if len(hh) >= k:
                        if hh[0] < vv:
                            heapreplace(hh, vv)
                    else:
                        heappush(hh, vv)
            h = hh
        return -h[0]


if __name__ == '__main__':
    # 7
    print(Solution().kthSmallest([[1, 3, 11], [2, 4, 6]], k=5))
    # 17
    print(Solution().kthSmallest([[1, 3, 11], [2, 4, 6]], k=9))
    # 9
    print(Solution().kthSmallest([[1, 10, 10], [1, 4, 5], [2, 3, 6]], k=7))
    # 12
    print(Solution().kthSmallest([[1, 1, 10], [2, 2, 9]], k=7))
