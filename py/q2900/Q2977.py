"""
 * 给你两个下标从 0 开始的字符串 source 和 target ，它们的长度均为 n 并且由 小写 英文字母组成。
 * 另给你两个下标从 0 开始的字符串数组 original 和 changed ，以及一个整数数组 cost ，
 * 其中 cost[i] 代表将字符串 original[i] 更改为字符串 changed[i] 的成本。
 * 你从字符串 source 开始。在一次操作中，如果 存在 任意 下标 j 满足 cost[j] == z  、original[j] == x 以及 changed[j] == y ，
 * 你就可以选择字符串中的 子串 x 并以 z 的成本将其更改为 y 。 你可以执行 任意数量 的操作，但是任两次操作必须满足 以下两个 条件 之一 ：
 * 1、在两次操作中选择的子串分别是 source[a..b] 和 source[c..d] ，满足 b < c  或 d < a 。换句话说，两次操作中选择的下标 不相交 。
 * 2、在两次操作中选择的子串分别是 source[a..b] 和 source[c..d] ，满足 a == c 且 b == d 。换句话说，两次操作中选择的下标 相同 。
 * 返回将字符串 source 转换为字符串 target 所需的 最小 成本。如果不可能完成转换，则返回 -1 。
 * 注意，可能存在下标 i 、j 使得 original[j] == original[i] 且 changed[j] == changed[i] 。
 * 提示：
 * 1、1 <= source.length == target.length <= 1000
 * 2、source、target 均由小写英文字母组成
 * 3、1 <= cost.length == original.length == changed.length <= 100
 * 4、1 <= original[i].length == changed[i].length <= source.length
 * 5、original[i]、changed[i] 均由小写英文字母组成
 * 6、original[i] != changed[i]
 * 7、1 <= cost[i] <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/
"""
from collections import defaultdict
from typing import List


class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = 0x3c3c3c3c3c
        dis = defaultdict(lambda: defaultdict(lambda: inf))
        len_to_strs = defaultdict(set)  # 基于长度分组
        for f, t, c in zip(original, changed, cost):
            dis[f][f] = 0
            dis[t][t] = 0
            dis[f][t] = min(c, dis[f][t])
            len_to_strs[len(f)].add(f)
            len_to_strs[len(t)].add(t)
        # Floyed
        for strs in len_to_strs.values():
            for k in strs:
                for i in strs:
                    if dis[i][k] == inf:
                        continue
                    for j in strs:
                        dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j])

        nn = len(source)
        dp = [0] + [inf] * nn
        for r in range(nn):
            if source[r] == target[r]:
                dp[r + 1] = min(dp[r + 1], dp[r])
            for size, strs in len_to_strs.items():  # 此处基于已经存在映射关系进行筛选，可以减少搜索规模
                l = r - size + 1
                if l < 0: continue
                if dp[l] == inf: continue
                s, t = source[l:r + 1], target[l:r + 1]
                if s == t:
                    dp[r + 1] = min(dp[r + 1], dp[l])
                if s in strs and t in strs:
                    dp[r + 1] = min(dp[r + 1], dp[l] + dis[s][t])
        return dp[-1] if dp[-1] != inf else -1


if __name__ == '__main__':
    # 9
    print(Solution().minimumCost("abcdefgh",
                                 target="acdeeghh",
                                 original=["bcd", "fgh", "thh"],
                                 changed=["cde", "thh", "ghh"],
                                 cost=[1, 3, 5]))
    # 28
    print(Solution().minimumCost("abcd",
                                 target="acbe",
                                 original=["a", "b", "c", "c", "e", "d"],
                                 changed=["b", "c", "b", "e", "b", "e"],
                                 cost=[2, 5, 5, 1, 2, 20]))
    # -1
    print(Solution().minimumCost("abcdefgh",
                                 target="addddddd",
                                 original=["bcd", "defgh"],
                                 changed=["ddd", "ddddd"],
                                 cost=[100, 1578]))
