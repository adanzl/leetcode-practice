"""
 * 在桌子上有 n 张卡片，每张卡片的正面和背面都写着一个正数（正面与背面上的数有可能不一样）。
 * 我们可以先翻转任意张卡片，然后选择其中一张卡片。
 * 如果选中的那张卡片背面的数字 x 与任意一张卡片的正面的数字都不同，那么这个数字是我们想要的数字。
 * 哪个数是这些想要的数字中最小的数（找到这些数中的最小值）呢？如果没有一个数字符合要求的，输出 0 。
 * 其中, fronts[i] 和 backs[i] 分别代表第 i 张卡片的正面和背面的数字。
 * 如果我们通过翻转卡片来交换正面与背面上的数，那么当初在正面的数就变成背面的数，背面的数就变成正面的数。
 * 提示：
 * 1、n == fronts.length == backs.length
 * 2、1 <= n <= 1000
 * 3、1 <= fronts[i], backs[i] <= 2000
 * 链接：https://leetcode.cn/problems/card-flipping-game/
"""
from typing import List


class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        LIMIT = 2001
        ans = LIMIT
        ss = set([f for f, b in zip(fronts, backs) if f == b])
        for f, b in zip(fronts, backs):
            if f == b:
                continue
            if f not in ss:
                ans = min(ans, f)
            if b not in ss:
                ans = min(ans, b)
        return ans if ans < LIMIT else 0


if __name__ == '__main__':
    # 2
    print(Solution().flipgame([1, 2, 4, 4, 7], backs=[1, 3, 4, 1, 3]))
    # 0
    print(Solution().flipgame([1], backs=[1]))
