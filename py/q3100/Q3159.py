"""
 * 给你一个整数数组 nums ，一个整数数组 queries 和一个整数 x 。
 * 对于每个查询 queries[i] ，你需要找到 nums 中第 queries[i] 个 x 的位置，并返回它的下标。
 * 如果数组中 x 的出现次数少于 queries[i] ，该查询的答案为 -1 。
 * 请你返回一个整数数组 answer ，包含所有查询的答案。
 * 提示：
 * 1、1 <= nums.length, queries.length <= 10^5
 * 2、1 <= queries[i] <= 10^5
 * 3、1 <= nums[i], x <= 10^4
 * 链接：https://leetcode.cn/problems/find-occurrences-of-an-element-in-an-array
"""
from typing import List


class Solution:

    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        arr = [i for i, v in enumerate(nums) if v == x]
        return [arr[q - 1] if q <= len(arr) else -1 for q in queries]


if __name__ == '__main__':
    # [0,-1,2,-1]
    print(Solution().occurrencesOfElement([1, 3, 1, 7], queries=[1, 3, 2, 4], x=1))
    # [-1]
    print(Solution().occurrencesOfElement([1, 2, 3], queries=[10], x=5))
