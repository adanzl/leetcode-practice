"""
 * 如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
 * 给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。
 * 提示：0 <= n <= 10^6
 * 链接：https://leetcode.cn/problems/next-greater-numerically-balanced-number
"""
from collections import Counter


class Solution:

    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 1224445):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i

        return -1


if __name__ == '__main__':
    # 22
    print(Solution().nextBeautifulNumber(1))
    # 1333
    print(Solution().nextBeautifulNumber(1000))
    # 3133
    print(Solution().nextBeautifulNumber(3000))
