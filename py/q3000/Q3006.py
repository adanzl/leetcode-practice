"""
 * 给你一个下标从 0 开始的字符串 s 、字符串 a 、字符串 b 和一个整数 k 。
 * 如果下标 i 满足以下条件，则认为它是一个 美丽下标：
 * 1、0 <= i <= s.length - a.length
 * 2、s[i..(i + a.length - 1)] == a
 * 3、存在下标 j 使得：
 *      0 <= j <= s.length - b.length
 *      s[j..(j + b.length - 1)] == b
 *      |j - i| <= k
 * 以数组形式按 从小到大排序 返回美丽下标。
 * 提示：
 * 1、1 <= k <= s.length <= 10^5
 * 2、1 <= a.length, b.length <= 10
 * 3、s、a、和 b 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-i/
"""
import bisect
from typing import List


class Solution:

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        idx_a, idx_b = [], []
        for i in range(len(s)):
            if i <= len(s) - len(a):
                if s[i:i + len(a)] == a:
                    idx_a.append(i)
            if i <= len(s) - len(b):
                if s[i:i + len(b)] == b:
                    idx_b.append(i)
        for i_a in idx_a:
            i0 = bisect.bisect_left(idx_b, i_a - k)
            i1 = bisect.bisect_left(idx_b, i_a + k)
            if i0 != i1 or (i0 < len(idx_b) and (idx_b[i0] == i_a - k or idx_b[i0] == i_a + k)):
                ans.append(i_a)
        return ans


if __name__ == '__main__':
    # [16, 33]
    print(Solution().beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15))
    # []
    print(Solution().beautifulIndices("opzufozzl", "opz", "foz", 3))
    # [0]
    print(Solution().beautifulIndices("abcd", a="a", b="a", k=4))
