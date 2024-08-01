"""
 * 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，
 * 若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。 
 * 给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 
 * 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。
 * 提示：
 * 1、1 <= cnt <= cards.length <= 10^5
 * 2、1 <= cards[i] <= 1000
 * 链接：https://leetcode.cn/problems/uOAnQW
"""
from typing import List


class Solution:

    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        ans = 0
        odd, even = [], []
        for card in cards:
            if card & 1: odd.append(card)
            else: even.append(card)
        odd.sort(reverse=True)
        even.sort(reverse=True)
        i_o, i_e = 0, 0
        if cnt & 1 and i_e < len(even):
            ans += even[i_e]
            i_e += 1
            cnt -= 1
        while cnt >= 2 and len(odd) - i_o >= 2 and len(even) - i_e >= 2:
            if odd[i_o] + odd[i_o + 1] >= even[i_e] + even[i_e + 1]:
                ans += odd[i_o] + odd[i_o + 1]
                i_o += 2
            else:
                ans += even[i_e] + even[i_e + 1]
                i_e += 2
            cnt -= 2
        while cnt >= 2 and len(odd) - i_o >= 2:
            ans += odd[i_o] + odd[i_o + 1]
            i_o += 2
            cnt -= 2
        while cnt and len(even) - i_e:
            ans += even[i_e]
            i_e += 1
            cnt -= 1
        return ans if cnt == 0 else 0


if __name__ == '__main__':
    # 28
    print(Solution().maxmiumScore([7, 1, 5, 8, 3, 3, 1, 2], 7))
    # 18
    print(Solution().maxmiumScore([1, 2, 8, 9], cnt=3))
    # 0
    print(Solution().maxmiumScore([1, 3, 4, 5], cnt=4))
    # 0
    print(Solution().maxmiumScore([3, 3, 1], cnt=1))
