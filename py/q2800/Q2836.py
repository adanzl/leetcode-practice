"""
 * 给你一个长度为 n 下标从 0 开始的整数数组 receiver 和一个整数 k 。
 * 总共有 n 名玩家，玩家 编号 互不相同，且为 [0, n - 1] 中的整数。
 * 这些玩家玩一个传球游戏，receiver[i] 表示编号为 i 的玩家会传球给编号为 receiver[i] 的玩家。
 * 玩家可以传球给自己，也就是说 receiver[i] 可能等于 i 。
 * 你需要从 n 名玩家中选择一名玩家作为游戏开始时唯一手中有球的玩家，球会被传 恰好 k 次。
 * 如果选择编号为 x 的玩家作为开始玩家，定义函数 f(x) 表示从编号为 x 的玩家开始，k 次传球内所有接触过球玩家的编号之 和 ，
 * 如果有玩家多次触球，则 累加多次 。换句话说， f(x) = x + receiver[x] + receiver[receiver[x]] + ... + receiver(k)[x] 。
 * 你的任务时选择开始玩家 x ，目的是 最大化 f(x) 。
 * 请你返回函数的 最大值 。
 * 注意：receiver 可能含有重复元素。
 * 提示：
 * 1、1 <= receiver.length == n <= 10^5
 * 2、0 <= receiver[i] <= n - 1
 * 3、1 <= k <= 1010
 * 链接：https://leetcode.cn/problems/maximize-value-of-function-in-a-ball-passing-game
"""
from typing import List


class Solution:

    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        ans = 0
        n = len(receiver)
        m = k.bit_length() + 1
        # 树上倍增
        arr = [[(p, p) for _ in range(m + 1)] for p in receiver]  # arr[i][j]->[终点，得分] i号，1<<j 距离的得分
        for i in range(m):
            for j in range(n):
                nx_1, v1 = arr[j][i]
                nx_2, v2 = arr[nx_1][i]
                arr[j][i + 1] = (nx_2, v1 + v2)
        for i in range(n):
            idx = v = i
            for j in range(m + 1):
                if k & (1 << j):
                    idx, val = arr[idx][j]
                    v += val
            ans = max(ans, v)
        return ans


if __name__ == '__main__':
    #
    # print(Solution().getMaxFunctionValue([2, 0, 1], k=3))
    # 6
    print(Solution().getMaxFunctionValue([2, 0, 1], k=4))
    # 10
    print(Solution().getMaxFunctionValue([1, 1, 1, 2, 3], k=3))
    #
    # print(Solution().getMaxFunctionValue())