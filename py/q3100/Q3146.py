"""
 * 给你两个字符串 s 和 t，每个字符串中的字符都不重复，且 t 是 s 的一个排列。
 * 排列差 定义为 s 和 t 中每个字符在两个字符串中位置的绝对差值之和。
 * 返回 s 和 t 之间的 排列差 。
 * 提示：
 * 1、1 <= s.length <= 26
 * 2、每个字符在 s 中最多出现一次。
 * 3、t 是 s 的一个排列。
 * 4、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/permutation-difference-between-two-strings/
"""


class Solution:

    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        d = {}
        for i, c in enumerate(s):
            d[c] = i
        for i, c in enumerate(t):
            ans += abs(i - d[c])
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().findPermutationDifference("abc", t="bac"))
    # 12
    print(Solution().findPermutationDifference("abcde", t="edbac"))
