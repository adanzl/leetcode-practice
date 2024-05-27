"""
 * 给你一个长度为 n 下标从 0 开始的正整数数组 nums 。
 * 同时给你一个长度为 m 的二维操作数组 queries ，其中 queries[i] = [index_i, k_i] 。
 * 一开始，数组中的所有元素都 未标记 。
 * 你需要依次对数组执行 m 次操作，第 i 次操作中，你需要执行：
 * 如果下标 index_i 对应的元素还没标记，那么标记这个元素。
 * 然后标记 k_i 个数组中还没有标记的 最小 元素。如果有元素的值相等，那么优先标记它们中下标较小的。
 * 如果少于 k_i 个未标记元素存在，那么将它们全部标记。
 * 请你返回一个长度为 m 的数组 answer ，其中 answer[i]是第 i 次操作后数组中还没标记元素的 和 。
 * 提示：
 * 1、n == nums.length
 * 2、m == queries.length
 * 3、1 <= m <= n <= 10^5
 * 4、1 <= n <= 10^5
 * 5、queries[i].length == 2
 * 6、0 <= index_i, k_i <= n - 1
 * 链接：https://leetcode.cn/problems/mark-elements-on-array-by-performing-queries/
"""
from typing import List


class Solution:

    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sm = sum(nums)
        arr = sorted([[num, i] for i, num in enumerate(nums)])
        mark = set()
        idx = 0
        for ii, k in queries:
            if ii not in mark:
                mark.add(ii)
                sm -= nums[ii]
            i = 0
            while idx < len(arr) and i < k:
                if not arr[idx][1] in mark:
                    i += 1
                    sm -= arr[idx][0]
                    mark.add(arr[idx][1])
                idx += 1
            ans.append(sm)
        return ans


if __name__ == '__main__':
    # [7]
    print(Solution().unmarkedSumArray([1, 4, 2, 3], queries=[[0, 1]]))
    # [8,3,0]
    print(Solution().unmarkedSumArray([1, 2, 2, 1, 2, 3, 1], queries=[[1, 2], [3, 3], [4, 2]]))
    #
    # print(Solution().unmarkedSumArray())
