"""
 * 有 n 个人排成一个队列，从左到右 编号为 0 到 n - 1 。给你以一个整数数组 heights ，每个整数 互不相同，heights[i] 表示第 i 个人的高度。
 * 一个人能 看到 他右边另一个人的条件是这两人之间的所有人都比他们两人 矮 。
 * 更正式的，第 i 个人能看到第 j 个人的条件是 i < j 且 min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]) 。
 * 请你返回一个长度为 n 的数组 answer ，其中 answer[i] 是第 i 个人在他右侧队列中能 看到 的 人数 。
 * 提示：
 * 1、n == heights.length
 * 2、1 <= n <= 10^5
 * 3、1 <= heights[i] <= 10^5
 * 4、heights 中所有数 互不相同 。
 * 链接：https://leetcode.cn/problems/number-of-visible-people-in-a-queue/
"""
from typing import List


class Solution:

    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        s = [n - 1]
        for i in range(n - 2, -1, -1):
            while s and heights[s[-1]] < heights[i]:
                s.pop()
                ans[i] += 1
            if s: ans[i] += 1
            s.append(i)
        return ans


if __name__ == '__main__':
    # [3,1,2,1,1,0]
    print(Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]))
    # [4,1,1,1,0]
    print(Solution().canSeePersonsCount([5, 1, 2, 3, 10]))
