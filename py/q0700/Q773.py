"""
 * 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。
 * 一次 移动 定义为选择 0 与一个相邻的数字（上下左右）进行交换.
 * 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
 * 给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
 * 提示：
 * 1、board.length == 2
 * 2、board[i].length == 3
 * 3、0 <= board[i][j] <= 5
 * 4、board[i][j] 中每个值都 不同
 * 链接：https://leetcode.cn/problems/sliding-puzzle/
"""

from typing import List

#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start

m, n = 2, 3
steps = {'123450': 0}
q = ['123450']
while q:
    state = q.pop(0)
    zx, zy = divmod(state.index('0'), n)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = zx + dx, zy + dy
        if x < 0 or x >= m or y < 0 or y >= n: continue
        sf = list(state)
        sf[zx * n + zy], sf[x * n + y] = sf[x * n + y], sf[zx * n + zy]
        nf = ''.join(sf)
        if nf in steps: continue
        steps[nf] = steps[state] + 1
        q.append(nf)


class Solution:

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        return steps.get(''.join([str(board[i][j]) for i in range(m) for j in range(n)]), -1)


# @lc code=end

if __name__ == '__main__':
    # 5
    print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
    # 14
    print(Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
    # 1
    print(Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
    # -1
    print(Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
