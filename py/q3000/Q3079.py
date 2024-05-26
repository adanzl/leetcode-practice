"""
 * 给你一个整数数组 nums ，数组中的元素都是 正 整数。
 * 定义一个加密函数 encrypt ，encrypt(x) 将一个整数 x 中 每一个 数位都用 x 中的 最大 数位替换。
 * 比方说 encrypt(523) = 555 且 encrypt(213) = 333 。
 * 请你返回数组中所有元素加密后的 和 。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/find-the-sum-of-encrypted-integers/
"""
from typing import List


class Solution:

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            num = list(str(num))
            for i in range(len(num)):
                num[i] = max(num)
            ans += int(''.join(num))
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().sumOfEncryptedInt([1, 2, 3]))
    # 66
    print(Solution().sumOfEncryptedInt([10, 21, 31]))
