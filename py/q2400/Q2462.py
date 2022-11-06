"""
 * 给你一个下标从 0 开始的整数数组 costs ，其中 costs[i] 是雇佣第 i 位工人的代价。
 * 同时给你两个整数 k 和 candidates 。我们想根据以下规则恰好雇佣 k 位工人：
 * 1、总共进行 k 轮雇佣，且每一轮恰好雇佣一位工人。
 * 2、在每一轮雇佣中，从最前面 candidates 和最后面 candidates 人中选出代价最小的一位工人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
 * 3、比方说，costs = [3,2,7,7,1,2] 且 candidates = 2 ，第一轮雇佣中，我们选择第 4 位工人，因为他的代价最小 [3,2,7,7,1,2] 。
 * 4、第二轮雇佣，我们选择第 1 位工人，因为他们的代价与第 4 位工人一样都是最小代价，而且下标更小，[3,2,7,7,2] 。注意每一轮雇佣后，剩余工人的下标可能会发生变化。
 * 5、如果剩余员工数目不足 candidates 人，那么下一轮雇佣他们中代价最小的一人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
 * 6、一位工人只能被选择一次。
 * 返回雇佣恰好 k 位工人的总代价。
 * 提示：
 * 1、1 <= costs.length <= 10^5
 * 2、1 <= costs[i] <= 10^5
 * 3、1 <= k, candidates <= costs.length
 * 链接：https://leetcode.cn/problems/total-cost-to-hire-k-workers/
"""
from heapq import heapify, heapreplace
from typing import List


class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cmp = lambda x: (costs[x], x)
        n = len(costs)
        ans = 0
        if candidates * 2 < n:
            il, ir = candidates, n - candidates - 1
            lq, rq = costs[:candidates], costs[-candidates:]
            heapify(lq)
            heapify(rq)
            while k and il <= ir:
                if lq[0] <= rq[0]:
                    ans += heapreplace(lq, costs[il])
                    il += 1
                else:
                    ans += heapreplace(rq, costs[ir])
                    ir -= 1
                k -= 1
            costs = lq + rq
        costs.sort()
        return ans + sum(costs[:k])


if __name__ == '__main__':
    # 4
    print(Solution().totalCost([1, 2, 4, 1], k=3, candidates=3))
    # 11
    print(Solution().totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
