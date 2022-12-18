"""
 * 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
 * 如果气温在这之后都不会升高，请在该位置用 0 来代替。
 * 提示：
 * 1、1 <= temperatures.length <= 10^5
 * 2、30 <= temperatures[i] <= 100
 * 链接：https://leetcode.cn/problems/daily-temperatures/
"""
from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        q = []
        for i, t in enumerate(temperatures):
            while q and temperatures[q[-1]] < t:
                idx = q.pop()
                ans[idx] = i - idx
            q.append(i)
        return ans


if __name__ == '__main__':
    # [1,1,4,2,1,1,0,0]
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # [1,1,1,0]
    print(Solution().dailyTemperatures([30, 40, 50, 60]))
    # [1,1,0]
    print(Solution().dailyTemperatures([30, 60, 90]))
