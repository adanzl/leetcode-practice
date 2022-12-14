"""
 * 给你一个字符串 s ，它仅包含字符 'a' 和 'b' 。
 * 你可以删除 s 中任意数目的字符，使得 s 平衡 。
 * 我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时 s[j]= 'a' 。
 * 请你返回使 s 平衡 的 最少 删除次数。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 要么是 'a' 要么是 'b'​。
 * 链接：https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/
"""


class Solution:

    def minimumDeletions(self, s: str) -> int:
        bn, ans = 0, 0x3c3c3c3c
        for c in s:
            if c == 'a':
                ans = min(ans + 1, bn)
            else:
                bn += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minimumDeletions("aababbab"))
    # 2
    print(Solution().minimumDeletions("bbaaaaabb"))