"""
 * 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。
 * 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
 * 注意：
 * 1、字母 x 的 频率 是这个字母在字符串中出现的次数。
 * 2、你 必须 恰好删除一个字母，不能一个字母都不删除。
 * 提示：
 * 1、2 <= word.length <= 100
 * 2、word 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/remove-letter-to-equalize-frequency/
"""
from typing import *


class Solution:

    def equalFrequency(self, word: str) -> bool:
        if len(word) == 2: return True
        w = Counter(word)
        ks = list(w.keys())
        for k in ks:
            w[k] -= 1
            if w[k] == 0:
                del w[k]
            c = Counter(w.values())
            if len(c) == 1: return True
            w[k] += 1
        return False


if __name__ == '__main__':
    # true
    print(Solution().equalFrequency("bac"))
    # True
    print(Solution().equalFrequency("cccaa"))
    # False
    print(Solution().equalFrequency("aaaaacc"))
    # True
    print(Solution().equalFrequency("aaaaa"))
    # false
    print(Solution().equalFrequency("cbccca"))
    # true
    print(Solution().equalFrequency("acbda"))
    # true
    print(Solution().equalFrequency("aac"))
    # false
    print(Solution().equalFrequency("aaaccc"))