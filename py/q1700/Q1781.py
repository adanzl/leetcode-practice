"""
 * 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
 * 比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
 * 给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。
 * 提示：
 * 1、1 <= s.length <= 500
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/sum-of-beauty-of-all-substrings/
"""
from typing import Counter, List


class Solution:

    def beautySum(self, s: str) -> int:
        ans, n = 0, len(s)
        dp = [Counter() for _ in s]
        for i in range(n):
            dp[i][s[i]] += 1
            for j in range(i - 1, -1, -1):
                dp[j][s[i]] += 1
                mc = dp[j].most_common()
                ans += mc[0][1] - mc[-1][1]
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().beautySum("aabcb"))
    # 17
    print(Solution().beautySum("aabcbaa"))