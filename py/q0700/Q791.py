"""
 * 给定两个字符串 order 和 s 。order 的所有单词都是 唯一 的，并且以前按照一些自定义的顺序排序。
 * 对 s 的字符进行置换，使其与排序的 order 相匹配。更具体地说，如果在 order 中的字符 x 出现字符 y 之前，那么在排列后的字符串中， x 也应该出现在 y 之前。
 * 返回 满足这个性质的 s 的任意排列 。
 * 提示:
 * 1、1 <= order.length <= 26
 * 2、1 <= s.length <= 200
 * 3、order 和 s 由小写英文字母组成
 * 4、order 中的所有字符都 不同
 * 链接：https://leetcode.cn/problems/custom-sort-string/
"""

from collections import defaultdict


class Solution:

    def customSortString(self, order: str, s: str) -> str:
        pro = defaultdict(int)
        for i in range(len(order)):
            pro[order[i]] = i
        ss = sorted(list(s), key=lambda x: pro[x])
        return ''.join(ss)


if __name__ == '__main__':
    # "cbad"
    print(Solution().customSortString("cba", "abcd"))
    # "cbad"
    print(Solution().customSortString("cbafg", "abcd"))
