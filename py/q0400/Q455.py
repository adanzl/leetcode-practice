"""
 * 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
 * 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
 * 如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
 * 你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
 * 提示：
 * 1、1 <= g.length <= 3 * 10^4
 * 2、0 <= s.length <= 3 * 10^4
 * 3、1 <= g[i], s[j] <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/assign-cookies/
"""
from typing import List


class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort(reverse=False)
        s.sort(reverse=False)
        i_g, i_s = 0, 0
        while i_g < len(g) and i_s < len(s):
            if g[i_g] <= s[i_s]:
                ans += 1
                i_g += 1
            i_s += 1

        return ans


if __name__ == '__main__':
    # 1
    print(Solution().findContentChildren([1, 2, 3], s=[1, 1]))
    # 2
    print(Solution().findContentChildren([1, 2], s=[1, 2, 3]))
    #
    # print(Solution().findContentChildren())
