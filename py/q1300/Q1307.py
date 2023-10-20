"""
 * 给你一个方程，左边用 words 表示，右边用 result 表示。
 * 你需要根据以下规则检查方程是否可解：
 * 1、每个字符都会被解码成一位数字（0 - 9）。
 * 2、每对不同的字符必须映射到不同的数字。
 * 3、每个 words[i] 和 result 都会被解码成一个没有前导零的数字。
 * 4、左侧数字之和（words）等于右侧数字（result）。 
 * 如果方程可解，返回 True，否则返回 False。
 * 提示：
 * 1、2 <= words.length <= 5
 * 2、1 <= words[i].length, results.length <= 7
 * 3、words[i], result 只含有大写英文字母
 * 4、表达式中使用的不同字符数最大为 10
 * 链接：https://leetcode.cn/problems/verbal-arithmetic-puzzle/
"""

from collections import Counter
from typing import List

#
# @lc app=leetcode.cn id=1307 lang=python3
#
# [1307] 口算难题
#


# @lc code=start
class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        # 边界情况绝对无解
        if all(len(word) + 1 < len(result) for word in words):
            return False
        wc = Counter()
        n_zero = set()  # 列出不能为0的字母
        for word in words:
            if len(word) > 1: n_zero.add(word[0])
            for i in range(len(word) - 1, -1, -1):
                wc[word[i]] += 10**(len(word) - 1 - i)
        for i in range(len(result) - 1, -1, -1):
            wc[result[i]] -= 10**(len(result) - 1 - i)
        if len(result) > 1: n_zero.add(result[0])
        n = len(wc)
        arr = sorted([[v, k] for k, v in wc.items()], key=lambda x: -abs(x[0]))

        used = [False] * 10

        def calc_range(i):
            # 预判后续可能性，计算出剩余的可能最大最小值
            ss = sorted([ii for ii in range(10) if not used[ii]], reverse=True)  # 可用数字大-小
            po = [arr[ii][0] for ii in range(i, n) if arr[ii][0] > 0]  # 正系数
            ng = [arr[ii][0] for ii in range(i, n) if arr[ii][0] < 0]  # 负系数
            mn, mx = 0, 0
            for a, b in zip(po, ss):
                mx += a * b
            for a, b in zip(ng, ss[::-1]):
                mx += a * b
            for a, b in zip(ng, ss):
                mn += a * b
            for a, b in zip(po, ss[::-1]):
                mn += a * b
            return mx, mn

        def dfs(i, sm):
            if i == n: return sm == 0
            mx, mn = calc_range(i)  # 利用后续可能性进行剪枝
            if sm + mx < 0 or sm + mn > 0: return False
            for v in range(1 if arr[i][1] in n_zero else 0, 10):
                if used[v]: continue
                used[v] = True
                if dfs(i + 1, sm + arr[i][0] * v): return True
                used[v] = False
            return False

        return dfs(0, 0)


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isSolvable(["THIS", "IS", "TOO"], result="FUNNY"))
    # True
    print(Solution().isSolvable(["SEND", "MORE"], result="MONEY"))
    # True
    print(Solution().isSolvable(["SIX", "SEVEN", "SEVEN"], result="TWENTY"))
    # False
    print(Solution().isSolvable(["LEET", "CODE"], result="POINT"))