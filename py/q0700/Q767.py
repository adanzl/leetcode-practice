"""
 * 给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。
 * 返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。
 * 提示:
 * 1、1 <= s.length <= 500
 * 2、s 只包含小写字母
 * 链接：https://leetcode.cn/problems/reorganize-string/
"""
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:

    def reorganizeString(self, s: str) -> str:
        pre = None
        h = [[-c, v] for v, c in Counter(s).items()]
        heapify(h)
        ans = []
        while h:
            v = heappop(h)
            ans.append(v[1])
            if pre and pre[0] < -1:
                heappush(h, [pre[0] + 1, pre[1]])
            pre = v
        return ''.join(ans) if len(ans) == len(s) else ''


if __name__ == '__main__':
    # 'aba'
    print(Solution().reorganizeString("aab"))
    # ''
    print(Solution().reorganizeString("aaab"))