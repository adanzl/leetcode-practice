"""
 * 给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目：
 * 可以写成某个字符串与其自身相连接的形式（即，可以写为 a + a，其中 a 是某个字符串）。
 * 例如，abcabc 就是 abc 和它自身连接形成的。
 * 提示：
 * 1、1 <= text.length <= 2000
 * 2、text 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/distinct-echo-substrings/
"""

#
# @lc app=leetcode.cn id=1316 lang=python3
#
# [1316] 不同的循环子字符串
#

# @lc code=start


class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        # f[i][j] 以s[i]和s[j]结尾的字符串有几个共同长度
        # f[i][j]: 如果s[i]==s[j], f[i][j]=f[i-1][j-1]+1; 否则 f[i][j]=0
        for i in range(n):
            for j in range(i, -1, -1):
                if text[i] == text[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
        ans = set()
        for i in range(n):
            for j in range(i - 1, i // 2 - 1, -1):
                if f[i + 1][j + 1] >= i - j:
                    ans.add(text[j + 1:i + 1])
        return len(ans)


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().distinctEchoSubstrings('leetcodeleetcode'))
    # 5
    print(Solution().distinctEchoSubstrings("aaaaaaaaaa"))
    # 3
    print(Solution().distinctEchoSubstrings('abcabcabc'))