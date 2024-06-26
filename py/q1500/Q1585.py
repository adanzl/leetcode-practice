"""
 * 给你两个字符串 s 和 t ，请你通过若干次以下操作将字符串 s 转化成字符串 t ：
 * 选择 s 中一个 非空 子字符串并将它包含的字符就地 升序 排序。
 * 比方说，对下划线所示的子字符串进行操作可以由 "14234" 得到 "12344" 。
 * 如果可以将字符串 s 变成 t ，返回 true 。否则，返回 false 。
 * 一个 子字符串 定义为一个字符串中连续的若干字符。
 * 提示：
 * 1、s.length == t.length
 * 2、1 <= s.length <= 10^5
 * 3、s 和 t 都只包含数字字符，即 '0' 到 '9' 。
 * 链接：https://leetcode.cn/problems/check-if-string-is-transformable-with-substring-sort-operations
"""

from collections import defaultdict

#
# @lc app=leetcode.cn id=1585 lang=python3
#
# [1585] 检查字符串是否可以通过排序子字符串得到另一个字符串
#


# @lc code=start
class Solution:

    def isTransformable(self, s: str, t: str) -> bool:
        pos, n = defaultdict(list), len(s)
        for i, c in enumerate(s):
            pos[c].append(i)
        for i in range(n - 1, -1, -1):
            if len(pos[t[i]]) == 0: return False
            ii = pos[t[i]].pop()
            for tn in range(int(t[i]), 10):
                a = pos[str(tn)]
                if a and a[-1] > ii:
                    return False
        return True


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isTransformable("84532", t="34852"))
    # True
    print(Solution().isTransformable("34521", t="23415"))
    # False
    print(Solution().isTransformable("12345", t="12435"))
    # False
    print(Solution().isTransformable("1", t="2"))
