"""
 * 有一棵根节点为 0 的 家族树 ，总共包含 n 个节点，节点编号为 0 到 n - 1 。
 * 给你一个下标从 0 开始的整数数组 parents ，其中 parents[i] 是节点 i 的父节点。
 * 由于节点 0 是 根 ，所以 parents[0] == -1 。
 * 总共有 105 个基因值，每个基因值都用 闭区间 [1, 10^5] 中的一个整数表示。
 * 给你一个下标从 0 开始的整数数组 nums ，其中 nums[i] 是节点 i 的基因值，且基因值 互不相同 。
 * 请你返回一个数组 ans ，长度为 n ，其中 ans[i] 是以节点 i 为根的子树内 缺失 的 最小 基因值。
 * 节点 x 为根的 子树 包含节点 x 和它所有的 后代 节点。
 * 提示：
 * 1、n == parents.length == nums.length
 * 2、2 <= n <= 10^5
 * 3、对于 i != 0 ，满足 0 <= parents[i] <= n - 1
 * 4、parents[0] == -1
 * 5、parents 表示一棵合法的树。
 * 6、1 <= nums[i] <= 10^5
 * 7、nums[i] 互不相同。
 * 链接：https://leetcode.cn/problems/smallest-missing-genetic-value-in-each-subtree
"""

from typing import List
import bisect

#
# @lc app=leetcode.cn id=2003 lang=python3
#
# [2003] 每棵子树内缺失的最小基因值
#


# @lc code=start
class Solution:

    def smallestMissingValueSubtree1(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n
        if 1 not in nums:  # 不存在基因值为 1 的点
            return ans

        # 建树
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parents[i]].append(i)

        vis = set()

        def dfs(x: int) -> None:
            vis.add(nums[x])  # 标记基因值
            for son in g[x]:
                if nums[son] not in vis:
                    dfs(son)

        mex = 2  # 缺失的最小基因值
        node = nums.index(1)  # 出发点
        while node >= 0:
            dfs(node)
            while mex in vis:  # node 子树包含这个基因值
                mex += 1
            ans[node] = mex  # 缺失的最小基因值
            node = parents[node]  # 往上走
        return ans

    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [0] * n
        sub = [[] for _ in range(n)]
        for i in range(1, n):
            sub[parents[i]].append(i)

        def merge(arr, l, r):
            idx = bisect.bisect_left(arr, [l, r])
            b_m = False
            if idx > 0 and arr[idx - 1][1] == l - 1:
                b_m = True
                arr[idx - 1][1] = r
            if idx < len(arr) and arr[idx][0] == r + 1:
                b_m = True
                arr[idx][0] = l
            if idx > 0 and idx < len(arr) and arr[idx - 1][1] >= arr[idx][0]:
                arr[idx - 1][1] = arr[idx][1]
                del arr[idx]
            return b_m

        def dfs(root):
            ret = [[nums[root], nums[root]]]
            for child in sub[root]:
                s_arr = dfs(child)
                for l, r in s_arr:
                    b_m = merge(ret, l, r)
                    if not b_m:
                        bisect.insort(ret, [l, r])
            ans[root] = 1 if ret[0][0] != 1 else (ret[0][1] + 1)
            return ret

        dfs(0)
        return ans


# @lc code=end

if __name__ == '__main__':
    # [5,1,2,1,2]
    print(Solution().smallestMissingValueSubtree([-1, 0, 0, 0, 2], nums=[6, 4, 3, 2, 1]))
    # [5,1,1,1]
    print(Solution().smallestMissingValueSubtree([-1, 0, 0, 2], nums=[1, 2, 3, 4]))
    # [7,1,1,4,2,1]
    print(Solution().smallestMissingValueSubtree([-1, 0, 1, 0, 3, 3], nums=[5, 4, 6, 2, 1, 3]))
    # [1,1,1,1,1,1,1]
    print(Solution().smallestMissingValueSubtree([-1, 2, 3, 0, 2, 4, 1], nums=[2, 3, 4, 5, 6, 7, 8]))
