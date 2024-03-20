"""
 * 给你一个大小为 m x n 、下标从 0 开始的二维矩阵 mat 。在每个单元格，你可以按以下方式生成数字：
 * 1、最多有 8 条路径可以选择：东，东南，南，西南，西，西北，北，东北。
 * 2、选择其中一条路径，沿着这个方向移动，并且将路径上的数字添加到正在形成的数字后面。
 * 3、注意，每一步都会生成数字，例如，如果路径上的数字是 1, 9, 1，那么在这个方向上会生成三个数字：1, 19, 191 。
 * 返回在遍历矩阵所创建的所有数字中，出现频率最高的、大于 10的 素数；如果不存在这样的素数，则返回 -1 。
 * 如果存在多个出现频率最高的素数，那么返回其中最大的那个。
 * 注意：移动过程中不允许改变方向。
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[i].length
 * 3、1 <= m, n <= 6
 * 4、1 <= mat[i][j] <= 9
 * 链接：https://leetcode.cn/problems/most-frequent-prime/description/
"""
from typing import Counter, List

LIMIT = 10**6 + 5
prime_list = []
b_composite = [False] * LIMIT
b_composite[1] = True  # 这里 1 被算为合数


def build_prime_list():
    # 线性筛选质数
    for i in range(2, LIMIT):
        if not b_composite[i]:
            prime_list.append(i)
        for prime in prime_list:
            nx = prime * i
            if nx < LIMIT:
                b_composite[nx] = True
            else:
                break


build_prime_list()


class Solution:

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        cnt = Counter()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                for dx, dy in [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, -1], [-1, 1], [-1, 0]]:
                    x, y = i, j
                    num = mat[i][j]
                    while True:
                        x += dx
                        y += dy
                        if x < 0 or y < 0 or x >= m or y >= n:
                            break
                        num = num * 10 + mat[x][y]
                        if num < 10 or b_composite[num]:
                            continue
                        cnt[num] += 1
        ss = sorted([[v, k] for k, v in cnt.items()], reverse=True)
        if len(ss) == 0: return -1
        return ss[0][1]


if __name__ == '__main__':
    # 19
    print(Solution().mostFrequentPrime([[1, 1], [9, 9], [1, 1]]))
    # -1
    print(Solution().mostFrequentPrime([[7]]))
    # 97
    print(Solution().mostFrequentPrime([[9, 7, 8], [4, 6, 5], [2, 8, 6]]))
