"""
 * 现在有一个正凸多边形，其上共有 n 个顶点。顶点按顺时针方向从 0 到 n - 1 依次编号。每个顶点上 正好有一只猴子 。下图中是一个 6 个顶点的凸多边形。
 * 每个猴子同时移动到相邻的顶点。顶点 i 的相邻顶点可以是：
 * 1、顺时针方向的顶点 (i + 1) % n ，或
 * 2、逆时针方向的顶点 (i - 1 + n) % n 。
 * 3、如果移动后至少有两个猴子位于同一顶点，则会发生 碰撞 。
 * 返回猴子至少发生 一次碰撞 的移动方法数。由于答案可能非常大，请返回对 10^9 + 7 取余后的结果。
 * 注意，每只猴子只能移动一次。
 * 提示：3 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/count-collisions-of-monkeys-on-a-polygon/
"""


class Solution:

    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7  # 需要使用快速幂
        return (pow(2, n, MOD) - 2) % MOD


if __name__ == '__main__':
    # 221645998
    print(Solution().monkeyMove(994641619))
    # 6
    print(Solution().monkeyMove(3))
    # 14
    print(Solution().monkeyMove(4))