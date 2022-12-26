"""
 * 给你一个长度为 n ，下标从 0 开始的整数数组 forts ，表示一些城堡。forts[i] 可以是 -1 ，0 或者 1 ，其中：
 * 1、-1 表示第 i 个位置 没有 城堡。
 * 2、0 表示第 i 个位置有一个 敌人 的城堡。
 * 3、1 表示第 i 个位置有一个你控制的城堡。
 * 现在，你需要决定，将你的军队从某个你控制的城堡位置 i 移动到一个空的位置 j ，满足：
 * 1、0 <= i, j <= n - 1
 * 2、军队经过的位置 只有 敌人的城堡。正式的，对于所有 min(i,j) < k < max(i,j) 的 k ，都满足 forts[k] == 0 。
 * 当军队移动时，所有途中经过的敌人城堡都会被 摧毁 。
 * 请你返回 最多 可以摧毁的敌人城堡数目。如果 无法 移动你的军队，或者没有你控制的城堡，请返回 0 。
 * 提示：
 * 1、1 <= forts.length <= 1000
 * 2、-1 <= forts[i] <= 1
 * 链接：https://leetcode.cn/problems/maximum-enemy-forts-that-can-be-captured
"""
from typing import List


class Solution:

    def captureForts(self, forts: List[int]) -> int:
        ans, n = 0, len(forts)
        for i, f in enumerate(forts):
            if f == 0: continue
            if f == 1:
                sm = 0
                for j in range(i + 1, n):
                    if forts[j] == 1: break
                    if forts[j] == 0: sm += 1
                    if forts[j] == -1:
                        ans = max(ans, sm)
                        break
                sm = 0
                for j in range(i - 1, -1, -1):
                    if forts[j] == 1: break
                    if forts[j] == 0: sm += 1
                    if forts[j] == -1:
                        ans = max(ans, sm)
                        break
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().captureForts([1, 0, 0, -1, 0, 0, -1, 0, 0, 1]))
    # 0
    print(Solution().captureForts([0, 0, 1, -1]))
