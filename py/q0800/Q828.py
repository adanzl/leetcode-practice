import collections
"""
 * 我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。
 * 例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueChars(s) = 5 。
 * 本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。输入用例保证返回值为 32 位整数。
 * 注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含大写英文字符
 * 链接：https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string
"""


class Solution:

    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        char_dict = collections.defaultdict(list)
        for i, c in enumerate(s):
            char_dict[c].append(i)
        for c, arr in char_dict.items():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return int(ans)


if __name__ == '__main__':
    # 1785
    print(Solution().uniqueLetterString("OBXBYZTNRTJRSHWNWJXQACMCZT"))
    # 1949
    print(Solution().uniqueLetterString("OBXBYZTNRTJRSHWNWJXQACMCZTX"))
    print(Solution().uniqueLetterString("ABC"))  # 10
    print(Solution().uniqueLetterString("ABA"))  # 8
    print(Solution().uniqueLetterString("LEETCODE"))  # 92
    print(Solution().uniqueLetterString("AA"))  # 2
