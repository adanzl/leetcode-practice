"""
 * 假设 力扣（LeetCode）即将开始 IPO 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 
 * 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
 * 给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。
 * 最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
 * 总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。
 * 答案保证在 32 位有符号整数范围内。
 * 提示：
 * 1、1 <= k <= 10^5
 * 2、0 <= w <= 10^9
 * 3、n == profits.length
 * 4、n == capital.length
 * 5、1 <= n <= 10^5
 * 6、0 <= profits[i] <= 10^4
 * 7、0 <= capital[i] <= 10^9
 * 链接：https://leetcode.cn/problems/ipo/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = []
        arr = sorted(zip(profits, capital), key=lambda x: x[1])
        cnt, idx = 0, 0
        while cnt < k:
            while idx < len(arr) and arr[idx][1] <= w:
                heappush(h, -arr[idx][0])
                idx += 1
            if h:
                w += -heappop(h)
                cnt += 1
            else:
                break
        return w


if __name__ == '__main__':
    # 4
    print(Solution().findMaximizedCapital(2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
    # 6
    print(Solution().findMaximizedCapital(3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
