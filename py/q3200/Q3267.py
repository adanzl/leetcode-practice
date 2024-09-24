"""
 * 注意：在这个问题中，操作次数增加为至多 两次 。
 * 给你一个正整数数组 nums 。
 * 如果我们执行以下操作 至多两次 可以让两个整数 x 和 y 相等，那么我们称这个数对是 近似相等 的：
 * 选择 x 或者 y  之一，将这个数字中的两个数位交换。
 * 请你返回 nums 中，下标 i 和 j 满足 i < j 且 nums[i] 和 nums[j] 近似相等 的数对数目。
 * 注意 ，执行操作后得到的整数可以有前导 0 。
 * 提示：
 * 1、2 <= nums.length <= 5000
 * 2、1 <= nums[i] < 10^7
 * 链接：https://leetcode.cn/problems/count-almost-equal-pairs-ii/description/
"""
from functools import cache
from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def countPairs(self, nums: List[int]) -> int:
        cnt = Counter()
        ans = 0
        nums.sort(reverse=True)

        @cache
        def get_change(num: int, nn: int):
            ret = set()
            for i in range(nn):
                for j in range(i + 1, nn):
                    val_i, val_j = num // 10**i % 10, num // 10**j % 10
                    val = num - 10**i * val_i + 10**j * val_i - 10**j * val_j + 10**i * val_j
                    ret.add(val)
            return ret

        for num in nums:
            ans += cnt[num]
            nn = len(str(num))
            s = get_change(num, nn)
            ss = set(s)
            ss.add(num)
            for v in s:
                val = get_change(v, nn)
                ss.update(val)
            for v in ss:
                cnt[v] += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().countPairs([1, 10, 100]))
    # 4
    print(Solution().countPairs([1023, 2310, 2130, 213]))
