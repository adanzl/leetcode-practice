"""
 * 在一个仓库里，有一排条形码，其中第 i 个条形码为 bar_codes[i]。
 * 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
 * 提示：
 * 1、1 <= bar_codes.length <= 10000
 * 2、1 <= bar_codes[i] <= 10000
 * 链接：https://leetcode.cn/problems/distant-barcodes/
"""
from collections import Counter
from typing import List


class Solution:

    def rearrangeBarcodes(self, bar_codes: List[int]) -> List[int]:
        n = len(bar_codes)
        ans = [0] * n
        cnt = Counter(bar_codes)
        arr = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        idx = 0
        for v, c in arr:
            while c:
                ans[idx] = v
                idx += 2
                if idx >= n:
                    idx = 1
                c -= 1
        return ans


if __name__ == '__main__':
    # [1, 2, 1, 2, 1, 2]
    print(Solution().rearrangeBarcodes([1, 1, 1, 2, 2, 2]))
    # [1, 2, 1, 2, 1, 3, 1, 3]
    print(Solution().rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))