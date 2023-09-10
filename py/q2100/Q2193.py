"""
 * 给你一个只包含小写英文字母的字符串 s 。
 * 每一次 操作 ，你可以选择 s 中两个 相邻 的字符，并将它们交换。
 * 请你返回将 s 变成回文串的 最少操作次数 。
 * 注意 ，输入数据会确保 s 一定能变成一个回文串。
 * 提示：
 * 1、1 <= s.length <= 2000
 * 2、s 只包含小写英文字母。
 * 3、s 可以通过有限次操作得到一个回文串。
 * 链接：https://leetcode.cn/problems/minimum-number-of-moves-to-make-palindrome/
"""

#
# @lc app=leetcode.cn id=2193 lang=python3
#
# [2193] 得到回文串的最少操作次数
#


# @lc code=start
class Solution:

    def minMovesToMakePalindrome(self, s: str) -> int:
        ss = list(s)
        ans = 0
        l, r = 0, len(s) - 1
        while l <= r:
            if ss[l] != ss[r]:
                lp = l + 1
                while lp <= r and ss[lp] != ss[r]:
                    lp += 1
                rp = r - 1
                while rp >= l and ss[rp] != ss[l]:
                    rp -= 1
                if lp - l < r - rp:
                    ans += lp - l
                    for i in range(lp, l, -1):
                        ss[i], ss[i - 1] = ss[i - 1], ss[i]
                else:
                    ans += r - rp
                    for i in range(rp, r):
                        ss[i], ss[i + 1] = ss[i + 1], ss[i]
            l += 1
            r -= 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 17
    print(Solution().minMovesToMakePalindrome("eqvvhtcsaaqtqesvvqch"))
    # 2
    print(Solution().minMovesToMakePalindrome("aabb"))
    # 2
    print(Solution().minMovesToMakePalindrome("letelt"))