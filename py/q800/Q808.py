"""
 * 有 A 和 B 两种类型 的汤。一开始每种类型的汤有 n 毫升。有四种分配操作：
 * 1、提供 100ml 的 汤A 和 0ml 的 汤B 。
 * 2、提供 75ml 的 汤A 和 25ml 的 汤B 。
 * 3、提供 50ml 的 汤A 和 50ml 的 汤B 。
 * 4、提供 25ml 的 汤A 和 75ml 的 汤B 。
 * 当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为 0.25 的操作中进行分配选择。
 * 如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。
 * 注意 不存在先分配 100 ml 汤B 的操作。
 * 需要返回的值： 汤A 先分配完的概率 +  汤A和汤B 同时分配完的概率 / 2。返回值在正确答案 10^-5 的范围内将被认为是正确的。
 * 提示: 0 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/soup-servings
"""


class Solution:

    def soupServings(self, n: int) -> float:
        if n > 15000: return 1.0
        ans = [0, 0, 0]
        dic = dict()
        dic[(0, 0)] = 1
        delta = [[100, 0], [75, 25], [50, 50], [25, 75]]
        while dic:
            n_dic = dict()
            for k, v in dic.items():
                v /= 4
                for d in delta:
                    nk = (k[0] + d[0], k[1] + d[1])
                    if nk[0] >= n and nk[1] >= n:
                        ans[2] += v
                    elif nk[0] >= n:
                        ans[0] += v
                    elif nk[1] >= n:
                        ans[1] += v
                    else:
                        n_dic[nk] = n_dic.get(nk, 0) + v
            dic = n_dic
        # print(ans)
        return ans[0] + ans[2] / 2


if __name__ == '__main__':
    # 0.71875
    print(Solution().soupServings(100))
    # 0.62500
    print(Solution().soupServings(50))
    # 1.0
    print(Solution().soupServings(1e9))
    print(Solution().soupServings(100000))