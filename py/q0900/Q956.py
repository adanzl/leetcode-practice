"""
 * 你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。
 * 你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。
 * 返回 广告牌的最大可能安装高度 。如果没法安装广告牌，请返回 0 。
 * 提示：
 * 1、0 <= rods.length <= 20
 * 2、1 <= rods[i] <= 1000
 * 3、sum(rods[i]) <= 5000
 * 链接：https://leetcode.cn/problems/tallest-billboard/
"""
from collections import defaultdict
from typing import List


class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dic = defaultdict(int, {0: 0})
        for rod in rods:
            nd = dic.copy()
            for k, v in dic.items():
                nd[k - rod] = max(nd[k - rod], v)
                nd[k + rod] = max(nd[k + rod], v + rod)
            dic = nd
        return dic[0]


if __name__ == '__main__':
    # 6
    print(Solution().tallestBillboard([1, 2, 3, 6]))
    # 10
    print(Solution().tallestBillboard([1, 2, 3, 4, 5, 6]))
    # 0
    print(Solution().tallestBillboard([1, 2]))
