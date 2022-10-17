"""
 * 给你一个正整数 n ，你需要找到一个下标从 0 开始的数组 powers ，它包含 最少 数目的 2 的幂，且它们的和为 n 。powers 数组是 非递减 顺序的。根据前面描述，构造 powers 数组的方法是唯一的。
 * 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [left_i, right_i] ，其中 queries[i] 表示请你求出满足 left_i <= j <= right_i 的所有 powers[j] 的乘积。
 * 请你返回一个数组 answers ，长度与 queries 的长度相同，其中 answers[i]是第 i 个查询的答案。由于查询的结果可能非常大，请你将每个 answers[i] 都对 109 + 7 取余 。
 * 提示：
 * 1、1 <= n <= 10^9
 * 2、1 <= queries.length <= 10^5
 * 3、0 <= start_i <= end_i < powers.length
 * 链接：https://leetcode.cn/problems/range-product-queries-of-powers/
"""
from typing import List


class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans, powers = []
        MOD = 10**9 + 7
        idx = 0
        while n:
            if n & 1 != 0:
                powers.append(1 << idx)
            n >>= 1
            idx += 1
        for l, r in queries:
            v = 1
            for i in range(l, r + 1):
                v = v * powers[i] % MOD
            ans.append(v)
        return ans


if __name__ == '__main__':
    # [2,4,64]
    print(Solution().productQueries(15, [[0, 1], [2, 2], [0, 3]]))
    # [2]
    print(Solution().productQueries(2, [[0, 0]]))