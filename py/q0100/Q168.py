"""
 * 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
 * 例如：
 * A -> 1
 * B -> 2
 * C -> 3
 * ...
 * Z -> 26
 * AA -> 27
 * AB -> 28 
 * ...
 * 提示：1 <= columnNumber <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/excel-sheet-column-title/
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        while columnNumber:
            columnNumber -= 1
            ans = c[columnNumber % 26] + ans
            columnNumber //= 26
        return ans


if __name__ == '__main__':
    # "A"
    print(Solution().convertToTitle(1))
    # "AB"
    print(Solution().convertToTitle(28))
    # 'ZY'
    print(Solution().convertToTitle(701))
    # 'FXSHRXW'
    print(Solution().convertToTitle(2147483647))