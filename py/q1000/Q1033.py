"""
 * 三枚石子放置在数轴上，位置分别为 a，b，c。
 * 每一回合，你可以从两端之一拿起一枚石子（位置最大或最小），并将其放入两端之间的任一空闲位置。
 * 形式上，假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。
 * 那么就可以从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。
 * 当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
 * 要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 
 * 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
 * 提示：
 * 1、1 <= a <= 100
 * 2、1 <= b <= 100
 * 3、1 <= c <= 100
 * 4、a != b, b != c, c != a
 * 链接：https://leetcode.cn/problems/moving-stones-until-consecutive/
"""
from typing import List


class Solution:

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        mn = 2
        if c - a == 2: mn = 0
        elif c - b == 2 or b - a == 2: mn = 1
        elif c - b == 1 or b - a == 1: mn = 1
        return [mn, c - a - 2]


if __name__ == '__main__':
    # [1, 2]
    print(Solution().numMovesStones(1, b=2, c=5))
    # [0, 0]
    print(Solution().numMovesStones(4, b=3, c=2))
