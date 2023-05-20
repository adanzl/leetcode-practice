"""
 * 给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。小扣有以下两种操作：
 * 升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
 * 蓄水：将全部水桶接满水，倒入各自对应的水缸
 * 每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。
 * 注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。
 * 提示：
 * 1、1 <= bucket.length == vat.length <= 100
 * 2、0 <= bucket[i], vat[i] <= 10^4
 * 链接：https://leetcode.cn/problems/o8SXZn/
"""
from heapq import heapify, heappop, heappush
import math
from typing import List


class Solution:

    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        h = [[-math.ceil(v / b) if b else -float('inf'), v, b] for b, v in zip(bucket, vat) if v]
        if not h: return 0
        heapify(h)
        ans = -h[0][0]
        pre = 0
        while True:
            c = -h[0][0]
            t = []
            while h and -h[0][0] == c:
                _, v, b = heappop(h)
                t.append([-math.ceil(v / (b + 1)), v, b + 1])
                pre += 1
            for _ in t:
                heappush(h, _)
            nv = pre + (-h[0][0] if h else 0)
            if nv > ans: break
            ans = nv
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().storeWater([100], [100]))
    # 4
    print(Solution().storeWater([1, 3], vat=[6, 8]))
    # 3
    print(Solution().storeWater([9, 0, 1], vat=[0, 2, 2]))
    # 0
    print(Solution().storeWater([0], [0]))
