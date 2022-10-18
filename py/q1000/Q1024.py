"""
 * 你将会获得一系列视频片段，这些片段来自于一项持续时长为 time 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
 * 使用数组 clips 描述所有的视频片段，其中 clips[i] = [start_i, end_i] 表示：某个视频片段开始于 start_i 并于 end_i 结束。
 * 甚至可以对这些片段自由地再剪辑：
 * 例如，片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
 * 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, time]）。
 * 返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。
 * 提示：
 * 1、1 <= clips.length <= 100
 * 2、0 <= start_i <= end_i <= 100
 * 3、1 <= time <= 100
 * 链接：https://leetcode.cn/problems/video-stitching/
"""
from typing import List


class Solution:

    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n = len(clips)
        dp = [0] * (n + 1)
        for clip in clips:
            for i in range(n, 0, -1):
                if clip[0] <= dp[i - 1]:
                    dp[i] = max(dp[i], clip[1])
        for i in range(n + 1):
            if dp[i] >= time:
                return i
        return -1


if __name__ == '__main__':
    # 3
    print(Solution().videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
    # 3
    print(Solution().videoStitching([[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], 9))
    # -1
    print(Solution().videoStitching([[0, 1], [1, 2]], 5))
