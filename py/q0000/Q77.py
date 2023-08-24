"""
 * 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
 * 你可以按 任何顺序 返回答案。
 * 提示：
 * 1、1 <= n <= 20
 * 2、1 <= k <= n
 * 链接：https://leetcode.cn/problems/combinations/
"""
from itertools import combinations
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(l) for l in combinations([i for i in range(1, n + 1)], k)]


if __name__ == '__main__':
    # [[1]]
    print(Solution().combine(1, 1))
    # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(Solution().combine(4, 2))