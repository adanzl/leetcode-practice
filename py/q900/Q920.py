"""
 * 你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：
 * 1、每首歌至少播放一次。
 * 2、一首歌只有在其他 K 首歌播放完之后才能再次播放。
 * 返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。
 * 提示：0 <= K < N <= L <= 100
 * 链接：https://leetcode.cn/problems/number-of-music-playlists/
"""
from math import *


class Solution:

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(n, 0, -1):
                dp[i][j] = dp[i - 1][j] * max(0, j - k)
                dp[i][j] += dp[i - 1][j - 1] * (n - j + 1)
                dp[i][j] %= MOD
        '''
        dp = [0] * (n + 1)
        dp[0] = 1
        for _ in range(goal):
            for j in range(n, 0, -1):
                dp[j] = dp[j] * max(0, j - k)  # 选重复的
                dp[j] += dp[j - 1] * (n - j + 1)  # 选新的
                dp[j] %= MOD
            dp[0] = 0  # 如果要压缩必须把第一位重置为0， 因为只有dp[0][0]=1其他dp[i][0]=0
        return dp[n]
        '''
        return dp[goal][n]


if __name__ == "__main__":
    # 6
    print(Solution().numMusicPlaylists(2, 3, 0))
    # 6
    print(Solution().numMusicPlaylists(3, 3, 1))
    # 2
    print(Solution().numMusicPlaylists(2, 3, 1))
