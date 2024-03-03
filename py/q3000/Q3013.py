"""
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums 和两个 正 整数 k 和 dist 。
 * 一个数组的 代价 是数组中的 第一个 元素。比方说，[1,2,3] 的代价为 1 ，[3,4,1] 的代价为 3 。
 * 你需要将 nums 分割成 k 个 连续且互不相交 的子数组，满足 第二 个子数组与第 k 个子数组中第一个元素的下标距离 不超过 dist 。
 * 换句话说，如果你将 nums 分割成子数组 nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)] ，
 * 那么它需要满足 ik-1 - i1 <= dist 。
 * 请你返回这些子数组的 最小 总代价。
 * 提示：
 * 1、3 <= n <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、3 <= k <= n
 * 4、k - 2 <= dist <= n - 2
 * 链接：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
"""
from heapq import heappop, heappush, heappushpop
from typing import List


class Solution:

    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        ans = 10**20
        q_small, q_large = [], []
        cur_size = 0
        cur_idx = set()
        v = 0
        for i in range(1, len(nums)):
            num = nums[i]
            i_del = i - dist - 1
            if i_del in cur_idx:
                v -= nums[i_del]
                cur_idx.remove(i_del)
                cur_size -= 1
            while q_large and q_large[0][1] <= i_del:
                heappop(q_large)
            while q_small and q_small[0][1] <= i_del:
                heappop(q_small)
            heappush(q_small, [num, i])
            while q_small and cur_size < k - 1:
                nv, ii = heappop(q_small)
                if ii > i_del:
                    cur_size += 1
                    heappush(q_large, [-nv, ii])
                    v += nv
                    cur_idx.add(ii)
            while q_small and q_large and -q_large[0][0] > q_small[0][0]:
                nv, ii = heappop(q_small)
                if ii > i_del:
                    vv, io = heappushpop(q_large, [-nv, ii])
                    v += nv + vv
                    cur_idx.add(ii)
                    cur_idx.remove(io)
                    if io > i_del:
                        heappush(q_small, [-vv, io])
            if cur_size >= k - 1:
                ans = min(ans, v)

        return ans + nums[0]


if __name__ == '__main__':
    # 570
    print(Solution().minimumCost([
        36, 28, 42, 36, 39, 13, 24, 3, 32, 16, 11, 43, 21, 40, 34, 49, 29, 20, 34, 34, 8, 3, 41, 6, 46, 5, 35, 5, 47, 2
    ], 25, 26))
    # 9
    print(Solution().minimumCost([1, 6, 3, 5], 3, 2))
    # 5
    print(Solution().minimumCost([1, 3, 2, 6, 4, 2], k=3, dist=3))
    # 15
    print(Solution().minimumCost([10, 1, 2, 2, 2, 1], k=4, dist=3))
    # 36
    print(Solution().minimumCost([10, 8, 18, 9], k=3, dist=1))
