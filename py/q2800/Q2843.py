"""
 * 对于一个由 2 * n 位数字组成的整数 x ，如果其前 n 位数字之和与后 n 位数字之和相等，则认为这个数字是一个对称整数。
 * 返回在 [low, high] 范围内的 对称整数的数目 。
 * 提示：1 <= low <= high <= 10^4
 * 链接：https://leetcode.cn/problems/count-symmetric-integers/
"""
#
# @lc app=leetcode.cn id=2843 lang=python3
#

# @lc code=start


class Solution:

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            s = str(num)
            n = len(s)
            if n & 1 == 0 and sum([int(c) for c in s[:n // 2]]) == sum([int(c) for c in s[n // 2:]]):
                ans += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 9
    print(Solution().countSymmetricIntegers(1, high=100))
    # 4
    print(Solution().countSymmetricIntegers(1200, high=1230))
