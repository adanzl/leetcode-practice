"""
 * 给你一个整数 money ，表示你总共有的钱数（单位为美元）和另一个整数 children ，表示你要将钱分配给多少个儿童。
 * 你需要按照如下规则分配：
 * 1、所有的钱都必须被分配。
 * 2、每个儿童至少获得 1 美元。
 * 3、没有人获得 4 美元。
 * 请你按照上述规则分配金钱，并返回 最多 有多少个儿童获得 恰好 8 美元。如果没有任何分配方案，返回 -1 。
 * 提示：
 * 1、1 <= money <= 200
 * 2、2 <= children <= 30
 * 链接：https://leetcode.cn/problems/distribute-money-to-maximum-children/
"""


class Solution:

    def distMoney(self, money: int, children: int) -> int:
        money -= children
        a, r = divmod(money, 7)
        if money < 0:
            return -1
        ans = min(children, a)
        if ans == children and (r != 0 or a > children):
            ans -= 1
        if r == 3 and a == children - 1:
            ans -= 1
        return max(ans, 0)


if __name__ == '__main__':
    # 1
    print(Solution().distMoney(23, 2))
    # 1
    print(Solution().distMoney(19, 2))
    # 1
    print(Solution().distMoney(20, children=3))
    # 1
    print(Solution().distMoney(13, 3))
    # 0
    print(Solution().distMoney(5, 2))
    # 0
    print(Solution().distMoney(2, 2))
    # -1
    print(Solution().distMoney(1, 5))
    # 4
    print(Solution().distMoney(41, 5))
    # 1
    print(Solution().distMoney(12, 5))
    # 2
    print(Solution().distMoney(16, children=2))
