"""
 * 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
 * 请返回所有可行解 s 中最长长度。
 * 提示：
 * 1、1 <= arr.length <= 16
 * 2、1 <= arr[i].length <= 26
 * 3、arr[i] 中只含有小写英文字母
 * 链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
"""
from typing import List


class Solution:

    def maxLength(self, arr: List[str]) -> int:
        a = []
        for s in arr:
            m = 0
            for c in s:
                mm = 1 << (ord(c) - ord('a'))
                if m & mm: break
                m |= mm
            else:
                a.append([m, len(s)])
        n = len(a)
        ans = 0

        def dfs(idx, mask, l):
            nonlocal ans
            if idx == n:
                ans = max(ans, l)
                return
            if mask & a[idx][0] == 0:
                dfs(idx + 1, mask | a[idx][0], l + a[idx][1])
            dfs(idx + 1, mask, l)

        dfs(0, 0, 0)
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maxLength(["un", "iq", "ue"]))
    # 6
    print(Solution().maxLength(["cha", "r", "act", "ers"]))
    # 26
    print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
    # 0
    print(Solution().maxLength(["yy", "bkhwmpbiisbldzknpm"]))
