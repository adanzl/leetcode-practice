"""
 * 设计一个数据结构，有效地找到给定子数组的 多数元素 。
 * 子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。
 * 实现 MajorityChecker 类:
 * 1、MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
 * 2、int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，如果不存在这样的元素则返回 -1。
 * 提示：
 * 1、1 <= arr.length <= 2 * 10^4
 * 2、1 <= arr[i] <= 2 * 10^4
 * 3、0 <= left <= right < arr.length
 * 4、threshold <= right - left + 1
 * 5、2 * threshold > right - left + 1
 * 6、调用 query 的次数最多为 10^4 
 * 链接：https://leetcode.cn/problems/online-majority-element-in-subarray/
"""
from bisect import bisect_left
from collections import defaultdict
from itertools import accumulate
from typing import List
"""
 * 解法 https://leetcode.cn/problems/online-majority-element-in-subarray/solution/by-424479543-8wxq/
 * 预处理复杂度O(logU n),查询复杂度O((logN+logU) q)
 * * U 是元素的范围1 <= arr[i] <= 20000，
 * * U <= 20000 , log2U<=15，我们只需要判断15位。
 * 查询的时候对每个位判断一下，用该位的前缀和，可以在O(1)时间获得此位在区间中1/0出现的次数。
 * 1).如果 此位中 1 出现的次数 >= threshold，则返回值val的这一位一定是 1
 * 2).如果 此位中 0 出现的次数 >= threshold，则返回值val的这一位一定是 0
 * 3).如果 1 和 0 出现的次数都 < threshold，直接返回-1
 * 4).如果15位均没有因为 (3) 退出，对得到的 val 二分判断一下：如果val在区间内的次数确实 >= threshold，返回val; 否则返回-1.
 * ps:如果U显著大于n,可以进行离散化，不过就算是1e9，无非从15n变成30n
"""


class MajorityChecker:

    def __init__(self, arr: List[int]):
        M = 15
        self.A = [[]] * M
        self.mp = defaultdict(list)
        for i, x in enumerate(arr):
            self.mp[x].append(i)
        for i in range(M):
            self.A[i] = [0] + list(accumulate(x >> i & 1 for x in arr))

    def query(self, left: int, right: int, threshold: int) -> int:
        mp = self.mp
        val = 0
        right += 1
        for i, a in enumerate(self.A):
            one = a[right] - a[left]
            if one >= threshold:  # (1)
                val |= 1 << i
            elif right - left - one < threshold:  # (3)
                return -1
            # else (2)
        return [val, -1][bisect_left(mp[val], right) - bisect_left(mp[val], left) < threshold]


if __name__ == '__main__':
    #
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(obj.query(0, 5, 4))  # 1
    print(obj.query(0, 3, 3))  # -1
    print(obj.query(2, 3, 2))  # 2
