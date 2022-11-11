"""
 * 二指输入法定制键盘在 X-Y 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处。
 * 例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。
 * 给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。
 * 坐标 (x1,y1) 和 (x2,y2) 之间的 距离 是 |x1 - x2| + |y1 - y2|。 
 * 注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。
 * 提示：
 * 1、2 <= word.length <= 300
 * 2、每个 word[i] 都是一个大写英文字母。
 * 链接：https://leetcode.cn/problems/minimum-distance-to-type-a-word-using-two-fingers/
"""
from functools import cache


class Solution:

    def minimumDistance(self, word: str) -> int:
        pos = dict()
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            pos[c] = divmod(ord(c) - ord('A'), 6)

        @cache
        def dis(c1, c2):
            (x1, y1), (x2, y2) = pos[c1], pos[c2]
            return abs(x1 - x2) + abs(y1 - y2)

        limit = 0x3c3c3c3c
        dp = [[limit] * 27 for _ in range(27)]
        dp[-1][-1] = 0
        for c in word:
            ndp = [[limit] * 27 for _ in range(27)]
            for i in range(27):
                for j in range(27):
                    if dp[i][j] == limit: continue
                    k = ord(c) - ord('A')
                    ndp[k][j] = min(dp[i][j] + (dis(chr(i + ord('A')), c) if i != 26 else 0), ndp[k][j])
                    ndp[i][k] = min(dp[i][j] + (dis(chr(j + ord('A')), c) if j != 26 else 0), ndp[i][k])
            dp = ndp
        ans = limit
        for i in range(27):
            for j in range(27):
                if dp[i][j] == limit: continue
                ans = min(ans, dp[i][j])
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().minimumDistance("QIBZR"))
    # 6
    print(Solution().minimumDistance("LSGQE"))
    # 3
    print(Solution().minimumDistance("CAKE"))
    # 6
    print(Solution().minimumDistance("HAPPY"))