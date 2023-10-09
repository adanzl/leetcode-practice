"""
 * 给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。
 * 请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。
 * 如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。
 * 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[i].length
 * 3、2 <= n, m <= 100
 * 4、1 <= k <= m
 * 5、matrix[i][j] 不是 0 就是 1
 * 链接：https://leetcode.cn/problems/the-k-weakest-rows-in-a-matrix
"""
from typing import List


#
# @lc app=leetcode.cn id=1337 lang=python3
# @lc code=start
class Solution:

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [l[1] for l in sorted([[sum(line), i] for i, line in enumerate(mat)])[:k]]


# @lc code=end

if __name__ == '__main__':
    # [2,0,3]
    print(Solution().kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], k=3))
    # [0,2]
    print(Solution().kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], k=2))