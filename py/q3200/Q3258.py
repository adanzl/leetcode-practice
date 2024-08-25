"""
 * 给你一个 二进制 字符串 s 和一个整数 k。
 * 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
 * 1、字符串中 0 的数量最多为 k。
 * 2、字符串中 1 的数量最多为 k。
 * 返回一个整数，表示 s 的所有满足 k 约束 的 子字符串 的数量。
 * 提示：
 * 1、1 <= s.length <= 50
 * 2、1 <= k <= s.length
 * 3、s[i] 是 '0' 或 '1'。
 * 链接：https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/description/
"""
from typing import Counter

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            cnt = Counter()
            for j in range(i, n):
                cnt[s[j]] += 1
                if cnt['0'] <= k or cnt['1'] <= k:
                    ans += 1
                else:
                    break
        return ans


if __name__ == '__main__':
    # 12
    print(Solution().countKConstraintSubstrings("10101", k=1))
    # 25
    print(Solution().countKConstraintSubstrings("1010101", k=2))
    # 15
    print(Solution().countKConstraintSubstrings("11111", k=1))
