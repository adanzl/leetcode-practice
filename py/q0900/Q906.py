"""
 * 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
 * 现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。
 * 提示：
 * 1、1 <= len(L) <= 18
 * 2、1 <= len(R) <= 18
 * 3、L 和 R 是表示 [1, 10^18) 范围的整数的字符串。
 * 4、int(L) <= int(R)
 * 链接：https://leetcode.cn/problems/super-palindromes/
"""
from typing import List
import bisect

is_pa = lambda x: str(x) == str(x)[::-1]

arr = []
for num in range(10**6):
    # odd
    r_o, r_e = num // 10, num
    val_o, val_e = num, num
    while r_o:
        r_o, r = divmod(r_o, 10)
        val_o = val_o * 10 + r
    if is_pa(val_o**2):
        arr.append(val_o**2)
    # even
    if num < 10**5:
        while r_e:
            r_e, r = divmod(r_e, 10)
            val_e = val_e * 10 + r
        if is_pa(val_e**2):
            arr.append(val_e**2)
arr.sort()


class Solution:

    def superpalindromesInRange(self, left: str, right: str) -> int:
        l, r = int(left), int(right)
        return bisect.bisect_left(arr, r + 1) - bisect.bisect_left(arr, l)


if __name__ == '__main__':
    # 4
    print(Solution().superpalindromesInRange("4", right="1000"))
    # 1
    print(Solution().superpalindromesInRange("1", "2"))
    # 21
    print(Solution().superpalindromesInRange("1", "1000000000"))
