"""
 * 给你两个 正整数 数组 arr1 和 arr2 。
 * 正整数的 前缀 是其 最左边 的一位或多位数字组成的整数。例如，123 是整数 12345 的前缀，而 234 不是 。
 * 设若整数 c 是整数 a 和 b 的 公共前缀 ，那么 c 需要同时是 a 和 b 的前缀。
 * 例如，5655359 和 56554 有公共前缀 565 ，而 1223 和 43456 没有 公共前缀。
 * 你需要找出属于 arr1 的整数 x 和属于 arr2 的整数 y 组成的所有数对 (x, y) 之中最长的公共前缀的长度。
 * 返回所有数对之中最长公共前缀的长度。如果它们之间不存在公共前缀，则返回 0 。
 * 提示：
 * 1、1 <= arr1.length, arr2.length <= 5 * 10^4
 * 2、1 <= arr1[i], arr2[i] <= 10^8
 * 链接：https://leetcode.cn/problems/find-the-length-of-the-longest-common-prefix/description/
"""
from typing import List


class Solution:

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        ans = 0
        t_tree = {}

        def insert(t: dict, s, ii):
            if ii == len(s):
                return
            if s[ii] not in t:
                t[s[ii]] = dict()
            insert(t[s[ii]], s, ii + 1)

        def search(t, s, ii):
            if ii == len(s):
                return len(s)
            if s[ii] in t:
                return search(t[s[ii]], s, ii + 1)
            return ii

        for num in arr1:
            insert(t_tree, str(num), 0)
        for num in arr2:
            ans = max(ans, search(t_tree, str(num), 0))

        return ans


if __name__ == '__main__':
    # 3
    print(Solution().longestCommonPrefix([1, 10, 100], arr2=[1000]))
    # 0
    print(Solution().longestCommonPrefix([1, 2, 3], arr2=[4, 4, 4]))
    #
    # print(Solution().longestCommonPrefix())
