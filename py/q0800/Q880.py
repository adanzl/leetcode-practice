"""
 * 给定一个编码字符串 S。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：
 * 1、如果所读的字符是字母，则将该字母写在磁带上。
 * 2、如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
 * 现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。
 * 提示：
 * 1、2 <= S.length <= 100
 * 2、S 只包含小写字母与数字 2 到 9 。
 * 3、S 以字母开头。
 * 4、1 <= K <= 10^9
 * 5、题目保证 K 小于或等于解码字符串的长度。
 * 6、解码后的字符串保证少于 2^63 个字母。
 * 链接：https://leetcode.cn/problems/decoded-string-at-index
"""

from typing import List

#
# @lc app=leetcode.cn id=880 lang=python3
#
# [880] 索引处的解码字符串
#


# @lc code=start
class Solution:

    def decodeAtIndex(self, s: str, k: int) -> str:
        cnt = 0
        action = []
        for c in s:
            if c.isdigit():
                cnt *= int(c)
                action.append([int(c), action[-1][1]])
            else:
                action.append([1, c])
                cnt += 1
            if cnt >= k:
                break
        while action:
            a, c = action.pop()
            if k % cnt == 0:
                return c
            if a == 1:
                cnt -= 1
            else:
                cnt //= a
                k %= cnt
        return ''


# @lc code=end

if __name__ == '__main__':
    # "a"
    print(Solution().decodeAtIndex("a2345678999999999999999", 10**9))
    # "h"
    print(Solution().decodeAtIndex("ha22", 5))
    # "o"
    print(Solution().decodeAtIndex("leet2code3", 10))
    # "a"
    print(Solution().decodeAtIndex("a2345678999999999999999", 1))
