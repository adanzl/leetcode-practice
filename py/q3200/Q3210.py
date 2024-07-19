"""
 * 给你一个字符串 s 和一个整数 k。请你使用以下算法加密字符串：
 * 对于字符串 s 中的每个字符 c，用字符串中 c 后面的第 k 个字符替换 c（以循环方式）。
 * 返回加密后的字符串。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、1 <= k <= 10^4
 * 3、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/find-the-encrypted-string/
"""


class Solution:

    def getEncryptedString(self, s: str, k: int) -> str:
        ans = []
        for i, c in enumerate(s):
            ans.append(s[(i + k) % len(s)])
        return ''.join(ans)


if __name__ == '__main__':
    # "oxoq"
    print(Solution().getEncryptedString("oxoq", 4))
    # "tdar"
    print(Solution().getEncryptedString("dart", k=3))
    # "aaa"
    print(Solution().getEncryptedString("aaa", k=1))
