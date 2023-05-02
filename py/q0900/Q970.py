"""
 * 给定三个整数 x 、 y 和 bound ，返回 值小于或等于 bound 的所有 强整数 组成的列表 。
 * 如果某一整数可以表示为 xi + yj ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个 强整数 。
 * 你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。
 * 提示：
 * 1、1 <= x, y <= 100
 * 2、0 <= bound <= 10^6
 * 链接：https://leetcode.cn/problems/powerful-integers/
"""
from typing import List


class Solution:

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        sx, sy = [1], [1]
        v = x
        while x != 1 and v < bound:
            sx.append(v)
            v *= x
        v = y
        while y != 1 and v < bound:
            sy.append(v)
            v *= y
        ans = set()
        for v in sx:
            for u in sy:
                if u + v > bound: break
                ans.add(u + v)
        return list(ans)


if __name__ == '__main__':
    # [2,3,4,5,7,9,10]
    print(Solution().powerfulIntegers(2, y=3, bound=10))
    # [2,4,6,8,10,14]
    print(Solution().powerfulIntegers(3, y=5, bound=15))
