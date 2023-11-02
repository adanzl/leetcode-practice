"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 target 。
 * 返回和为 target 的 nums 子序列中，子序列 长度的最大值 。如果不存在和为 target 的子序列，返回 -1 。
 * 子序列 指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 1000
 * 3、1 <= target <= 1000
 * 链接：https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/
"""
from collections import defaultdict
from typing import List


class Solution:

    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dic = defaultdict(int)
        dic[0] = 0
        for num in nums:
            nd = defaultdict(int)
            for k, v in dic.items():
                nv = k + num
                if nv > target: continue
                nd[nv] = max(v + 1, dic.get(nv, 0))
            for k, v in nd.items():
                dic[k] = max(v, dic[k])
        return dic[target] if target in dic else -1


if __name__ == '__main__':
    # 3
    print(Solution().lengthOfLongestSubsequence([1, 2, 3, 4, 5], target=9))
    # 4
    print(Solution().lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], target=7))
    # -1
    print(Solution().lengthOfLongestSubsequence([1, 1, 5, 4, 5], target=3))
