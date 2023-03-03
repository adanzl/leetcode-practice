"""
 * 给你一个整数数组 gifts ，表示各堆礼物的数量。每一秒，你需要执行以下操作：
 * 1、选择礼物数量最多的那一堆。
 * 2、如果不止一堆都符合礼物数量最多，从中选择任一堆即可。
 * 3、选中的那一堆留下平方根数量的礼物（向下取整），取走其他的礼物。
 * 返回在 k 秒后剩下的礼物数量。
 * 提示：
 * 1、1 <= gifts.length <= 10^3
 * 2、1 <= gifts[i] <= 10^9
 * 3、1 <= k <= 10^3
 * 链接：https://leetcode.cn/problems/take-gifts-from-the-richest-pile/
"""
from heapq import heapify, heapreplace
import math
from typing import List


class Solution:

    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-v for v in gifts]
        heapify(h)
        while k > 0:
            heapreplace(h, int(-math.sqrt(-h[0])))
            k -= 1
        return -sum(h)


if __name__ == '__main__':
    # 29
    print(Solution().pickGifts([25, 64, 9, 4, 100], k=4))
    # 4
    print(Solution().pickGifts([1, 1, 1, 1], k=4))
