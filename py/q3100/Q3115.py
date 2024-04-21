"""
 * 给你一个整数数组 nums。
 * 返回两个（不一定不同的）素数在 nums 中 下标 的 最大距离。
 * 提示：
 * 1、1 <= nums.length <= 3 * 10^5
 * 2、1 <= nums[i] <= 100
 * 3、输入保证 nums 中至少有一个素数。
 * 链接：https://leetcode.cn/problems/maximum-prime-difference/
"""
from typing import List

LIMIT = 10**2 + 5
prime_list = []
b_composite = [False] * LIMIT
b_composite[1] = True  # 这里 1 被算为合数


def build_prime_list():
    # 线性筛选质数
    for i in range(2, LIMIT):
        if not b_composite[i]:
            prime_list.append(i)
        for prime in prime_list:
            nx = prime * i
            if nx < LIMIT:
                b_composite[nx] = True
            else:
                break


build_prime_list()


class Solution:

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        ids = []
        for i, num in enumerate(nums):
            if not b_composite[num]:
                ids.append(i)
        return ids[-1] - ids[0]


if __name__ == '__main__':
    # 3
    print(Solution().maximumPrimeDifference([4, 2, 9, 5, 3]))
    # 0
    print(Solution().maximumPrimeDifference([4, 8, 2, 8]))
    #
    # print(Solution().maximumPrimeDifference())
