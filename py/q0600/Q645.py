"""
 * 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
 * 给定一个数组 nums 代表了集合 S 发生错误后的结果。
 * 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
 * 提示：
 * 1、2 <= nums.length <= 10^4
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/set-mismatch/
"""
from typing import Counter, List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(list(range(1, 1 + len(nums))))
        c = Counter(nums)
        ans = []
        for k, v in c.items():
            if v > 1: ans.append(k)
        for v in s:
            if v not in c: ans.append(v)
        return ans


if __name__ == '__main__':
    # [2,3]
    print(Solution().findErrorNums([1, 2, 2, 4]))
    # [1,2]
    print(Solution().findErrorNums([1, 1]))