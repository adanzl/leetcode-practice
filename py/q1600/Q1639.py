"""
 * 给你一个字符串列表 words 和一个目标字符串 target 。words 中所有字符串都 长度相同  。
 * 你的目标是使用给定的 words 字符串列表按照下述规则构造 target ：
 * 1、从左到右依次构造 target 的每一个字符。
 * 2、为了得到 target 第 i 个字符（下标从 0 开始），当 target[i] = words[j][k] 时，你可以使用 words 列表中第 j 个字符串的第 k 个字符。
 * 3、一旦你使用了 words 中第 j 个字符串的第 k 个字符，你不能再使用 words 字符串列表中任意单词的第 x 个字符（x <= k）。也就是说，所有单词下标小于等于 k 的字符都不能再被使用。
 * 4、请你重复此过程直到得到目标字符串 target 。
 * 请注意， 在构造目标字符串的过程中，你可以按照上述规定使用 words 列表中 同一个字符串 的 多个字符 。
 * 请你返回使用 words 构造 target 的方案数。由于答案可能会很大，请对 109 + 7 取余 后返回。
 * （译者注：此题目求的是有多少个不同的 k 序列，详情请见示例。）
 * 提示：
 * 1、1 <= words.length <= 1000
 * 2、1 <= words[i].length <= 1000
 * 3、words 中所有单词长度相同。
 * 4、1 <= target.length <= 1000
 * 5、words[i] 和 target 都仅包含小写英文字母。
 * 链接：https://leetcode.cn/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
"""
from collections import Counter
from itertools import accumulate
from typing import List


class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        dp = [1] + [0] * (n)
        cnt = [Counter() for _ in range(n)]
        for word in words:
            for i, c in enumerate(word):
                cnt[i][c] += 1
        for i, t in enumerate(target):
            pre_sum = list(accumulate(dp))
            dp = [0] * (n + 1)
            for j in range(i, n):
                dp[j + 1] += cnt[j][t] * (pre_sum[j])
        return sum(dp) % MOD


if __name__ == '__main__':
    # 6
    print(Solution().numWays(["acca", "bbbb", "caca"], "aba"))
    # 4
    print(Solution().numWays(["abba", "baab"], "bab"))
    # 1
    print(Solution().numWays(["abcd"], "abcd"))
    # 16
    print(Solution().numWays(["abab", "baba", "abba", "baab"], "abba"))
