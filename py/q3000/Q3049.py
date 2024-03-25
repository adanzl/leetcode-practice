"""
 * 给你两个下标从 1 开始的整数数组 nums 和 changeIndices ，数组的长度分别为 n 和 m 。
 * 一开始，nums 中所有下标都是未标记的，你的任务是标记 nums 中 所有 下标。
 * 从第 1 秒到第 m 秒（包括 第 m 秒），对于每一秒 s ，你可以执行以下操作 之一 ：
 * 1、选择范围 [1, n] 中的一个下标 i ，并且将 nums[i] 减少 1 。
 * 2、将 nums[changeIndices[s]] 设置成任意的 非负 整数。
 * 3、选择范围 [1, n] 中的一个下标 i ， 满足 nums[i] 等于 0, 并 标记 下标 i 。
 * 4、什么也不做。
 * 请你返回范围 [1, m] 中的一个整数，表示最优操作下，标记 nums 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 -1 。
 * 提示：
 * 1、1 <= n == nums.length <= 5000
 * 2、0 <= nums[i] <= 10^9
 * 3、1 <= m == changeIndices.length <= 5000
 * 4、1 <= changeIndices[i] <= n
 * 链接：https://leetcode.cn/problems/earliest-second-to-mark-indices-ii/
"""
from bisect import bisect_left
from heapq import heappop, heappush
from typing import List


class Solution:

    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        first_t = [-1] * n
        for t in range(m - 1, -1, -1):
            first_t[changeIndices[t] - 1] = t

        def check(mx: int) -> bool:
            cnt = 0
            done = [False] * n
            h = []
            for t in range(mx, -1, -1):
                i = changeIndices[t] - 1
                v = nums[i]
                if v <= 1 or first_t[i] != t:
                    cnt += 1  # 留着给前面，用来减一/标记
                    continue
                if cnt == 0:
                    if not h or v <= h[0][0]:
                        cnt += 1  # 留着给前面，用来减一/标记
                        continue
                    done[heappop(h)[1]] = False
                    cnt += 2  # 反悔：一次置 0，一次标记
                done[i] = True
                cnt -= 1  # nums[i] 置 0，然后消耗一次标记的时间
                heappush(h, (v, i))

            for i, b in enumerate(done):
                if not b:
                    cnt -= nums[i] + 1  # 减一的时间，以及标记的时间
            return cnt >= 0

        ans = bisect_left(range(m), True, key=check)
        return -1 if ans == m else ans + 1


if __name__ == '__main__':
    # 13
    print(Solution().earliestSecondToMarkIndices([5, 3, 2, 0, 3, 5], [4, 3, 6, 5, 6, 5, 3, 6, 4, 1, 2, 3, 6, 1]))
    # -1
    print(Solution().earliestSecondToMarkIndices([1, 2, 3], changeIndices=[1, 2, 3]))
    # 4
    print(Solution().earliestSecondToMarkIndices([0, 2], [1, 1, 2, 2, 1]))
    # 7
    print(Solution().earliestSecondToMarkIndices([0, 0, 1, 2], changeIndices=[1, 2, 1, 2, 1, 2, 1, 2]))
    # 6
    print(Solution().earliestSecondToMarkIndices([3, 2, 3], changeIndices=[1, 3, 2, 2, 2, 2, 3]))
