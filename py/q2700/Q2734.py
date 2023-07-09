"""
 * 给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以完成以下行为：
 * 选则 s 的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b' 用 'a' 替换，'a' 用 'z' 替换。
 * 返回执行上述操作 恰好一次 后可以获得的 字典序最小 的字符串。
 * 子字符串 是字符串中的一个连续字符序列。
 * 现有长度相同的两个字符串 x 和 字符串 y ，在满足 x[i] != y[i] 的第一个位置 i 上，如果  x[i] 在字母表中先于 y[i] 出现，则认为字符串 x 比字符串 y 字典序更小 。
 * 提示：
 * 1、1 <= s.length <= 3 * 10^5
 * 2、s 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/
"""


class Solution:

    def smallestString(self, s: str) -> str:
        ans = []
        i = 0
        f = False
        while i < len(s):
            c = s[i]
            if c == 'a':
                if f:
                    break
                else:
                    ans.append(c)
                    i += 1
                    continue
            f = True
            ans.append(chr(ord(c) - 1))
            i += 1
        if not f:
            ans[-1] = 'z'
        return "".join(ans) + s[i:]


if __name__ == '__main__':
    # "az"
    print(Solution().smallestString("aa"))
    # "abaab"
    print(Solution().smallestString("acbbc"))
    # "baabc"
    print(Solution().smallestString("cbabc"))
    # "kddsbncd"
    print(Solution().smallestString("leetcode"))