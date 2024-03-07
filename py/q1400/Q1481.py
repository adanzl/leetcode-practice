"""
 * 给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、1 <= arr[i] <= 10^9
 * 3、0 <= k <= arr.length
 * 链接：https://leetcode.cn/problems/least-number-of-unique-integers-after-k-removals/
"""
from collections import Counter
from typing import List


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ss = sorted([[c, v] for v, c in Counter(arr).items()])
        tot = 0
        for i, (c, v) in enumerate(ss):
            if tot + c > k:
                return len(ss) - i
            else:
                tot += c
        return 0


if __name__ == '__main__':
    # 1
    print(Solution().findLeastNumOfUniqueInts([5, 5, 4], k=1))
    # 2
    print(Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], k=3))
