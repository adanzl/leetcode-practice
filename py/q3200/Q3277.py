"""
 * 给你一个由 n 个整数组成的数组 nums，以及一个大小为 q 的二维整数数组 queries，其中 queries[i] = [l_i, r_i]。
 * 对于每一个查询，你需要找出 nums[l_i..r_i] 中任意 子数组 的 最大异或值。
 * 1、数组的异或值 需要对数组 a 反复执行以下操作，直到只剩一个元素，剩下的那个元素就是 异或值：
 * 2、对于除最后一个下标以外的所有下标 i，同时将 a[i] 替换为 a[i] XOR a[i + 1] 。
 * 移除数组的最后一个元素。
 * 返回一个大小为 q 的数组 answer，其中 answer[i] 表示查询 i 的答案。
 * 提示：
 * 1、1 <= n == nums.length <= 2000
 * 2、0 <= nums[i] <= 2^31 - 1
 * 3、1 <= q == queries.length <= 10^5
 * 4、queries[i].length == 2
 * 5、queries[i] = [l_i, r_i]
 * 6、0 <= l_i <= r_i <= n - 1
 * 链接：https://leetcode.cn/problems/maximum-xor-score-subarray-queries/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)  # 2000
        f = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]
        # f[i][j] = f[i-1][j] ^ f[i][j-1]
        for i in range(n - 1, -1, -1):
            mx[i][i] = f[i][i] = nums[i]
            for j in range(i + 1, n):
                f[i][j] = f[i + 1][j] ^ f[i][j - 1]
                mx[i][j] = max(f[i][j], mx[i][j - 1], mx[i + 1][j])
        return [mx[l][r] for l, r in queries]


if __name__ == '__main__':
    # [12,60,60]
    print(Solution().maximumSubarrayXor([2, 8, 4, 32, 16, 1], queries=[[0, 2], [1, 4], [0, 5]]))
    # [7,14,11,14,5]
    print(Solution().maximumSubarrayXor([0, 7, 3, 2, 8, 5, 1], queries=[[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]]))
