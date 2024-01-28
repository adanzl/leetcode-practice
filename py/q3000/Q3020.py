"""
 * 给你一个 正整数 数组 nums 。
 * 你需要从数组中选出一个满足下述条件的子集：
 *     你可以将选中的元素放置在一个下标从 0 开始的数组中，并使其遵循以下模式：
 *     [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x]（注意，k 可以是任何 非负 的 2 的幂）。
 *     例如，[2, 4, 16, 4, 2] 和 [3, 9, 3] 都符合这一模式，而 [2, 4, 8, 4, 2] 则不符合。
 * 返回满足这些条件的子集中，元素数量的 最大值 。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-maximum-number-of-elements-in-subset/
"""
from collections import Counter
import math
from typing import List


class Solution:

    def maximumLength(self, nums: List[int]) -> int:
        ans = 1
        cnt = Counter(nums)
        vis = set()
        if 1 in cnt:
            ans = cnt[1] - ((cnt[1] & 1) ^ 1)
            vis.add(1)
        for v in sorted(cnt.keys()):
            if v in vis or cnt[v] == 1: continue
            vv = 1
            vq = v * v
            while vq in cnt and cnt[v] >= 2:
                vis.add(vq)
                vv += 2
                v = vq
                vq = vq * vq
            ans = max(ans, vv)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maximumLength([
        65025, 312481, 107584, 148996, 322624, 194481, 570025, 15376, 123904, 848241, 88804, 47961, 117649, 66564,
        295936, 271441, 16900, 474721, 27556, 285156, 11236, 175561, 917764, 968256, 16, 38025, 312481, 426409, 354025,
        8464, 522729, 60516, 210681, 378225, 638401, 101124, 697225, 427716, 262144, 940900, 988036, 324900, 151321,
        309136, 178929, 168921, 189225, 4, 301401, 659344, 786769, 964324, 15625, 302500, 56644, 61504, 31684, 369664,
        345744, 19321, 59049, 5041, 40000, 147456, 372100, 708964, 171396, 214369, 707281, 484, 49729, 82944, 100489,
        103684, 58564, 208849, 946729, 84100, 4, 600625, 334084, 683929, 9604, 245025, 97969, 147456, 160801, 434281,
        223729, 294849, 166464, 432964, 518400, 376996, 17424, 315844, 256, 737881, 10000, 632025
    ]))
    # 9
    print(Solution().maximumLength([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]))
    # 3
    print(Solution().maximumLength([5, 4, 1, 2, 2]))
    # 1
    print(Solution().maximumLength([1, 16, 49, 16, 121]))
    # 1
    print(Solution().maximumLength([1, 3, 2, 4]))
