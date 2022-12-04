"""
 * 给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。
 * 返回 已排序的字符串 。如果有多个答案，返回其中任何一个。
 * 提示:
 * 1、1 <= s.length <= 5 * 10^5
 * 2、s 由大小写英文字母和数字组成
 * 链接：https://leetcode.cn/problems/sort-characters-by-frequency
"""
from typing import Counter


class Solution:

    def frequencySort(self, s: str) -> str:
        arr = sorted([[v, k] for k, v in Counter(s).items()], reverse=True)
        ans = [k * v for v, k in arr]
        return ''.join(ans)


if __name__ == '__main__':
    # "eert"
    print(Solution().frequencySort("tree"))
    # "aaaccc"
    print(Solution().frequencySort("cccaaa"))
    # "bbAa"
    print(Solution().frequencySort("Aabb"))