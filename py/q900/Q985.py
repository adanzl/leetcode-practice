"""
 * 给出一个整数数组 A 和一个查询数组 queries。
 * 对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中偶数值的和。
 * （此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）
 * 返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。
 * 提示：
 * 1、1 <= A.length <= 10000
 * 2、-10000 <= A[i] <= 10000
 * 3、1 <= queries.length <= 10000
 * 4、-10000 <= queries[i][0] <= 10000
 * 5、0 <= queries[i][1] < A.length
 * 链接：https://leetcode.cn/problems/sum-of-even-numbers-after-queries/
"""
from typing import *


class Solution:

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum([n for n in nums if n % 2 == 0])
        ans = []
        for v, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += v
            if nums[idx] % 2 == 0:
                s += nums[idx]
            ans.append(s)
        return ans


if __name__ == '__main__':
    # [8,6,2,4]
    print(Solution().sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
    # [0]
    print(Solution().sumEvenAfterQueries([1], [[4, 0]]))
