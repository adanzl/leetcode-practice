"""
 * 给你一个数组 arr ，数组中有 n 个 非空 字符串。
 * 请你求出一个长度为 n 的字符串 answer ，满足：
 *     answer[i] 是 arr[i] 最短 的子字符串，且它不是 arr 中其他任何字符串的子字符串。
 *     如果有多个这样的子字符串存在，answer[i] 应该是它们中字典序最小的一个。如果不存在这样的子字符串，answer[i] 为空字符串。
 * 请你返回数组 answer 。
 * 提示：
 * 1、n == arr.length
 * 2、2 <= n <= 100
 * 3、1 <= arr[i].length <= 20
 * 4、arr[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/shortest-uncommon-substring-in-an-array/
"""
from functools import cache
from typing import List


class Solution:

    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ans = []

        @cache
        def is_sub(ss, idx):
            return arr[idx].find(ss) != -1

        for i, s in enumerate(arr):
            aa = ""
            for size in range(1, len(s) + 1):
                for ii in range(len(s) - size + 1):
                    ss = s[ii:ii + size]
                    valid = True
                    for idx in range(len(arr)):
                        if idx == i: continue
                        if is_sub(ss, idx):
                            valid = False
                            break
                    if valid and (aa == "" or ss < aa):
                        aa = ss
                if aa != '':
                    break
            ans.append(aa)
        return ans


if __name__ == '__main__':
    # ["g","x","z","r","i","c","h"]
    print(Solution().shortestSubstrings(["gfnt", "xn", "mdz", "yfmr", "fi", "wwncn", "hkdy"]))
    # ["ab","","ba",""]
    print(Solution().shortestSubstrings(["cab", "ad", "bad", "c"]))
    # ["","","abcd"]
    print(Solution().shortestSubstrings(["abc", "bcd", "abcd"]))
