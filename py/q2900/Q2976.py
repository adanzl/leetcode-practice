"""
 * 给你两个下标从 0 开始的字符串 source 和 target ，它们的长度均为 n 并且由 小写 英文字母组成。
 * 另给你两个下标从 0 开始的字符数组 original 和 changed ，以及一个整数数组 cost ，其中 cost[i] 代表将字符 original[i] 更改为字符 changed[i] 的成本。
 * 你从字符串 source 开始。在一次操作中，如果 存在 任意 下标 j 满足 cost[j] == z  、original[j] == x 以及 changed[j] == y 。
 * 你就可以选择字符串中的一个字符 x 并以 z 的成本将其更改为字符 y 。
 * 返回将字符串 source 转换为字符串 target 所需的 最小 成本。如果不可能完成转换，则返回 -1 。
 * 注意，可能存在下标 i 、j 使得 original[j] == original[i] 且 changed[j] == changed[i] 。
 * 提示：
 * 1、1 <= source.length == target.length <= 10^5
 * 2、source、target 均由小写英文字母组成
 * 3、1 <= cost.length== original.length == changed.length <= 2000
 * 4、original[i]、changed[i] 是小写英文字母
 * 5、1 <= cost[i] <= 10^6
 * 6、original[i] != changed[i]
 * 链接：https://leetcode.cn/problems/minimum-cost-to-convert-string-i/
"""
from typing import List


class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        nn = lambda c: ord(c) - ord('a')
        inf = 0x3c3c3c3c
        n = 26
        dis = [[0 if i == j else inf for i in range(26)] for j in range(26)]
        for f, t, c in zip(original, changed, cost):
            u, v = nn(f), nn(t)
            dis[u][v] = min(c, dis[u][v])
        # Floyed
        for k in range(n):  # 遍历中间节点，此处必须放在最外层
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        ans = 0
        for c0, c1 in zip(source, target):
            u,v = nn(c0), nn(c1)
            if dis[u][v] == inf:
                return -1
            ans += dis[u][v]
        return ans


if __name__ == '__main__':
    # 28
    print(Solution().minimumCost("abcd",
                                 target="acbe",
                                 original=["a", "b", "c", "c", "e", "d"],
                                 changed=["b", "c", "b", "e", "b", "e"],
                                 cost=[2, 5, 5, 1, 2, 20]))
    # 12
    print(Solution().minimumCost("aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]))
    # -1
    print(Solution().minimumCost("abcd", target="abce", original=["a"], changed=["e"], cost=[10000]))
