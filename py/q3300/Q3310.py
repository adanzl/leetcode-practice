"""
 * 你正在维护一个项目，该项目有 n 个方法，编号从 0 到 n - 1。
 * 给你两个整数 n 和 k，以及一个二维整数数组 invocations，其中 invocations[i] = [ai, bi] 表示方法 ai 调用了方法 bi。
 * 已知如果方法 k 存在一个已知的 bug。那么方法 k 以及它直接或间接调用的任何方法都被视为 可疑方法 ，我们需要从项目中移除这些方法。
 * 只有当一组方法没有被这组之外的任何方法调用时，这组方法才能被移除。
 * 返回一个数组，包含移除所有 可疑方法 后剩下的所有方法。你可以以任意顺序返回答案。如果无法移除 所有 可疑方法，则 不 移除任何方法。
 * 提示:
 * 1、1 <= n <= 10^5
 * 2、0 <= k <= n - 1
 * 3、0 <= invocations.length <= 2 * 10^5
 * 4、invocations[i] == [ai, bi]
 * 5、0 <= ai, bi <= n - 1
 * 6、ai != bi
 * 7、invocations[i] != invocations[j]
 * 链接：https://leetcode.cn/problems/remove-methods-from-project/
"""

from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=3310 lang=python3
#
# [3310] 移除可疑的方法
#


# @lc code=start
class Solution:

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u,v in invocations:
            g[u].append(v)
        parent = [i for i in range(n)]
        doubt = set()
        def dfs(u, doubt):
            if u in doubt: return 
            doubt.add(u)
            for nx in g[u]:
                dfs(nx, doubt)
        dfs(k, doubt)
        def find(x):
            r = x
            while parent[r] != r:
                r = parent[r]
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r
        for u, v in invocations:
            r0, r1 = find(u), find(v)
            parent[r1] = r0
        cnt = Counter()
        for i in range(n):
            cnt[find(i)] += 1
        if cnt[find(k)] == len(doubt):
            return [i for i in range(n) if i not in doubt]
        return [i for i in range(n)]


# @lc code=end

if __name__ == '__main__':
    # [0,1,2,3]
    print(Solution().remainingMethods(4, k=1, invocations=[[1, 2], [0, 1], [3, 2]]))
    # [3,4]
    print(Solution().remainingMethods(5, k=0, invocations=[[1, 2], [0, 2], [0, 1], [3, 4]]))
    # []
    print(Solution().remainingMethods(3, k=2, invocations=[[1, 2], [0, 1], [2, 0]]))
