"""
 * 给你 n 个盒子，每个盒子的格式为 [status, candies, keys, containedBoxes] ，其中：
 * 1、状态字 status[i]：整数，如果 box[i] 是开的，那么是 1 ，否则是 0 。
 * 2、糖果数 candies[i]: 整数，表示 box[i] 中糖果的数目。
 * 3、钥匙 keys[i]：数组，表示你打开 box[i] 后，可以得到一些盒子的钥匙，每个元素分别为该钥匙对应盒子的下标。
 * 4、内含的盒子 containedBoxes[i]：整数，表示放在 box[i] 里的盒子所对应的下标。
 * 给你一个 initialBoxes 数组，表示你现在得到的盒子，你可以获得里面的糖果，
 * 也可以用盒子里的钥匙打开新的盒子，还可以继续探索从这个盒子里找到的其他盒子。
 * 请你按照上述规则，返回可以获得糖果的 最大数目 。
 * 提示：
 * 1、1 <= status.length <= 1000
 * 2、status.length == candies.length == keys.length == containedBoxes.length == n
 * 3、status[i] 要么是 0 要么是 1 。
 * 4、1 <= candies[i] <= 1000
 * 5、0 <= keys[i].length <= status.length
 * 6、0 <= keys[i][j] < status.length
 * 7、keys[i] 中的值都是互不相同的。
 * 8、0 <= containedBoxes[i].length <= status.length
 * 9、0 <= containedBoxes[i][j] < status.length
 * 10、containedBoxes[i] 中的值都是互不相同的。
 * 11、每个盒子最多被一个盒子包含。
 * 12、0 <= initialBoxes.length <= status.length
 * 13、0 <= initialBoxes[i] < status.length
 * 链接：https://leetcode.cn/problems/maximum-candies-you-can-get-from-boxes/
"""

from typing import List

#
# @lc app=leetcode.cn id=1298 lang=python3
#
# [1298] 你能从盒子里获得的最大糖果数
#


# @lc code=start
class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = []
        ans = 0
        k = set()
        locks = set()
        for b in initialBoxes:
            if status[b]: q.append(b)
            else: locks.add(b)
        while q:
            box = q.pop(0)
            ans += candies[box]
            for b in containedBoxes[box]:
                if status[b] == 1 or b in k:
                    q.append(b)
                else:
                    locks.add(b)
            for key in keys[box]:
                k.add(key)
                if key in locks:
                    locks.remove(key)
                    q.append(key)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().maxCandies([1, 0, 1, 0], [7, 5, 4, 100], [[], [], [], []], [[1, 2], [3], [], []], [1, 2]))
    # 10
    print(Solution().maxCandies([1, 0, 0, 0], [1, 2, 3, 4], [[1, 2], [3], [], []], [[2], [3], [1], []], [0]))
    # 6
    print(Solution().maxCandies([1, 0, 0, 0, 0, 0], candies=[1, 1, 1, 1, 1, 1], keys=[[1, 2, 3, 4, 5], [], [], [], [], []], containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []], initialBoxes=[0]))
    # 16
    print(Solution().maxCandies([1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []], containedBoxes=[[1, 2], [3], [], []], initialBoxes=[0]))
    # 1
    print(Solution().maxCandies([1, 1, 1], candies=[100, 1, 100], keys=[[], [0, 2], []], containedBoxes=[[], [], []], initialBoxes=[1]))
    # 0
    print(Solution().maxCandies([1], candies=[100], keys=[[]], containedBoxes=[[]], initialBoxes=[]))
    # 7
    print(Solution().maxCandies([1, 1, 1], candies=[2, 3, 2], keys=[[], [], []], containedBoxes=[[], [], []], initialBoxes=[2, 1, 0]))
