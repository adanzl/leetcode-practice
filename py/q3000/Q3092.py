"""
 * 你需要在一个集合里动态记录 ID 的出现频率。
 * 给你两个长度都为 n 的整数数组 nums 和 freq ，nums 中每一个元素表示一个 ID ，
 * 对应的 freq 中的元素表示这个 ID 在集合中此次操作后需要增加或者减少的数目。
 * 1、增加 ID 的数目：如果 freq[i] 是正数，那么 freq[i] 个 ID 为 nums[i] 的元素在第 i 步操作后会添加到集合中。
 * 2、减少 ID 的数目：如果 freq[i] 是负数，那么 -freq[i] 个 ID 为 nums[i] 的元素在第 i 步操作后会从集合中删除。
 * 请你返回一个长度为 n 的数组 ans ，其中 ans[i] 表示第 i 步操作后出现频率最高的 ID 数目 ，如果在某次操作后集合为空，那么 ans[i] 为 0 。
 * 提示：
 * 1、1 <= nums.length == freq.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、-10^5 <= freq[i] <= 10^5
 * 4、freq[i] != 0
 * 5、输入保证任何操作后，集合中的元素出现次数不会为负数。
 * 链接：https://leetcode.cn/problems/most-frequent-ids/
"""
from heapq import heappop, heappush
from typing import Counter, List


class Solution:

    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        cnt = Counter()
        ans = []
        h = []
        for num, f in zip(nums, freq):
            cnt[num] += f
            heappush(h, [-cnt[num], num])
            while h and cnt[h[0][1]] != -h[0][0]:
                heappop(h)
            if h:
                ans.append(-h[0][0])
            else:
                ans.append(0)
        return ans


if __name__ == '__main__':
    # [3,3,2,2]
    print(Solution().mostFrequentIDs([2, 3, 2, 1], freq=[3, 2, -3, 1]))
    # [2,0,1]
    print(Solution().mostFrequentIDs([5, 5, 3], freq=[2, -2, 1]))
    #
    # print(Solution().mostFrequentIDs())
