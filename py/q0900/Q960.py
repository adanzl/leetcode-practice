"""
 * 给定由 n 个小写字母字符串组成的数组 strs ，其中每个字符串长度相等。
 * 选取一个删除索引序列，对于 strs 中的每个字符串，删除对应每个索引处的字符。
 * 比如，有 strs = ["abcdef","uvwxyz"] ，删除索引序列 {0, 2, 3} ，删除后为 ["bef", "vyz"] 。
 * 假设，我们选择了一组删除索引 answer ，那么在执行删除操作之后，最终得到的数组的行中的 每个元素 都是按字典序排列的
 * (即(strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]) 和
 * (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]) ，依此类推）。
 * 请返回 answer.length 的最小可能值 。
 * 提示：
 * 1、n == strs.length
 * 2、1 <= n <= 100
 * 3、1 <= strs[i].length <= 100
 * 4、strs[i] 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/delete-columns-to-make-sorted-iii/
"""
from math import inf
from typing import *


class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [0] * n
        for i in range(1, n):
            dp[i] = i
            for j in range(i):
                fit = True
                for s in strs:
                    if s[i] < s[j]:
                        fit = False
                        break
                if fit:
                    dp[i] = min(dp[i], dp[j] + i - j - 1)
        ans = inf
        for i in range(n):
            ans = min(ans, dp[i] + n - i - 1)
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minDeletionSize(["abbba"]))
    # 3
    print(Solution().minDeletionSize(["aabbaa", "baabab", "aaabab"]))
    # 3
    print(Solution().minDeletionSize(["babca", "bbazb"]))
    # 4
    print(Solution().minDeletionSize(["edcba"]))
    # 0
    print(Solution().minDeletionSize(["ghi", "def", "abc"]))
