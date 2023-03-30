"""
 * 给你一个下标从 0 开始的整数数组 nums 。你可以将 nums 中的元素按 任意顺序 重排（包括给定顺序）。
 * 令 prefix 为一个数组，它包含了 nums 重新排列后的前缀和。换句话说，prefix[i] 是 nums 重新排列后下标从 0 到 i 的元素之和。nums 的 分数 是 prefix 数组中正整数的个数。
 * 返回可以得到的最大分数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^6 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score/
"""
from typing import List


class Solution:

    def maxScore(self, nums: List[int]) -> int:
        p_arr, n_arr = [], []
        for num in nums:
            if num > 0:
                p_arr.append(num)
            else:
                n_arr.append(num)
        p_arr.sort(reverse=True)
        n_arr.sort(reverse=True)
        if not p_arr:
            return 0
        i_p, i_n = 1, 0
        sm = p_arr[0]
        ans = 1
        while i_p < len(p_arr) and i_n < len(n_arr) and sm > 0:
            if sm + n_arr[i_n] > 0:
                sm += n_arr[i_n]
                i_n += 1
            else:
                sm += p_arr[i_p]
                i_p += 1
            ans += 1
        if i_p < len(p_arr):
            ans += len(p_arr) - i_p
        while i_n < len(n_arr) and sm > 0:
            sm += n_arr[i_n]
            i_n += 1
            if sm > 0: ans += 1
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().maxScore([2, -1, 0, 1, -3, 3, -3]))
    # 5
    print(Solution().maxScore([-32495, -144584, -270506, -394309, -298138, 922535]))
    # 1
    print(Solution().maxScore([1000000]))
    # 0
    print(Solution().maxScore([0, 0, 0, 0, 0, 0]))
    # 20
    print(Solution().maxScore([-687767, -860350, 950296, 52109, 510127, 545329, -291223, -966728, 852403, 828596, 456730, -483632, -529386, 356766, 147293, 572374, 243605, 931468, 641668, 494446]))
    # 0
    print(Solution().maxScore([-2, -3, 0]))
