"""
 * 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
 * 一个整数数组的 能量 定义为和 等于 k 的子序列的数目。
 * 请你返回 nums 中所有子序列的 能量和 。
 * 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= n <= 100
 * 2、1 <= nums[i] <= 10^4
 * 3、1 <= k <= 100
 * 链接：https://leetcode.cn/problems/find-the-sum-of-the-power-of-all-subsequences/
"""
from typing import Counter, List


class Solution:

    def sumOfPower(self, nums: List[int], k: int) -> int:
        tot = 0
        sm_cnt = Counter()
        for num in nums:
            cnt = Counter()
            cnt[num] = tot + 1
            tot += tot + 1
            for v, c in sm_cnt.items():
                if v + num <= k:
                    cnt[v + num] += c
                cnt[v] += c
            sm_cnt += cnt
        return sm_cnt[k] % (10**9 + 7)


if __name__ == '__main__':
    # 4
    print(Solution().sumOfPower([2, 3, 3], k=5))
    # 6
    print(Solution().sumOfPower([1, 2, 3], k=3))
    # 0
    print(Solution().sumOfPower([1, 2, 3], k=7))
