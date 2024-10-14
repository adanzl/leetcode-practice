"""
 * 给你一个长度为 n 的字符串 source ，一个字符串 pattern 且它是 source 的 子序列 ，
 * 和一个 有序 整数数组 targetIndices ，整数数组中的元素是 [0, n - 1] 中 互不相同 的数字。
 * 定义一次 操作 为删除 source 中下标在 idx 的一个字符，且需要满足：
 * 1、idx 是 targetIndices 中的一个元素。
 * 2、删除字符后，pattern 仍然是 source 的一个 子序列 。
 * 执行操作后 不会 改变字符在 source 中的下标位置。比方说，如果从 "acb" 中删除 'c' ，下标为 2 的字符仍然是 'b' 。
 * 请你返回 最多 可以进行多少次删除操作。
 * 子序列指的是在原字符串里删除若干个（也可以不删除）字符后，不改变顺序地连接剩余字符得到的字符串。
 * 提示：
 * 1、1 <= n == source.length <= 3 * 10^3
 * 2、1 <= pattern.length <= n
 * 3、1 <= targetIndices.length <= n
 * 4、targetIndices 是一个升序数组。
 * 5、输入保证 targetIndices 包含的元素在 [0, n - 1] 中且互不相同。
 * 6、source 和 pattern 只包含小写英文字母。
 * 7、输入保证 pattern 是 source 的一个子序列。
 * 链接：https://leetcode.cn/problems/find-maximum-removals-from-source-string/
"""
import bisect
from functools import cache
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:

        st = set(targetIndices)

        @cache
        def dfs(i, j):
            if j < 0:
                return bisect.bisect_right(targetIndices, i)
            if i < 0:
                return -INF
            ret = -INF
            if source[i] == pattern[j]:
                ret = max(ret, dfs(i - 1, j - 1))
                if i in st:
                    ret = max(ret, dfs(i - 1, j) + 1)
            else:
                ret = max(ret, dfs(i - 1, j) + (1 if i in st else 0))

            return ret

        n = len(source)
        i, j = n - 1, len(pattern) - 1
        while i > targetIndices[-1]:
            if source[i] == pattern[j]:
                j -= 1
            if j < 0:
                return len(targetIndices)
            i -= 1
        return dfs(i, j)


if __name__ == '__main__':
    # 1
    print(Solution().maxRemovals("nhdb", pattern="hb", targetIndices=[0, 1]))
    # 1
    print(Solution().maxRemovals("abbaa", pattern="aba", targetIndices=[0, 1, 2]))
    # 2
    print(Solution().maxRemovals("bcda", pattern="d", targetIndices=[0, 3]))
    # 0
    print(Solution().maxRemovals("dda", pattern="dda", targetIndices=[0, 1, 2]))
    # 2
    print(Solution().maxRemovals("yeyeykyded", pattern="yeyyd", targetIndices=[0, 2, 3, 4]))
