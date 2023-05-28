"""
 * 给你一个下标从 0 开始的字符串 s 和一个单词字典 dictionary 。
 * 你需要将 s 分割成若干个 互不重叠 的子字符串，每个子字符串都在 dictionary 中出现过。s 中可能会有一些 额外的字符 不在任何子字符串中。
 * 请你采取最优策略分割 s ，使剩下的字符 最少 。
 * 提示：
 * 1、1 <= s.length <= 50
 * 2、1 <= dictionary.length <= 50
 * 3、1 <= dictionary[i].length <= 50
 * 4、dictionary[i] 和 s 只包含小写英文字母。
 * 5、dictionary 中的单词互不相同。
 * 链接：https://leetcode.cn/problems/extra-characters-in-a-string/
"""


class Solution:

    def minExtraChar(self, s, dictionary):
        dp = [-1] * (len(s) + 1)
        st = set(dictionary)

        def func(idx, s, st, dp):
            if idx == len(s): return 0
            if dp[idx] != -1: return dp[idx]
            res = float('inf')
            for j in range(idx, len(s)):
                substr = s[idx:j + 1]
                if substr in st:
                    res = min(res, 0 + func(j + 1, s, st, dp))
                else:
                    res = min(res, j - idx + 1 + func(j + 1, s, st, dp))
            dp[idx] = res
            return res

        return func(0, s, st, dp)


if __name__ == '__main__':
    # 1
    print(Solution().minExtraChar("leetscode", dictionary=["leet", "code", "leetcode"]))
    # 3
    print(Solution().minExtraChar("sayhelloworld", dictionary=["hello", "world"]))
