"""
 * 给你一个字符串 s，请你对 s 的子串进行检测。
 * 每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。
 * 我们可以 重新排列 子串 s[left], ..., s[right]，并从中选择 最多 k 项替换成任何小写英文字母。 
 * 如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。
 * 返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。
 * 注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。
 * （另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）
 * 提示：
 * 1、1 <= s.length, queries.length <= 10^5
 * 2、0 <= queries[i][0] <= queries[i][1] < s.length
 * 3、0 <= queries[i][2] <= s.length
 * 4、s 中只有小写英文字母
 * 链接：https://leetcode.cn/problems/can-make-palindrome-from-substring/
"""
from typing import List


class Solution:

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        cnt = [0] * 26
        pre = [cnt]
        for c in s:
            nCnt = pre[-1][:]
            nCnt[ord(c) - ord('a')] += 1
            pre.append(nCnt)
        for l, r, k in queries:
            ll, rr = pre[l], pre[r + 1]
            cc = [(v2 - v1) % 2 for v1, v2 in zip(ll, rr)]
            ans.append(sum(cc) // 2 <= k)
        return ans


if __name__ == '__main__':
    # [true,false,false,true,true]
    print(Solution().canMakePaliQueries("abcda", queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))