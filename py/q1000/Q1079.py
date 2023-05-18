"""
 * 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
 * 注意：本题中，每个活字字模只能使用一次。
 * 提示：
 * 1、1 <= tiles.length <= 7
 * 2、tiles 由大写英文字母组成
 * 链接：https://leetcode.cn/problems/letter-tile-possibilities/
"""
import math
from typing import Counter


class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        tl = "".join(sorted(tiles))
        s = set()

        def func(tl):
            if len(tl) == 0 or tl in s: return 0
            s.add(tl)
            ret, n = 0, len(tl)
            for i in range(n):
                if i > 0 and tl[i] == tl[i - 1]: continue
                ret += func(tl[:i] + tl[i + 1:])
            cnt = Counter(tl)
            vv = math.factorial(n)
            for v in cnt.values():
                vv //= math.factorial(v)
            return ret + vv

        return func(tl)


if __name__ == '__main__':
    # 8
    print(Solution().numTilePossibilities("AAB"))
    # 188
    print(Solution().numTilePossibilities("AAABBC"))
    # 7
    print(Solution().numTilePossibilities("AAAAAAA"))
    # 1
    print(Solution().numTilePossibilities("V"))