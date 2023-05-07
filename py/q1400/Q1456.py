"""
 * 给你字符串 s 和整数 k 。
 * 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
 * 英文中的 元音字母 为（a, e, i, o, u）。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 由小写英文字母组成
 * 3、1 <= k <= s.length
 * 链接：https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        o = 'aeiou'
        ans, l = 0, 0
        for i, c in enumerate(s):
            if c in o:
                l += 1
            if i >= k and s[i - k] in o:
                l -= 1
            ans = max(ans, l)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maxVowels("abciiidef", k=3))
    # 2
    print(Solution().maxVowels("aeiou", k=2))
    # 2
    print(Solution().maxVowels("leetcode", k=3))
    # 0
    print(Solution().maxVowels("rhythms", k=4))
    # 1
    print(Solution().maxVowels("tryhard", k=4))
