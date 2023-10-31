"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * nums 中的 K-or 是一个满足以下条件的非负整数：
 * 只有在 nums 中，至少存在 k 个元素的第 i 位值为 1 ，那么 K-or 中的第 i 位的值才是 1 。
 * 返回 nums 的 K-or 值。
 * 注意 ：对于整数 x ，如果 (2^i AND x) == 2^i ，则 x 中的第 i 位值为 1 ，其中 AND 为按位与运算符。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、0 <= nums[i] < 2^31
 * 3、1 <= k <= nums.length
 * 链接：https://leetcode.cn/problems/find-the-k-or-of-an-array/
"""
from typing import List


class Solution:

    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = [0] * 32
        for i in range(32):
            for num in nums:
                cnt[i] += bool(num & (1 << i))
        ans = 0
        for i in range(32):
            if cnt[i] >= k:
                ans |= 1 << i
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().findKOr([7, 12, 9, 8, 9, 15], k=4))
    # 0
    print(Solution().findKOr([2, 12, 1, 11, 4, 5], k=6))
    # 15
    print(Solution().findKOr([10, 8, 5, 9, 11, 6, 8], k=1))
