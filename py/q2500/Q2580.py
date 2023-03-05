"""
 * 给你一个二维整数数组 ranges ，其中 ranges[i] = [start_i, end_i] 表示 start_i 到 end_i 之间（包括二者）的所有整数都包含在第 i 个区间中。
 * 你需要将 ranges 分成 两个 组（可以为空），满足：
 * 1、每个区间只属于一个组。
 * 2、两个有 交集 的区间必须在 同一个 组内。
 * 如果两个区间有至少 一个 公共整数，那么这两个区间是 有交集 的。
 * 比方说，区间 [1, 3] 和 [2, 5] 有交集，因为 2 和 3 在两个区间中都被包含。
 * 请你返回将 ranges 划分成两个组的 总方案数 。由于答案可能很大，将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= ranges.length <= 10^5
 * 2、ranges[i].length == 2
 * 3、0 <= start_i <= end_i <= 10^9
 * 链接：https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/
"""
from typing import List


class Solution:

    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort()
        arr = []  # [l,r]
        for l, r in ranges:
            find = False
            for i in range(len(arr) - 1, -1, -1):
                if arr[i][1] >= l:
                    arr[i][1] = max(arr[i][1], r)
                    find = True
                    break
                else:
                    break
            if not find:
                arr.append([l, r])
        return (1 << len(arr)) % MOD


if __name__ == '__main__':
    # 16
    print(Solution().countWays([[0, 0], [8, 9], [12, 13], [1, 3]]))
    # 4
    print(Solution().countWays([[1, 3], [10, 20], [2, 5], [4, 8]]))
    # 2
    print(Solution().countWays([[6, 10], [5, 15]]))