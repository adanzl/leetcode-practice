"""
 * 给你一个字符串 s 和一个字符 c 。返回在字符串 s 中并且以 c 字符开头和结尾的非空子字符串的总数。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 和 c 均由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/count-substrings-starting-and-ending-with-given-character/
"""
from collections import Counter
import math


class Solution:

    def countSubstrings(self, s: str, c: str) -> int:
        cnt = Counter(s)[c]
        return math.comb(cnt, 2) + cnt


if __name__ == '__main__':
    # 6
    print(Solution().countSubstrings("abada", c="a"))
    # 6
    print(Solution().countSubstrings("zzz", c="z"))
