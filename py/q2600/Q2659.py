"""
 * 给你一个包含若干 互不相同 整数的数组 nums ，你需要执行以下操作 直到数组为空 ：
 * 1、如果数组中第一个元素是当前数组中的 最小值 ，则删除它。
 * 2、否则，将第一个元素移动到数组的 末尾 。
 * 请你返回需要多少个操作使 nums 为空。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 3、nums 中的元素 互不相同 。
 * 链接：https://leetcode.cn/problems/make-array-empty/
"""
from typing import List

from sortedcontainers import SortedList


class Solution:

    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        arr = sorted([[v, i] for i, v in enumerate(nums)])
        st = SortedList()
        n = len(nums)
        ans = 0
        pre = -1
        for _, i in arr:
            if pre < i:
                i0, i1 = st.bisect_left(pre + 1), st.bisect_left(i)
                ans += i - pre - (i1 - i0)
            else:
                i0, i1 = st.bisect_left(pre + 1), st.bisect_left(i)
                ans += (i - pre + n) % n - (i1 + len(st) - i0)
            st.add(i)
            pre = i
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().countOperationsToEmptyArray([3, 4, -1]))
    # 5
    print(Solution().countOperationsToEmptyArray([-15, -19, 5]))
    # 5
    print(Solution().countOperationsToEmptyArray([1, 2, 4, 3]))
    # 3
    print(Solution().countOperationsToEmptyArray([1, 2, 3]))
