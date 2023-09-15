"""
 * 欢迎各位勇者来到力扣新手村，在开始试炼之前，请各位勇者先进行「宝石补给」。
 * 每位勇者初始都拥有一些能量宝石， gem[i] 表示第 i 位勇者的宝石数量。
 * 现在这些勇者们进行了一系列的赠送，operations[j] = [x, y] 表示在第 j 次的赠送中 第 x 位勇者将自己一半的宝石（需向下取整）赠送给第 y 位勇者。
 * 在完成所有的赠送后，请找到拥有最多宝石的勇者和拥有最少宝石的勇者，并返回他们二者的宝石数量之差。
 * 注意：赠送将按顺序逐步进行。
 * 提示：
 * 1、2 <= gem.length <= 10^3
 * 2、0 <= gem[i] <= 10^3
 * 3、0 <= operations.length <= 10^4
 * 4、operations[i].length == 2
 * 5、0 <= operations[i][0], operations[i][1] < gem.length
 * 链接：https://leetcode.cn/problems/WHnhjV
"""
from typing import List


class Solution:

    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            v = gem[x] // 2
            gem[y] += v
            gem[x] -= v
        return max(gem) - min(gem)


if __name__ == '__main__':
    # 2
    print(Solution().giveGem([3, 1, 2], operations=[[0, 2], [2, 1], [2, 0]]))
    # 75
    print(Solution().giveGem([100, 0, 50, 100], operations=[[0, 2], [0, 1], [3, 0], [3, 0]]))
    # 0
    print(Solution().giveGem([0, 0, 0, 0], operations=[[1, 2], [3, 1], [1, 2]]))
