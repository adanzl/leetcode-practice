"""
 * 给你一棵 树（即，一个连通、无向且无环的图），根 节点为 0 ，由编号从 0 到 n - 1 的 n 个节点组成。
 * 这棵树用一个长度为 n 、下标从 0 开始的数组 parent 表示，其中 parent[i] 为节点 i 的父节点，由于节点 0 为根节点，所以 parent[0] == -1 。
 * 另给你一个长度为 n 的字符串 s ，其中 s[i] 是分配给 i 和 parent[i] 之间的边的字符。s[0] 可以忽略。
 * 找出满足 u < v ，且从 u 到 v 的路径上分配的字符可以 重新排列 形成 回文 的所有节点对 (u, v) ，并返回节点对的数目。
 * 如果一个字符串正着读和反着读都相同，那么这个字符串就是一个 回文 。
 * 提示：
 * 1、n == parent.length == s.length
 * 2、1 <= n <= 10^5
 * 3、对于所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立
 * 4、parent[0] == -1
 * 5、parent 表示一棵有效的树
 * 6、s 仅由小写英文数字组成
 * 链接：https://leetcode.cn/problems/count-paths-that-can-form-a-palindrome-in-a-tree/
"""
from collections import Counter
from typing import List


class Solution:

    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        flag = [-1] * n
        ans = 0
        m = lambda x: 1 << (ord(x) - ord('a'))

        def get_flag(i):
            if i == -1: return 0
            if flag[i] == -1:
                flag[i] = get_flag(parent[i]) ^ m(s[i])
            return flag[i]

        cnt = Counter()
        for i in range(n):
            f = get_flag(i)
            ans += cnt[f]
            for j in range(26):
                ans += cnt[f ^ (1 << j)]
            cnt[f] += 1
        return ans


if __name__ == '__main__':
    # 8
    print(Solution().countPalindromePaths([-1, 0, 0, 1, 1, 2], s="acaabc"))
    # 10
    print(Solution().countPalindromePaths([-1, 0, 0, 0, 0], s="aaaaa"))
