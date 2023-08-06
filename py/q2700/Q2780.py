"""
 * 如果元素 x 在长度为 m 的整数数组 arr 中满足 freq(x) * 2 > m ，那么我们称 x 是 支配元素 。
 * 其中 freq(x) 是 x 在数组 arr 中出现的次数。注意，根据这个定义，数组 arr 最多 只会有 一个 支配元素。
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums ，数据保证它含有一个支配元素。
 * 你需要在下标 i 处将 nums 分割成两个数组 nums[0, ..., i] 和 nums[i + 1, ..., n - 1] ，如果一个分割满足以下条件，我们称它是 合法 的：
 * 1、0 <= i < n - 1
 * 2、nums[0, ..., i] 和 nums[i + 1, ..., n - 1] 的支配元素相同。
 * 这里， nums[i, ..., j] 表示 nums 的一个子数组，它开始于下标 i ，结束于下标 j ，两个端点都包含在子数组内。
 * 特别地，如果 j < i ，那么 nums[i, ..., j] 表示一个空数组。
 * 请你返回一个 合法分割 的 最小 下标。如果合法分割不存在，返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、nums 有且只有一个支配元素。
 * 链接：https://leetcode.cn/problems/minimum-index-of-a-valid-split/
"""
from collections import Counter
from typing import List


class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        r_cnt, l_cnt = Counter(), Counter()
        n = len(nums)
        m_r = [-1] * n
        for i in range(n - 1, -1, -1):
            r_cnt[nums[i]] += 1
            if r_cnt[nums[i]] * 2 > n - i:
                m_r[i] = nums[i]
            elif r_cnt[nums[i]] * 2 == n - i:
                m_r[i] = -1
            else:
                m_r[i] = m_r[i + 1]
            if r_cnt[m_r[i]] * 2 <= n - i:
                m_r[i] = -1

        for i in range(n - 1):
            l_cnt[nums[i]] += 1
            if l_cnt[nums[i]] * 2 > i + 1:
                if m_r[i + 1] != -1 and m_r[i + 1] == nums[i]:
                    return i
        return -1


if __name__ == '__main__':
    # -1
    print(Solution().minimumIndex([1, 2, 1, 2, 1, 1, 1, 1, 3, 2, 3]))
    # 0
    print(Solution().minimumIndex([1, 2, 1, 1]))
    # 0
    print(Solution().minimumIndex([1, 1, 1]))
    # 2
    print(Solution().minimumIndex([1, 2, 2, 2]))
    # 4
    print(Solution().minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]))
    # -1
    print(Solution().minimumIndex([3, 3, 3, 3, 7, 2, 2]))
