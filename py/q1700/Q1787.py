"""
 * 给你一个整数数组 nums 和一个整数 k 。
 * 区间 [left, right]（left <= right）的 异或结果 是对下标位于 left 和 right（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：
 *  nums[left] XOR nums[left+1] XOR ... XOR nums[right] 。
 * 返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。
 * 提示：
 * 1、1 <= k <= nums.length <= 2000
 * 2、0 <= nums[i] < 2^10
 * 链接：https://leetcode.cn/problems/make-the-xor-of-all-segments-equal-to-zero/description/
"""
from collections import defaultdict
from itertools import accumulate


class Solution:

    def minChanges(self, nums: list[int], k: int) -> int:

        # Find the length of numbers
        n = len(nums)
        # Counts of numbers for each position 0, 1, ..., k-1
        counts = [defaultdict(int) for _ in range(k)]
        for i in range(n):
            counts[i % k][nums[i]] += 1
        # Find the maximum numbers we can keep for each position
        maxKeptPerPosition = [max(count.values()) for count in counts]
        # Create a suffix sum for O(1) lookup for how many numbers we can keep from i position onward
        suffix = list(accumulate(maxKeptPerPosition[::-1]))[::-1]
        # Case 1: Greedy approach
        maxKept = sum(maxKeptPerPosition) - min(maxKeptPerPosition)

        # Case 2: Search through all combinations with pruning
        def dfs(i, xor, kept):
            nonlocal maxKept
            # If the current position is k, we have reach the base case
            if i == k:
                # If the xor of all numbers is 0
                if xor == 0:
                    # Update the maximum numbers that we kept
                    maxKept = max(maxKept, kept)
                return
            # If processing the current position won't result in us keeping more numbers than before, end the search
            if kept + suffix[i] <= maxKept:
                return
            # Else, check all numbers at the current position
            for num, count in counts[i].items():
                dfs(i + 1, xor ^ num, kept + count)

        dfs(0, 0, 0)

        return n - maxKept


if __name__ == '__main__':
    # 3
    print(Solution().minChanges([1, 2, 4, 1, 2, 5, 1, 2, 6], 3))
    # 3
    print(Solution().minChanges([1, 2, 0, 3, 0], 1))
    # 3
    print(Solution().minChanges([3, 4, 5, 2, 1, 7, 3, 4, 7], 3))
