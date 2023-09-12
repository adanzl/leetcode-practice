"""
 * 给你一个下标从 0 开始的字符串 num ，表示一个非负整数。
 * 在一次操作中，您可以选择 num 的任意一位数字并将其删除。请注意，如果你删除 num 中的所有数字，则 num 变为 0。
 * 返回最少需要多少次操作可以使 num 变成特殊数字。
 * 如果整数 x 能被 25 整除，则该整数 x 被认为是特殊数字。
 * 提示
 * 1、1 <= num.length <= 100
 * 2、num 仅由数字 '0' 到 '9' 组成
 * 3、num 不含任何前导零
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/
"""


class Solution:

    def minimumOperations(self, num: str) -> int:
        if num == '0': return 0
        n = len(num)

        def check(ss):
            ii, ret = 0, 0
            for i in range(n - 1, -1, -1):
                if num[i] == ss[ii]:
                    ii += 1
                else:
                    ret += 1
                if ii >= len(ss):
                    break
            return ret if ii == len(ss) else n

        ans = min([check(ss) for ss in ['00', '52', '05', '57']])
        if '0' in num:
            ans = min(ans, n - 1)
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().minimumOperations("820366"))
    # 0
    print(Solution().minimumOperations("75"))
    # 1
    print(Solution().minimumOperations("10"))
    # 3
    print(Solution().minimumOperations("2908305"))
    # 2
    print(Solution().minimumOperations("2245047"))