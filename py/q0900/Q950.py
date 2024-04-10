"""
 * 牌组中的每张卡牌都对应有一个唯一的整数。你可以按你想要的顺序对这套卡片进行排序。
 * 最初，这些卡牌在牌组里是正面朝下的（即，未显示状态）。
 * 现在，重复执行以下步骤，直到显示所有卡牌为止：
 * 1、从牌组顶部抽一张牌，显示它，然后将其从牌组中移出。
 * 2、如果牌组中仍有牌，则将下一张处于牌组顶部的牌放在牌组的底部。
 * 3、如果仍有未显示的牌，那么返回步骤 1。否则，停止行动。
 * 返回能以递增顺序显示卡牌的牌组顺序。
 * 答案中的第一张牌被认为处于牌堆顶部。
 * 提示：
 * 1、1 <= A.length <= 1000
 * 2、1 <= A[i] <= 10^6
 * 3、对于所有的 i != j，A[i] != A[j]
 * 链接：https://leetcode.cn/problems/reveal-cards-in-increasing-order
"""

from typing import Deque, List

#
# @lc app=leetcode.cn id=950 lang=python3
#
# [950] 按递增顺序显示卡牌
#


# @lc code=start
class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        ans = [0] * n
        q = Deque([i for i in range(n)])
        ii = 0
        while q:
            ans[q.popleft()] = deck[ii]
            ii += 1
            if q:
                q.append(q.popleft())
        return ans


# @lc code=end

if __name__ == '__main__':
    # [2,13,3,11,5,17,7]
    print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
    # [1,1000]
    print(Solution().deckRevealedIncreasing([1, 1000]))
