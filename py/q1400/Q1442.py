"""
 * 给你一个整数数组 arr 。
 * 现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。
 * a 和 b 定义如下：
 * 1、a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
 * 2、b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
 * 注意：^ 表示 按位异或 操作。
 * 请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。
 * 提示：
 * 1、1 <= arr.length <= 300
 * 2、1 <= arr[i] <= 10^8
 * 链接：https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=1442 lang=python3
#
# [1442] 形成两个异或相等数组的三元组数目
#


# @lc code=start
class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for j in range(1, len(arr)):
            cnt = Counter()
            a = 0
            for i in range(j - 1, -1, -1):
                a ^= arr[i]
                cnt[a] += 1
            b = 0
            for k in range(j, len(arr)):
                b ^= arr[k]
                ans += cnt[b]
        return ans


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().countTriplets([2, 3, 1, 6, 7]))
    # 10
    print(Solution().countTriplets([1, 1, 1, 1, 1]))
    # 0
    print(Solution().countTriplets([2, 3]))
    # 3
    print(Solution().countTriplets([1, 3, 5, 7, 9]))
    # 8
    print(Solution().countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))
