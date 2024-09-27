"""
 * 给你一个长度为 n 的字符串 s 和一个整数 k ，n 是 k 的 倍数 。你的任务是将字符串 s 哈希为一个长度为 n / k 的新字符串 result 。
 * 首先，将 s 分割成 n / k 个 子字符串 ，每个子字符串的长度都为 k 。然后，将 result 初始化为一个 空 字符串。
 * 我们依次从前往后处理每一个 子字符串 ：
 * 1、一个字符的 哈希值 是它在 字母表 中的下标（也就是 'a' → 0 ，'b' → 1 ，... ，'z' → 25）。
 * 2、将子字符串中字母的 哈希值 求和。
 * 3、将和对 26 取余，将结果记为 hashedChar 。
 * 4、找到小写字母表中 hashedChar 对应的字符。
 * 5、将该字符添加到 result 的末尾。
 * 返回 result 。
 * 提示：
 * 1、1 <= k <= 100
 * 2、k <= s.length <= 1000
 * 3、s.length 能被 k 整除。
 * 4、s 只含有小写英文字母。
 * 链接：https://leetcode.cn/problems/hash-divided-string/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        ans = []
        for i in range(n // k):
            val = 0
            for j in range(k):
                ii = i * k + j
                val += ord(s[ii]) - ord('a')
            ans.append(chr(val % 26 + ord('a')))
        return ''.join(ans)


if __name__ == '__main__':
    # "bf"
    print(Solution().stringHash("abcd", k=2))
    # "i"
    print(Solution().stringHash("mxz", k=3))
