"""
 * 给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。
 * 现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
 * 如果存在这样的分法，请返回 true ；否则，返回 false。
 * 提示：
 * 1、arr.length == n
 * 2、1 <= n <= 10^5
 * 3、n 为偶数
 * 4、-10^9 <= arr[i] <= 10^9
 * 5、1 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/check-if-array-pairs-are-divisible-by-k/
"""
from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1: return True
        cnt = Counter()
        for v in arr:
            cnt[v % k] += 1
        for a in range(1, k):
            if a == k - a:
                if cnt[a] & 1:
                    return False
            elif cnt[a] != cnt[k - a]:
                return False
        return True


if __name__ == '__main__':
    # True
    print(Solution().canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
    # True
    print(Solution().canArrange([1, 2, 3, 4, 5, 6], k=7))
    # False
    print(Solution().canArrange([1, 2, 3, 4, 5, 6], k=10))
