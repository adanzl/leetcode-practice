"""
 * 我们把玻璃杯摆成金字塔的形状，其中 第一层 有 1 个玻璃杯， 第二层 有 2 个，依次类推到第 100 层，每个玻璃杯 (250ml) 将盛有香槟。
 * 从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。
 * 当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）
 * 例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。
 * 在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。
 * 提示:
 * 0 <= poured <= 10^9
 * 0 <= query_glass <= query_row < 100
 * 链接：https://leetcode.cn/problems/champagne-tower
"""


class Solution:

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * (r + 1) for r in range(query_row + 1)]
        pour = [poured]
        for r in range(query_row + 1):
            n_poured = [0] * (r + 2)
            for c in range(r + 1):
                if pour[c] + glasses[r][c] > 1.0:
                    remain = pour[c] + glasses[r][c] - 1.0
                    n_poured[c] += remain / 2
                    n_poured[c + 1] += remain / 2
                    poured -= 1.0 - glasses[r][c]
                    glasses[r][c] = 1.0
                else:
                    glasses[r][c] += pour[c]
                    poured -= pour[c]
                if poured == 0: break
            pour = n_poured
        return glasses[query_row][query_glass]


if __name__ == '__main__':
    # 0.5
    print(Solution().champagneTower(2, 1, 1))
    # 0.0
    print(Solution().champagneTower(1, 1, 1))
    # 1.0
    print(Solution().champagneTower(100000009, 33, 17))
