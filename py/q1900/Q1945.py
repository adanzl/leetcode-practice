"""
 * 链接：https://leetcode.cn/problems/sum-of-digits-of-string-after-convert/
"""


class Solution:

    def getLucky(self, s: str, k: int) -> int:
        sm = 0
        for num in [ord(c) - ord('a') + 1 for c in s]:
            while num:
                sm += num % 10
                num //= 10
        for _ in range(1, k):
            nn = 0
            while sm:
                nn += sm % 10
                sm //= 10
            sm = nn
        return sm


if __name__ == '__main__':
    # 36
    print(Solution().getLucky("iiii", 1))
    # 6
    print(Solution().getLucky("leetcode", 2))
    # 8
    print(Solution().getLucky("zbax", 2))