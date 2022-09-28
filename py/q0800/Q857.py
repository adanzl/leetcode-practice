from typing import *
from heapq import *
"""
 * 有 n 名工人。 给定两个数组 quality 和 wage ，其中，quality[i] 表示第 i 名工人的工作质量，其最低期望工资为 wage[i] 。
 * 现在我们想雇佣 k 名工人组成一个工资组。在雇佣 一组 k 名工人时，我们必须按照下述规则向他们支付工资：
 * 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
 * 工资组中的每名工人至少应当得到他们的最低期望工资。
 * 给定整数 k ，返回 组成满足上述条件的付费群体所需的最小金额 。在实际答案的 10^-5 以内的答案将被接受。。
 * 提示：
 * 1、n == quality.length == wage.length
 * 2、1 <= k <= n <= 10^4
 * 3、1 <= quality[i], wage[i] <= 10^4
 * 链接：https://leetcode.cn/problems/minimum-cost-to-hire-k-workers
"""


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        arr = sorted([[q, w / q] for q, w in zip(quality, wage)], key=lambda x: x[1])
        h = []
        n = len(arr)
        sm = 0
        for i in range(k):
            heappush(h, -arr[i][0])
            sm += arr[i][0]
        ans = sm * arr[k - 1][1]
        for q, r in arr[k:]:
            if q < -h[0]:
                sm += q + heapreplace(h, -q)
                ans = min(ans, sm * r)
        return ans


if __name__ == '__main__':
    # 25.2
    print(Solution().mincostToHireWorkers([4, 5], [8, 14], 2))
    # 105.00
    print(Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))
    # 30.66
    print(Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3))
