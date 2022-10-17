"""
 * 有一棵 n 个节点的无向树，节点编号为 0 到 n - 1 。
 * 给你一个长度为 n 下标从 0 开始的整数数组 nums ，其中 nums[i] 表示第 i 个节点的值。
 * 同时给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 与 bi 之间有一条边。
 * 你可以 删除 一些边，将这棵树分成几个连通块。一个连通块的 价值 定义为这个连通块中 所有 节点 i 对应的 nums[i] 之和。
 * 你需要删除一些边，删除后得到的各个连通块的价值都相等。请返回你可以删除的边数 最多 为多少。
 * 提示：
 * 1、1 <= n <= 2 * 10^4
 * 2、nums.length == n
 * 3、1 <= nums[i] <= 50
 * 4、edges.length == n - 1
 * 5、edges[i].length == 2
 * 6、0 <= edges[i][0], edges[i][1] <= n - 1
 * 7、edges 表示一棵合法的树。
 * 链接：https://leetcode.cn/problems/create-components-with-same-value/
"""
from typing import List


class Solution:
    '''
    统计子树大小、点权和
    def dfs(src, parent)->int:
        sz = 1
        for next in g[src]:
            if next == parent: continue
            sz += dfs(next, src)
        return sz
    dfs(0, -1)
    '''

    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for v, w in edges:
            g[v].append(w)
            g[w].append(v)

        mx, sm = max(nums), sum(nums)

        def dfs(src, parent, target):  # remain
            ret = nums[src]
            for next in g[src]:
                if next == parent: continue
                res = dfs(next, src, target)
                if res == -1: return -1
                ret += res
            if ret == target: return 0
            if ret > target: return -1
            return ret

        i = min(n, sm // mx)  # del i edges
        for i in range(min(n, sm // mx), 0, -1):
            if sm % i != 0: continue
            if dfs(0, -1, sm // i) == 0: return i - 1
        return -1


if __name__ == '__main__':
    # 2
    print(Solution().componentValue([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]))
    # 0
    print(Solution().componentValue([2], []))
