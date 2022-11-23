"""
 * 给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。
 * 如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：
 * 1、s 被分成 k 段互不相交的子字符串。
 * 2、每个子字符串长度都 至少 为 minLength 。
 * 3、每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。质数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。
 * 请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 10^9 + 7 取余 后的结果。
 * 一个 子字符串 是字符串中一段连续字符串序列。
 * 提示：
 * 1、1 <= k, minLength <= s.length <= 1000
 * 2、s 每个字符都为数字 '1' 到 '9' 之一。
 * 链接：https://leetcode.cn/problems/number-of-beautiful-partitions/
"""
from typing import List


class Solution:

    def beautifulPartitions(self, s: str, k: int, l: int) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        is_prime = lambda c: c in "2357"
        if k * l > n or not is_prime(s[0]) or is_prime(s[-1]):  # 剪枝
            return 0
        # 判断是否可以在 j-1 和 j 之间分割（开头和末尾也算）
        can_partition = lambda j: j == 0 or j == n or not is_prime(s[j - 1]) and is_prime(s[j])
        for i in range(1, k + 1):
            sum = 0
            # 枚举的起点和终点需要给前后的子串预留出足够的长度
            for j in range(i * l, n - (k - i) * l + 1):
                if can_partition(j - l): sum += dp[i - 1][j - l]  # 长度至少是 minLength
                if can_partition(j): dp[i][j] = sum

        return dp[-1][-1] % (10**9 + 7)


if __name__ == '__main__':
    # 4
    print(Solution().beautifulPartitions("783938233588472343879134266968", 4, 6))
    # 3
    print(Solution().beautifulPartitions("23542185131", 3, 2))
    # 1
    print(Solution().beautifulPartitions("23542185131", 3, 3))
    # 1
    print(Solution().beautifulPartitions("3312958", 3, 1))
