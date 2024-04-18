"""
 * 一个整数数组 original 可以转变成一个 双倍 数组 changed ，
 * 转变方式为将 original 中每个元素 值乘以 2 加入数组中，然后将所有元素 随机打乱 。
 * 给你一个数组 changed ，如果 change 是 双倍 数组，那么请你返回 original数组，
 * 否则请返回空数组。original 的元素可以以 任意 顺序返回。
 * 提示：
 * 1、1 <= changed.length <= 10^5
 * 2、0 <= changed[i] <= 10^5
 * 链接：https://leetcode.cn/problems/find-original-array-from-doubled-array/
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=2007 lang=python3
#
# [2007] 从双倍数组中还原原数组
#


# @lc code=start
class Solution:

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        ans = []
        for v in list(sorted(cnt.keys())):
            if v == 0:
                if cnt[v] & 1:
                    return []
                else:
                    ans.extend([v] * (cnt[v] // 2))
            else:
                if cnt[v << 1] < cnt[v]:
                    return []
                else:
                    ans.extend([v] * cnt[v])
                    cnt[v << 1] -= cnt[v]
        return ans


# @lc code=end

if __name__ == '__main__':
    # [1,3,4]
    print(Solution().findOriginalArray([1, 3, 4, 2, 6, 8]))
    # []
    print(Solution().findOriginalArray([0]))
    # []
    print(Solution().findOriginalArray([6, 3, 0, 1]))
    # []
    print(Solution().findOriginalArray([1]))
