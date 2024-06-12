"""
 * 给你一个字符串 word，请你使用以下算法进行压缩：
 * 从空字符串 comp 开始。当 word 不为空 时，执行以下操作：
 * 1、移除 word 的最长单字符前缀，该前缀由单一字符 c 重复多次组成，且该前缀长度 最多 为 9 。
 * 2、将前缀的长度和字符 c 追加到 comp 。
 * 返回字符串 comp 。
 * 提示：
 * 1、1 <= word.length <= 2 * 10^5
 * 2、word 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/string-compression-iii/
"""


class Solution:

    def compressedString(self, word: str) -> str:
        ln, cc = 0, ''
        ans = ''
        for c in word:
            if ln >= 9 or cc != c:
                if ln:
                    ans += str(ln) + cc
                ln = 1
                cc = c
            else:
                ln += 1
        return ans + str(ln) + c


if __name__ == '__main__':
    # "1a1b1c1d1e"
    print(Solution().compressedString("abcde"))
    # "9a5a2b"
    print(Solution().compressedString("aaaaaaaaaaaaaabb"))
