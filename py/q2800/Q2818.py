"""
 * 给你一个长度为 n 的正整数数组 nums 和一个整数 k 。
 * 一开始，你的分数为 1 。你可以进行以下操作至多 k 次，目标是使你的分数最大：
 * 1、选择一个之前没有选过的 非空 子数组 nums[l, ..., r] 。
 * 2、从 nums[l, ..., r] 里面选择一个 质数分数 最高的元素 x 。如果多个元素质数分数相同且最高，选择下标最小的一个。
 * 3、将你的分数乘以 x 。
 * nums[l, ..., r] 表示 nums 中起始下标为 l ，结束下标为 r 的子数组，两个端点都包含。
 * 一个整数的 质数分数 等于 x 不同质因子的数目。比方说， 300 的质数分数为 3 ，因为 300 = 2 * 2 * 3 * 5 * 5 。
 * 请你返回进行至多 k 次操作后，可以得到的 最大分数 。
 * 由于答案可能很大，请你将结果对 10^9 + 7 取余后返回。
 * 提示：
 * 1、1 <= nums.length == n <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、1 <= k <= min(n * (n + 1) / 2, 10^9)
 * 链接：https://leetcode.cn/problems/apply-operations-to-maximize-score/
"""
from typing import List

LIMIT = 10**5 + 2
c_prime = [0] * LIMIT  # c_prime[i] 表示 i 的质因子个数
for i in range(2, LIMIT):  # 预处理
    if c_prime[i] == 0:  # i 是质数
        for j in range(i, LIMIT, i):  # 累加 i
            c_prime[j] += 1  # i 是 j 的一个质因子


class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        n = len(nums)
        arr = sorted([[num, idx] for idx, num in enumerate(nums)], key=lambda x: -x[0])
        l_idx, r_idx = [], []
        s = []
        for i, num in enumerate(nums):
            while s and c_prime[nums[s[-1]]] < c_prime[num]:
                s.pop()
            l_idx.append(s[-1] if s else -1)
            s.append(i)
        s.clear()
        for i in range(n - 1, -1, -1):
            while s and c_prime[nums[s[-1]]] <= c_prime[nums[i]]:
                s.pop()
            r_idx.append(s[-1] if s else n)
            s.append(i)
        r_idx.reverse()
        idx, n = 0, len(arr)
        while k > 0 and idx < n:
            num, i = arr[idx]
            l, r = l_idx[i], r_idx[i]
            size = min(k, (r - i) * (i - l))
            ans = (ans * pow(num, size, MOD)) % MOD
            k -= size
            idx += 1
        return ans


if __name__ == '__main__':
    # 823751938
    print(Solution().maximumScore([1, 7, 11, 1, 5], 14))
    # 256720975
    print(Solution().maximumScore([3289, 2832, 14858, 22011], 6))
    # 81
    print(Solution().maximumScore([8, 3, 9, 3, 8], k=2))
    # 4788
    print(Solution().maximumScore([19, 12, 14, 6, 10, 18], k=3))