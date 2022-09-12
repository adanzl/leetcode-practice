from typing import *
"""
 * 给你两个整数 n 和 k ，请你构造一个答案列表 answer ，该列表应当包含从 1 到 n 的 n 个不同正整数，并同时满足下述条件：
 * 假设该列表是 answer = [a1, a2, a3, ... , an] ，那么列表 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数。
 * 返回列表 answer 。如果存在多种答案，只需返回其中 任意一种 。
 * 提示：1 <= k < n <= 10^4
 * 链接：https://leetcode.cn/problems/beautiful-arrangement-ii
"""


class Solution:

    def constructArray(self, n: int, k: int) -> List[int]:
        v, end = n - k, n
        ans = list(range(1, v))
        while len(ans) < n:
            ans += [v]
            v += 1
            if end > v:
                ans += [end]
            end -= 1
        return ans


if __name__ == '__main__':
    print(Solution().constructArray(100, 50))
    print(Solution().constructArray(3, 2))  # [1, 3, 2]
