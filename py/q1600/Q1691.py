"""
 * 给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [width_i, length_i, height_i]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。
 * 如果 width_i <= width_j 且 length_i <= length_j 且 height_i <= length_j ，你就可以将长方体 i 堆叠在长方体 j 上。
 * 你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。
 * 返回 堆叠长方体 cuboids 可以得到的 最大高度 。
 * 提示：
 * 1、n == cuboids.length
 * 2、1 <= n <= 100
 * 3、1 <= width_i, length_i, height_i <= 100
 * 链接：https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/
"""
from typing import List


class Solution:

    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cub in cuboids:
            cub.sort()
        cuboids.sort(key=lambda x: (x[2], x[1], x[0]))
        n = len(cuboids)
        dp = [0] * (n)
        for r in range(n):
            c = cuboids[r]
            dp[r] = c[2]
            for l in range(r):
                lc = cuboids[l]
                if c[0] >= lc[0] and c[1] >= lc[1] and c[2] >= lc[2]:
                    dp[r] = max(dp[r], dp[l] + c[2])
        return max(dp)


if __name__ == '__main__':
    # 435
    print(Solution().maxHeight([[29, 59, 36], [12, 13, 97], [49, 86, 43], [9, 57, 50], [97, 19, 10], [17, 92, 69], [92, 36, 15], [16, 63, 8], [94, 24, 78], [52, 11, 39], [48, 61, 57], [15, 44, 79],
                                [6, 69, 98], [30, 70, 41], [23, 17, 33], [85, 86, 12], [13, 75, 98], [75, 30, 30], [89, 18, 27], [94, 83, 81]]))
    # 190
    print(Solution().maxHeight([[50, 45, 20], [95, 37, 53], [45, 23, 12]]))
    # 76
    print(Solution().maxHeight([[38, 25, 45], [76, 35, 3]]))
    # 102
    print(Solution().maxHeight([[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]))
