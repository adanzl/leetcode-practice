"""
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都为 n 。
 * 每次操作中，你可以选择交换 nums1 中任意两个下标处的值。操作的 开销 为两个下标的 和 。
 * 你的目标是对于所有的 0 <= i <= n - 1 ，都满足 nums1[i] != nums2[i] ，你可以进行 任意次 操作，请你返回达到这个目标的 最小 总代价。
 * 请你返回让 nums1 和 nums2 满足上述条件的 最小总代价 ，如果无法达成目标，返回 -1 。
 * 提示：
 * 1、n == nums1.length == nums2.length
 * 2、1 <= n <= 10^5
 * 3、1 <= nums1[i], nums2[i] <= n
 * 链接：https://leetcode.cn/problems/minimum-total-cost-to-make-arrays-unequal/
"""
from typing import Counter, List


class Solution:

    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        # 贪心思路，两两匹配交换一定大于其他形式
        n = len(nums1)
        arr = set()
        cnt = Counter()
        # 统计所有需要交换的元素，和出现最多次数的元素
        for i, (n1, n2) in enumerate(zip(nums1, nums2)):
            if n1 != n2: continue
            cnt[n2] += 1
            arr.add(i)
        if not cnt: return 0
        mc_v, mc_c = cnt.most_common(1)[0]
        # 如果需要的需要处理的元素的最高频次（mc_c）小于总交换个数的一半，则这些数据内部即可完成交换任务。
        # 否则需要从不需要交换的元素里找元素扩充交换区域，如果能使交换区域大于mc_c的2倍，则以此情况下的交换区域的成本为答案
        if mc_c <= len(arr) // 2: return sum(arr)
        for i in range(n):
            # 扩充交换区域，原交换区域内的不能扩展、nums1和nums2中对应下标和mc_v相同的不能扩展，因为扩展了也不能交换，无意义
            if i in arr or nums1[i] == mc_v or mc_v == nums2[i]: continue
            arr.add(i)
            if mc_c <= len(arr) // 2:  # 扩充够了就break
                break
        # 如果不可能扩充足够则返回-1
        return sum(arr) if mc_c <= len(arr) // 2 else -1


if __name__ == '__main__':
    # -1
    print(Solution().minimumTotalCost([1, 2, 2], [2, 1, 2]))
    # 10
    print(Solution().minimumTotalCost([2, 2, 2, 1, 3], [1, 2, 2, 3, 3]))
    # 28
    print(Solution().minimumTotalCost([2, 1, 2, 2, 1, 4, 1, 5], [2, 1, 2, 2, 1, 4, 1, 5]))
    # -1
    print(Solution().minimumTotalCost([1, 2, 2], [1, 2, 2]))
    # 10
    print(Solution().minimumTotalCost([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
