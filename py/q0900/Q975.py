"""
 * 给定一个整数数组 A，你可以从某一起始索引出发，跳跃一定次数。在你跳跃的过程中，第 1、3、5... 次跳跃称为奇数跳跃，而第 2、4、6... 次跳跃称为偶数跳跃。
 * 你可以按以下方式从索引 i 向后跳转到索引 j（其中 i < j）：
 * 1、在进行奇数跳跃时（如，第 1，3，5... 次跳跃），你将会跳到索引 j，使得 A[i] <= A[j]，A[j] 是可能的最小值。如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
 * 2、在进行偶数跳跃时（如，第 2，4，6... 次跳跃），你将会跳到索引 j，使得 A[i] >= A[j]，A[j] 是可能的最大值。如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
 * 3、（对于某些索引 i，可能无法进行合乎要求的跳跃。）
 * 如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 A.length - 1），那么该索引就会被认为是好的起始索引。
 * 返回好的起始索引的数量。
 * 提示：
 * 1、1 <= A.length <= 20000
 * 2、0 <= A[i] < 100000
 * 链接：https://leetcode.cn/problems/odd-even-jump/
"""
from functools import lru_cache
from typing import List


class Solution:

    def oddEvenJumps(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)

        # 单调栈
        def make(arr_idx):
            ans = [None] * n
            stack = []  # invariant: stack is decreasing
            for i in arr_idx:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        next_odd = make(sorted(range(n), key=lambda i: (arr[i], i)))  # 值递增，索引递增
        next_even = make(sorted(range(n), key=lambda i: (-arr[i], i)))  # 值递减，索引递增

        @lru_cache
        def dfs(idx, odd: bool):
            if idx == n - 1: return True
            pos = next_odd[idx] if odd else next_even[idx]
            if pos is None:
                return False
            return dfs(pos, not odd)

        for i in range(n):
            if dfs(i, True): ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().oddEvenJumps([5, 1, 3, 4, 2]))
    # 2
    print(Solution().oddEvenJumps([10, 13, 12, 14, 15]))
    # 3
    print(Solution().oddEvenJumps([2, 3, 1, 1, 4]))
