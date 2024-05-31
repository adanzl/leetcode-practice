"""
 * 给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件：
 * 1、这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[x..y] ，要么 j < x 要么 i > y 。
 * 2、如果一个子字符串包含字符 char ，那么 s 中所有 char 字符都应该在这个子字符串中。
 * 请你找到满足上述条件的最多子字符串数目。
 * 如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。
 * 请注意，你可以以 任意 顺序返回最优解的子字符串。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/maximum-number-of-non-overlapping-substrings/
"""

from typing import List

#
# @lc app=leetcode.cn id=1520 lang=python3
#
# [1520] 最多的不重叠子字符串
#

# @lc code=start


class Solution:

    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ids, n = {}, len(s)
        ans = []
        for i, c in enumerate(s):
            if c in ids:
                ids[c][1] = i
            else:
                ids[c] = [i, i]
        r_list = sorted(ids.values(), key=lambda x: x[1])
        barrier = 0
        for l, r in r_list:
            i, valid = r, True
            while i >= l:
                c = s[i]
                if ids[c][1] > r:
                    valid = False
                    break
                else:
                    l = min(l, ids[c][0])
                if l < barrier:
                    valid = False
                    break
                i -= 1
            if valid:
                ans.append(s[l:r + 1])
                barrier = r + 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # ["cabcccbaa"]
    print(Solution().maxNumOfSubstrings("cabcccbaa"))
    # ["a","b"]
    print(Solution().maxNumOfSubstrings("dabddcdc"))
    # ["d","bb","cc"]
    print(Solution().maxNumOfSubstrings("abbaccd"))
    # ["ababa"]
    print(Solution().maxNumOfSubstrings("ababa"))
    # ["abab"]
    print(Solution().maxNumOfSubstrings("abab"))
    # ["e","f","ccc"]
    print(Solution().maxNumOfSubstrings("adefaddaccc"))
