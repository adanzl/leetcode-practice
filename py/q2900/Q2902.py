"""
 * 给你一个下标从 0 开始的非负整数数组 nums 和两个整数 l 和 r 。
 * 请你返回 nums 中子多重集合的和在闭区间 [l, r] 之间的 子多重集合的数目 。
 * 由于答案可能很大，请你将答案对 10^9 + 7 取余后返回。
 * 子多重集合 指的是从数组中选出一些元素构成的 无序 集合，
 * 每个元素 x 出现的次数可以是 0, 1, ..., occ[x] 次，其中 occ[x] 是元素 x 在数组中的出现次数。
 * 注意：
 * 1、如果两个子多重集合中的元素排序后一模一样，那么它们两个是相同的 子多重集合 。
 * 2、空 集合的和是 0 。
 * 提示：
 * 1、1 <= nums.length <= 2 * 10^4
 * 2、0 <= nums[i] <= 2 * 10^4
 * 3、nums 的和不超过 2 * 10^4 
 * 4、0 <= l <= r <= 2 * 10^4
 * 链接：https://leetcode.cn/problems/count-of-sub-multisets-with-bounded-sum/
"""
from collections import Counter
from typing import List


class Solution:

    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        cnt, s = Counter(nums), 0
        f = [cnt[0] + 1] + [0] * (r)
        del cnt[0]
        # 有限物品 多重背包 相同物品的顺序不同算作不同方案
        # f(i,j) 表示前i个物品放入容量 j 的背包中，方案的数量，v_i表示第i个物品的容量，n表示第i个物品的熟练限制
        # f(i,j) = f(i-1,j) + f(i-1,j-1*v_i) + f(i-1,j-2*v_i) + ... + f(i-1,j-n*v_i)
        # 此时遍历容量和物品可以求出每个容量的方案数，但是复杂度太高，需要优化
        # 特殊技巧：观察v_i，f(i,j) 可以由 f(i,j-v_i) 计算得出
        # f(i,j-v_i) = f(i-1,j-1*v_i) + f(i-1,j-2*v_i) + f(i-1,j-3*v_i) + ... + f(i-1,j-n*v_i) + f(i-1,j-(n+1)*v_i)
        #            = f(i,j) - f(i-1,j) + f(i-1,j-(n+1)*v_i)
        # => f(i,j) = f(i,j-v_i) + f(i-1,j) - f(i-1,j-(n+1)*v_i) 如果j<(n+1)*v_i则最有一项取0
        for w, cc in cnt.items():
            nf = f[:]
            s = min(s + w * cc, r)  # 到目前为止，能选的元素和至多为 s
            for j in range(w, s + 1):  # 把循环上界从 r 改成 s，能快一倍
                nf[j] += nf[j - w]
                if j >= (cc + 1) * w:
                    nf[j] -= f[j - (cc + 1) * w]
            f = nf

        return sum(f[l:]) % MOD


if __name__ == '__main__':
    # 1
    print(Solution().countSubMultisets([1, 2, 2, 3], l=6, r=6))
    # 9
    print(Solution().countSubMultisets([0, 0, 1, 2, 3], 2, 3))
    # 6
    print(Solution().countSubMultisets([0, 0, 0, 0, 0], 0, 0))
    # 7
    print(Solution().countSubMultisets([2, 1, 4, 2, 7], l=1, r=5))
    # 9
    print(Solution().countSubMultisets([1, 2, 1, 3, 5, 2], l=3, r=5))
