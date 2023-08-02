"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个正整数 k 。
 * 你可以对数组执行下述操作 任意次 ：
 * 从数组中选出长度为 k 的 任一 子数组，并将子数组中每个元素都 减去 1 。
 * 如果你可以使数组中的所有元素都等于 0 ，返回  true ；否则，返回 false 。
 * 子数组 是数组中的一个非空连续元素序列。
 * 提示：
 * 1、1 <= k <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/
"""
from typing import Deque, List


class Solution:

    def checkArray(self, nums: List[int], k: int) -> bool:
        r, n = 0, len(nums)
        while r < n and nums[r] == 0:
            r += 1
        q = Deque()
        while r < n:
            if len(q) < k:
                d = (nums[r] - nums[r - 1]) if r > 0 else nums[r]
                if d < 0:
                    return False
                if d > 0 or q: q.append(d)
                r += 1
                continue
            else:
                nums[r - 1] -= q.popleft()
                while q and q[0] == 0:
                    q.popleft()
        if len(q) == 0: return True
        if q: q.popleft()
        return len(q) == k - 1 and sum(q) == 0


if __name__ == '__main__':
    # False
    print(Solution().checkArray([1, 1, 1], 2))
    # True
    print(Solution().checkArray([60, 72, 87, 89, 63, 52, 64, 62, 31, 37, 57, 83, 98, 94, 92, 77, 94, 91, 87, 100, 91, 91, 50, 26], 4))
    # True
    print(Solution().checkArray([2, 2, 3, 1, 1, 0], k=3))
    # False
    print(Solution().checkArray([1, 3, 1, 1], k=2))
    # False
    print(Solution().checkArray([0, 45, 82, 98, 99], 4))
