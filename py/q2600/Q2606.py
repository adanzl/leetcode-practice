"""
 * 给你一个字符串 s ，一个字符 互不相同 的字符串 chars 和一个长度与 chars 相同的整数数组 vals 。
 * 子字符串的开销 是一个子字符串中所有字符对应价值之和。空字符串的开销是 0 。
 * 字符的价值 定义如下：
 * 1、如果字符不在字符串 chars 中，那么它的价值是它在字母表中的位置（下标从 1 开始）。比方说，'a' 的价值为 1 ，'b' 的价值为 2 ，以此类推，'z' 的价值为 26 。
 * 2、否则，如果这个字符在 chars 中的位置为 i ，那么它的价值就是 vals[i] 。
 * 请你返回字符串 s 的所有子字符串中的最大开销。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含小写英文字母。
 * 3、1 <= chars.length <= 26
 * 4、chars 只包含小写英文字母，且 互不相同 。
 * 5、vals.length == chars.length
 * 6、-1000 <= vals[i] <= 1000
 * 链接：https://leetcode.cn/problems/find-the-substring-with-maximum-cost/
"""
from typing import List


class Solution:

    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        ans = 0
        vv = 0
        sc = dict()
        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            sc[c] = i + 1
        for c, v in zip(chars, vals):
            sc[c] = v
        for c in s:
            vv = max(sc[c], vv + sc[c])
            ans = max(ans, vv)

        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maximumCostSubstring("adaa", chars="d", vals=[-1000]))
    # 0
    print(Solution().maximumCostSubstring("abc", chars="abc", vals=[-1, -1, -1]))
