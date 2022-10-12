"""
 * 给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。
 * 我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。
 * 返回数组能分成的最多块数量。
 * 提示:
 * 1、n == arr.length
 * 2、1 <= n <= 10
 * 3、0 <= arr[i] < n
 * 4、arr 中每个元素都 不同
 * 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted/
"""
from typing import List


class Solution:

    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        ss = sorted(zip(arr, range(len(arr))))
        n, mx = len(ss), 0
        for i, v in enumerate(ss):
            mx = max(mx, v[1])
            if mx == i: ans += 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().maxChunksToSorted([2, 0, 1]))
    # 4
    print(Solution().maxChunksToSorted([1, 0, 2, 3, 4]))
    # 2
    print(Solution().maxChunksToSorted([0, 1]))
    # 1
    print(Solution().maxChunksToSorted([0]))
    # 2
    print(Solution().maxChunksToSorted([0, 2, 1]))
    # 2
    print(Solution().maxChunksToSorted([1, 0, 2]))
    # 1
    print(Solution().maxChunksToSorted([4, 3, 2, 1, 0]))
