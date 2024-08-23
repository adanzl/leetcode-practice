"""
 * 一个国家由 n 个编号为 0 到 n - 1 的城市组成。在这个国家里，每两个 城市之间都有一条道路连接。
 * 总共有 m 个编号为 0 到 m - 1 的朋友想在这个国家旅游。他们每一个人的路径都会包含一些城市。
 * 每条路径都由一个整数数组表示，每个整数数组表示一个朋友按顺序访问过的城市序列。
 * 同一个城市在一条路径中可能 重复 出现，但同一个城市在一条路径中不会连续出现。
 * 给你一个整数 n 和二维数组 paths ，其中 paths[i] 是一个整数数组，表示第 i 个朋友走过的路径，
 * 请你返回 每一个 朋友都走过的 最长公共子路径 的长度，如果不存在公共子路径，请你返回 0 。
 * 一个 子路径 指的是一条路径中连续的城市序列。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、m == paths.length
 * 3、2 <= m <= 10^5
 * 4、sum(paths[i].length) <= 10^5
 * 5、0 <= paths[i][j] < n
 * 6、paths[i] 中同一个城市不会连续重复出现。
 * 链接：https://leetcode.cn/problems/longest-common-subpath
"""

from typing import List

#
# @lc app=leetcode.cn id=1923 lang=python3
#
# [1923] 最长公共子路径
#

# @lc code=start
INF = 0x3c3c3c3c3c3c3c
MAX_N = 5 * 10**5 + 5  # 2倍串长度

rk = [0] * (MAX_N)
y = [0] * (MAX_N)
c = [0] * (MAX_N)
sa = [0] * (MAX_N)
height = [0] * (MAX_N)


def get_sa_base(s, m):
    n = len(s)
    global rk, y, c, sa, height
    for i in range(len(c)):
        c[i] = 0
    for i in range(1, n + 1):
        rk[i] = s[i - 1]
        c[rk[i]] += 1
    for i in range(1, m):
        c[i] += c[i - 1]
    for i in range(n, 0, -1):
        sa[c[rk[i]]] = i
        c[rk[i]] -= 1
    k = 1
    while (k <= n):
        num = 0
        for i in range(n - k + 1, n + 1):
            num += 1
            y[num] = i
        for i in range(1, n + 1):
            if (sa[i] > k):
                num += 1
                y[num] = sa[i] - k
        for i in range(1, m + 1):
            c[i] = 0
        for i in range(1, n + 1):
            c[rk[i]] += 1
        for i in range(1, m + 1):
            c[i] += c[i - 1]
        for i in range(n, 0, -1):
            sa[c[rk[y[i]]]] = y[i]
            c[rk[y[i]]] -= 1
            y[i] = 0
        rk, y = y, rk
        rk[sa[1]] = 1
        num = 1
        for i in range(2, n + 1):
            if (y[sa[i]] == y[sa[i - 1]] and (y[sa[i] + k] == y[sa[i - 1] + k])):
                rk[sa[i]] = num
            else:
                num += 1
                rk[sa[i]] = num
        if (num == n):
            break
        m = num
        k *= 2
    k = 0
    for i in range(1, n + 1):
        k = max(k - 1, 0) if k else k
        j = sa[rk[i] - 1]
        while (i + k <= n and j + k <= n and s[i + k - 1] == s[j + k - 1]):
            k += 1
        height[rk[i]] = k
    return sa, rk, height


class Solution:

    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # 后缀数组
        arr, mn_ln = [], INF
        MX = 10**5 + 1  # 值域范围
        for i, path in enumerate(paths):
            arr += path + [MX + i]
            mn_ln = min(mn_ln, len(path))
        ids = [INF] * (len(arr) + 1)
        id = 0
        for i, v in enumerate(arr):
            if v >= MX:
                id += 1
                ids[i] = len(paths) + 5
            else:
                ids[i] = id
        sa, rk, height = get_sa_base(arr, 2 * MX)
        ans = 0

        def check(v):
            ii = 2
            n = len(arr) + 1
            while ii < n:
                if height[ii] >= v:
                    j = ii
                    ss = set()
                    while j < n and height[j] >= v:
                        ss.add(ids[sa[j - 1] - 1])
                        ss.add(ids[sa[j] - 1])
                        j += 1
                    j -= 1
                    if len(ss) >= len(paths):
                        return True
                    ii = j
                ii += 1
            return False

        lo, hi = 0, mn_ln + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
                ans = mid
            else:
                hi = mid
        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    # print(Solution().longestCommonSubpath(69846, [[31172] for _ in range(100000)]))
    # 10
    arr = [[0, 1] * 5 + [2] + [0, 1] * 5] + [[0, 1] * 10]
    print(Solution().longestCommonSubpath(3, arr))
    # 3
    print(Solution().longestCommonSubpath(5, [[0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 3, 0, 1, 4, 0, 1, 0]]))
    # 1
    print(Solution().longestCommonSubpath(5, [[1, 2, 3, 4], [4, 1, 2, 3], [4]]))
    # 2
    print(Solution().longestCommonSubpath(
        955, [[825, 555], [825, 555], [825, 555], [825, 555], [825, 555], [825, 555], [825, 555], [825, 555]]))
    # 1
    print(Solution().longestCommonSubpath(5, paths=[[0, 1, 2, 3, 4], [4, 3, 2, 1, 0]]))
    # 2
    print(Solution().longestCommonSubpath(5, paths=[[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]]))
    # 0
    print(Solution().longestCommonSubpath(3, paths=[[0], [1], [2]]))
