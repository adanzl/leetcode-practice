"""
 * 给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
 * 换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），
 * （删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。
 * 注意，删除一个元素后，子数组 不能为空。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、-10^4 <= arr[i] <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/
"""
from typing import List


class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        ans = max(arr)
        n = len(arr)
        lsm, rsm = [arr[0]] * n, [arr[n - 1]] * n
        sm_l, sm_r = arr[0], arr[n - 1]
        for i in range(1, n):
            lsm[i] = sm_l = arr[i] if sm_l < 0 else (sm_l + arr[i])
            rsm[i] = sm_r = arr[n - 1 - i] if sm_r < 0 else (sm_r + arr[n - 1 - i])
            ans = max(ans, sm_r, sm_l)
        for i in range(1, n - 1):
            ans = max(ans, lsm[i - 1] + rsm[n - i - 2])
        return ans


if __name__ == '__main__':
    #  14
    print(Solution().maximumSum([-7, 6, 1, 2, 1, 4, -1]))
    #  3
    print(Solution().maximumSum([2, 1, -2, -5, -2]))
    #  4
    print(Solution().maximumSum([1, -2, 0, 3]))
    #  3
    print(Solution().maximumSum([1, -2, -2, 3]))
    #  -1
    print(Solution().maximumSum([-1, -1, -1, -1]))
