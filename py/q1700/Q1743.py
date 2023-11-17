"""
 * 存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。
 * 给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。
 * 题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，
 * 存在形式可能是 [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。
 * 返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。
 * 提示：
 * 1、nums.length == n
 * 2、adjacentPairs.length == n - 1
 * 3、adjacentPairs[i].length == 2
 * 4、2 <= n <= 10^5
 * 5、-10^5 <= nums[i], ui, vi <= 10^5
 * 6、题目数据保证存在一些以 adjacentPairs 作为元素对的数组 nums
 * 链接：https://leetcode.cn/problems/restore-the-array-from-adjacent-pairs/
"""

from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=1743 lang=python3
#
# [1743] 从相邻元素对还原数组
#


# @lc code=start
class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbor = defaultdict(list)
        ans = []
        for u, v in adjacentPairs:
            neighbor[u].append(v)
            neighbor[v].append(u)
        lst, fa = -1, -1
        for k, v in neighbor.items():
            if len(v) == 1:
                ans.append(k)
                lst = k
                break
        while lst != None:
            for nx in neighbor[lst]:
                if nx == fa: continue
                ans.append(nx)
                if len(neighbor[nx]) == 1:
                    lst = None
                else:
                    fa = lst
                    lst = nx
                break
        return ans


# @lc code=end

if __name__ == '__main__':
    # [1,2,3,4]
    print(Solution().restoreArray([[2, 1], [3, 4], [3, 2]]))
    # [-2,4,1,-3]
    print(Solution().restoreArray([[4, -2], [1, 4], [-3, 1]]))
    # [100000,-100000]
    print(Solution().restoreArray([[100000, -100000]]))
