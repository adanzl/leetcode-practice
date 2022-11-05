"""
 * 给你一个下标从 0 开始的数组 nums ，它包含若干正整数，表示数轴上你需要摧毁的目标所在的位置。同时给你一个整数 space 。
 * 你有一台机器可以摧毁目标。给机器 输入 nums[i] ，这台机器会摧毁所有位置在 nums[i] + c * space 的目标，其中 c 是任意非负整数。你想摧毁 nums 中 尽可能多 的目标。
 * 请你返回在摧毁数目最多的前提下，nums[i] 的 最小值 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= space <= 10^9
 * 链接：https://leetcode.cn/problems/destroy-sequential-targets/
"""
from collections import Counter
from typing import List


class Solution:

    def destroyTargets(self, nums: List[int], space: int) -> int:
        c = Counter()
        m = dict()
        for num in nums:
            r = num % space
            c[r] += 1
            m[r] = min(m.get(r, 0x3c3c3c3c), num)
        k = c.most_common(1)[0]
        arr = [m[v] for v in c.keys() if c[v] == k[1]]
        return sorted(arr)[0]


if __name__ == '__main__':
    # 1
    print(Solution().destroyTargets([1, 3, 5, 2, 4, 6], 2))
    # 2
    print(Solution().destroyTargets([6, 2, 5], 100))
    # 1
    print(Solution().destroyTargets([3, 7, 8, 1, 1, 5], 2))
