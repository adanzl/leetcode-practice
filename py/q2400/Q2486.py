"""
 * 给你两个仅由小写英文字母组成的字符串 s 和 t 。
 * 现在需要通过向 s 末尾追加字符的方式使 t 变成 s 的一个 子序列 ，返回需要追加的最少字符数。
 * 子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。
 * 提示：
 * 1、1 <= s.length, t.length <= 10^5
 * 2、s 和 t 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/append-characters-to-string-to-make-subsequence/
"""


class Solution:

    def appendCharacters(self, s: str, t: str) -> int:
        i_t, i_s = 0, 0
        while i_t < len(t):
            while i_s < len(s):
                if t[i_t] == s[i_s]:
                    i_t += 1
                    i_s += 1
                    break
                i_s += 1
            if i_s == len(s): break
        return len(t) - i_t


if __name__ == '__main__':
    # 0
    print(Solution().appendCharacters("a", "a"))
    # 4
    print(Solution().appendCharacters("coaching", "coding"))
    # 0
    print(Solution().appendCharacters('abcde', 'a'))
    # 5
    print(Solution().appendCharacters('z', 'abcde'))