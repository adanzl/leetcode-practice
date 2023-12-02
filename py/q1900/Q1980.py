"""
 * 给你一个字符串数组 nums ，该数组由 n 个 互不相同 的二进制字符串组成，且每个字符串长度都是 n 。
 * 请你找出并返回一个长度为 n 且 没有出现 在 nums 中的二进制字符串。如果存在多种答案，只需返回 任意一个 即可。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 16
 * 3、nums[i].length == n
 * 4、nums[i] 为 '0' 或 '1'
 * 5、nums 中的所有字符串 互不相同
 * 链接：https://leetcode.cn/problems/find-unique-binary-string
"""

from typing import List

#
# @lc app=leetcode.cn id=1980 lang=python3
#
# [1980] 找出不同的二进制字符串
#


# @lc code=start
class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        arr = set([i for i in range(1<<n)])
        for num in nums:
            arr.discard(int(num, 2))
        return bin(list(arr)[0])[2:].zfill(n)


# @lc code=end

if __name__ == '__main__':
    # "11"
    print(Solution().findDifferentBinaryString(["01", "10"]))
    # "11"
    print(Solution().findDifferentBinaryString(["00", "01"]))
    # "101"
    print(Solution().findDifferentBinaryString(["111", "011", "001"]))
