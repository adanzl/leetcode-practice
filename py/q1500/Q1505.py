"""
 * 给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。
 * 你可以交换这个整数相邻数位的数字 最多 k 次。
 * 请你返回你能得到的最小整数，并以字符串形式返回。
 * 提示：
 * 1、1 <= num.length <= 30000
 * 2、num 只包含 数字 且不含有 前导 0 。
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
"""

import bisect
from typing import Deque

#
# @lc app=leetcode.cn id=1505 lang=python3
#
# [1505] 最多 K 次交换相邻数位后得到的最小整数
#

# @lc code=start


class Solution:

    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        ans = []
        n_pos = [Deque() for _ in range(10)]
        for i, c in enumerate(num):
            # 按照数字分组下标
            n_pos[int(c)].append(i)
        p_ids = []
        while k:
            # 每次尝试将最小的数字放入答案
            for nn in range(10):
                if n_pos[nn]:
                    idx: int = n_pos[nn][0]
                    ii = bisect.bisect_left(p_ids, idx)
                    d = idx - len(ans) + len(p_ids) - ii
                    if d <= k:
                        bisect.insort(p_ids, idx)
                        ans.append(num[idx])
                        k -= d
                        n_pos[nn].popleft()
                        # 找到可以放入的最小值则退出
                        break
            else:
                # 没有可以放入数字了则退出尝试
                break
        s = set(p_ids)
        for i, c in enumerate(num):
            if i not in s:
                ans.append(c)
        return "".join(ans)


# @lc code=end

if __name__ == '__main__':
    # "36789"
    print(Solution().minInteger("36789", k=1000))
    # "010"
    print(Solution().minInteger("100", k=1))
    # "124498948179"
    print(Solution().minInteger("294984148179", k=11))
    # "0009900"
    print(Solution().minInteger("9000900", k=3))
    # "0345989723478563548"
    print(Solution().minInteger("9438957234785635408", k=23))
    # "1342"
    print(Solution().minInteger("4321", k=4))
    # "22"
    print(Solution().minInteger("22", k=22))
