"""
 * 给你一个整数 num ，返回 num 中能整除 num 的数位的数目。
 * 如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。
 * 提示：
 * 1、1 <= num <= 10^9
 * 2、num 的数位中不含 0
 * 链接：https://leetcode.cn/problems/count-the-digits-that-divide-a-number/
"""


class Solution:

    def countDigits(self, num: int) -> int:
        ans = 0
        for n in str(num):
            if num % int(n) == 0: ans += 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().countDigits(7))
    # 2
    print(Solution().countDigits(121))
    # 4
    print(Solution().countDigits(1248))