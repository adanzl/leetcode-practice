"""
 * 给你一个下标从 0 开始、长度为 n 的数组 nums 。一开始，所有元素都是 未染色 （值为 0 ）的。
 * 给你一个二维整数数组 queries ，其中 queries[i] = [index_i, color_i] 。
 * 对于每个操作，你需要将数组 nums 中下标为 index_i 的格子染色为 color_i 。
 * 请你返回一个长度与 queries 相等的数组 answer ，其中 answer[i]是前 i 个操作 之后 ，相邻元素颜色相同的数目。
 * 更正式的，answer[i] 是执行完前 i 个操作后，0 <= j < n - 1 的下标 j 中，满足 nums[j] == nums[j + 1] 且 nums[j] != 0 的数目。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= queries.length <= 10^5
 * 3、queries[i].length == 2
 * 4、0 <= index_i <= n - 1
 * 5、1 <= color_i <= 10^5
 * 链接：https://leetcode.cn/problems/number-of-adjacent-elements-with-the-same-color/
"""
from typing import List


class Solution:

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        arr = [0] * n
        for i, c in queries:
            v = 0 if len(ans) == 0 else ans[-1]
            if i > 0:
                if arr[i - 1] == arr[i] and arr[i]:
                    v -= 1
                if arr[i - 1] == c:
                    v += 1
            if i < n - 1:
                if arr[i + 1] == arr[i] and arr[i]:
                    v -= 1
                if arr[i + 1] == c:
                    v += 1
            arr[i] = c
            ans.append(max(0, v))
        return ans


if __name__ == '__main__':
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(Solution().colorTheArray(8, queries=[[6, 2], [2, 1], [0, 6], [0, 1], [0, 4], [0, 1], [5, 7], [5, 3], [7, 6], [6, 7], [0, 4], [4, 6], [4, 2], [3, 7], [4, 4], [5, 1]]))
    # [0,1,1,0,2]
    print(Solution().colorTheArray(4, queries=[[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]))
    # [0]
    print(Solution().colorTheArray(1, queries=[[0, 100000]]))
