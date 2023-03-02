"""
 * 给你一个字符数组 chars ，请使用下述算法压缩：
 * 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
 * 1、如果这一组长度为 1 ，则将字符追加到 s 中。
 * 2、否则，需要向 s 追加字符，后跟这一组的长度。
 * 压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
 * 请在 修改完输入数组后 ，返回该数组的新长度。
 * 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
 * 提示：
 * 1、1 <= chars.length <= 2000
 * 2、chars[i] 可以是小写英文字母、大写英文字母、数字或符号
 * 链接：https://leetcode.cn/problems/string-compression/
"""
from typing import List


class Solution:

    def compress(self, chars: List[str]) -> int:
        idx = 0
        lc, lcc = '', 0
        for c in chars:
            if c == lc:
                lcc += 1
            else:
                if lc != '':
                    chars[idx] = lc
                    idx += 1
                if lcc > 1:
                    for cc in str(lcc):
                        chars[idx] = cc
                        idx += 1
                lc = c
                lcc = 1

        if lc != '':
            chars[idx] = lc
            idx += 1
        if lcc > 1:
            for cc in str(lcc):
                chars[idx] = cc
                idx += 1
        return idx


if __name__ == '__main__':
    # 6
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
    # 1
    print(Solution().compress(["a"]))
    # 4
    print(Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
