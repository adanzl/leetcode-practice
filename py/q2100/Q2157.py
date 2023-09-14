"""
 * 给你一个下标从 0 开始的字符串数组 words 。每个字符串都只包含 小写英文字母 。words 中任意一个子串中，每个字母都至多只出现一次。
 * 如果通过以下操作之一，我们可以从 s1 的字母集合得到 s2 的字母集合，那么我们称这两个字符串为 关联的 ：
 * 1、往 s1 的字母集合中添加一个字母。
 * 2、从 s1 的字母集合中删去一个字母。
 * 3、将 s1 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。
 * 数组 words 可以分为一个或者多个无交集的 组 。如果一个字符串与另一个字符串关联，那么它们应当属于同一个组。
 * 注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。
 * 请你返回一个长度为 2 的数组 ans ：
 * 1、ans[0] 是 words 分组后的 总组数 。
 * 2、ans[1] 是字符串数目最多的组所包含的字符串数目。
 * 提示：
 * 1、1 <= words.length <= 2 * 10^4
 * 2、1 <= words[i].length <= 26
 * 3、words[i] 只包含小写英文字母。
 * 4、words[i] 中每个字母最多只出现一次。
 * 链接：
"""

from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=2157 lang=python3
#
# [2157] 字符串分组
#


# @lc code=start
class Solution:

    def groupStrings(self, words: List[str]) -> List[int]:
        pa = {}
        cnt = defaultdict(lambda: 0)
        ans = [0, 1]
        for w in words:
            v = 0
            for c in w:
                v |= 1 << (ord(c) - ord('a'))
            pa[v] = v
            cnt[v] += 1
            ans[1] = max(ans[1], cnt[v])
            if cnt[v] == 1: ans[0] += 1

        def find(x):
            if x not in pa: return -1
            if x == pa[x]: return x
            pa[x] = find(pa[x])
            return pa[x]

        def merge(r0, r1):
            if r1 == -1 or r0 == r1: return
            pa[r1] = r0
            cnt[r0] += cnt[r1]
            ans[0] -= 1
            ans[1] = max(ans[1], cnt[r0])

        for v in cnt.keys():
            r0 = find(v)
            # del
            for i in range(v.bit_length()):
                if v & (1 << i):
                    r1 = find(v - (1 << i))
                    merge(r0, r1)
            # add
            for i in range(v.bit_length()):
                if v & (1 << i) == 0:
                    r1 = find(v + (1 << i))
                    merge(r0, r1)
            # modify
            for i in range(v.bit_length()):
                if v & (1 << i):
                    for j in range(v.bit_length()):
                        if v & (1 << j) == 0:
                            r1 = find(v - (1 << i) + (1 << j))
                            merge(r0, r1)
        return ans


# @lc code=end

if __name__ == '__main__':
    # [1,3]
    print(Solution().groupStrings(["abc", "abc", "abc"]))
    # [5,4]
    print(Solution().groupStrings(["web", "a", "te", "hsx", "v", "k", "a", "roh"]))
    # [1,3]
    print(Solution().groupStrings(["a", "ab", "abc"]))
    # [2,3]
    print(Solution().groupStrings(["a", "b", "ab", "cde"]))
