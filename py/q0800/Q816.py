"""
 * 我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。
 * 原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。
 * 此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。
 * 最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。
 * 提示:
 * 1、4 <= S.length <= 12.
 * 2、S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。
 * 链接：https://leetcode.cn/problems/ambiguous-coordinates/
"""
from itertools import product
from typing import List


class Solution:

    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        s = s[1:-1]
        n = len(s)

        def f(start, end):
            ret = []
            ss = s[start:end + 1]
            if end - start + 1 == 1: return [ss]
            limit = len(ss)
            if s[start] != '0': ret.append(ss)
            else: limit = min(limit, 2)
            if int(ss):
                for i in range(1, limit):  # dot
                    if not ss[i:].endswith('0'): ret.append(ss[:i] + '.' + ss[i:])
            return ret

        for i in range(1, n):  # comma
            arr1, arr2 = [], []
            arr1.extend(f(0, i - 1))
            arr2.extend(f(i, n - 1))
            for v1, v2 in product(arr1, arr2):
                ans.append('(' + v1 + ', ' + v2 + ')')
        return ans


if __name__ == '__main__':
    # ["(0.01, 0)"]
    print(Solution().ambiguousCoordinates("(0010)"))
    # ["(0.001, 1)", "(0, 0.011)"]
    print(Solution().ambiguousCoordinates("(00011)"))
    # ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
    print(Solution().ambiguousCoordinates("(123)"))
    # ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
    print(Solution().ambiguousCoordinates("(0123)"))
    # [(10, 0)]
    print(Solution().ambiguousCoordinates("(100)"))