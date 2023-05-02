"""
 * 给你两个下标从 0 开始长度为 n 的整数排列 A 和 B 。
 * A 和 B 的 前缀公共数组 定义为数组 C ，其中 C[i] 是数组 A 和 B 到下标为 i 之前公共元素的数目。
 * 请你返回 A 和 B 的 前缀公共数组 。
 * 如果一个长度为 n 的数组包含 1 到 n 的元素恰好一次，我们称这个数组是一个长度为 n 的 排列 。
 * 提示：
 * 1、1 <= A.length == B.length == n <= 50
 * 2、1 <= A[i], B[i] <= n
 * 3、题目保证 A 和 B 两个数组都是 n 个元素的排列。
 * 链接：https://leetcode.cn/problems/find-the-prefix-common-array-of-two-arrays/
"""
from typing import List


class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa, sb = set(), set()
        ans = []
        v = 0
        for a, b in zip(A, B):
            if a == b:
                v += 1
            else:
                if a in sb:
                    v += 1
                if b in sa:
                    v += 1
            sa.add(a)
            sb.add(b)
            ans.append(v)
        return ans


if __name__ == '__main__':
    # [0,2,3,4]
    print(Solution().findThePrefixCommonArray([1, 3, 2, 4], B=[3, 1, 2, 4]))
    # [0,1,3]
    print(Solution().findThePrefixCommonArray([2, 3, 1], B=[3, 1, 2]))