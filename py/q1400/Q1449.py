"""
 * 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
 * 1、给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
 * 2、总成本必须恰好等于 target 。
 * 3、添加的数位中没有数字 0 。
 * 由于答案可能会很大，请你以字符串形式返回。
 * 如果按照上述要求无法得到任何整数，请你返回 "0" 。
 * 提示：
 * 1、cost.length == 9
 * 2、1 <= cost[i] <= 5000
 * 3、1 <= target <= 5000
 * 链接：https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/
"""
from typing import List


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:

        def cmp(arr1, arr2):
            if arr1 == arr2: return 0
            if arr2 is None: return 1
            if arr1 is None: return -1
            l1, l2 = len(arr1), len(arr2)
            return (l1 - l2) if l1 != l2 else (1 if arr1 > arr2 else -1)

        dp = [[]] + [None] * target
        for i in range(target):
            for l, c in enumerate(cost):  # num-cost
                l += 1
                if i + c > target: continue
                if dp[i] is None: continue
                nv = (dp[i] or [])[:]
                nv.append(str(l))
                nv.sort(reverse=True)
                if cmp(nv, dp[i + c]) > 0:
                    dp[i + c] = nv

        return ''.join(dp[target]) if dp[target] else '0'  # type: ignore


if __name__ == '__main__':
    # "7772"
    print(Solution().largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], target=9))
    # "85"
    print(Solution().largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], target=12))
    # "0"
    print(Solution().largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], target=5))
    # "32211"
    print(Solution().largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], target=47))
    #
    # print(Solution().largestNumber())