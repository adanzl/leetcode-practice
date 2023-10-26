"""
 * 给定整数 p 和 m ，一个长度为 k 且下标从 0 开始的字符串 s 的哈希值按照如下函数计算：
 * hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.
 * 其中 val(s[i]) 表示 s[i] 在字母表中的下标，从 val('a') = 1 到 val('z') = 26 。
 * 给你一个字符串 s 和整数 power，modulo，k 和 hashValue 。
 * 请你返回 s 中 第一个 长度为 k 的 子串 sub ，满足 hash(sub, power, modulo) == hashValue 。
 * 测试数据保证一定 存在 至少一个这样的子串。
 * 子串 定义为一个字符串中连续非空字符组成的序列。
 * 提示：
 * 1、1 <= k <= s.length <= 2 * 10^4
 * 2、1 <= power, modulo <= 10^9
 * 3、0 <= hashValue < modulo
 * 4、s 只包含小写英文字母。
 * 5、测试数据保证一定 存在 满足条件的子串。
 * 链接：https://leetcode.cn/problems/find-substring-with-given-hash-value/
"""

from typing import List

#
# @lc app=leetcode.cn id=2156 lang=python3
#
# [2156] 查找给定哈希值的子串
#


# @lc code=start
class Solution:

    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        sn = [ord(c) - ord('a') + 1 for c in s]
        ans_idx = -1
        val = 0
        n = len(sn)
        for i in range(n - 1, -1, -1):
            val = (val * power + sn[i]) % modulo
            if i <= n - 1 - k:
                val = (val - sn[i + k] * pow(power, k, modulo)) % modulo
            if i <= n - k and val == hashValue:
                ans_idx = i
        return s[ans_idx:ans_idx + k]


# @lc code=end

if __name__ == '__main__':
    # c
    print(Solution().subStrHash("abc", 7, 10, 1, 3))
    # xmmhdakfursinye
    print(Solution().subStrHash("xmmhdakfursinye", 96, 45, 15, 21))
    # "ee"
    print(Solution().subStrHash("leetcode", power=7, modulo=20, k=2, hashValue=0))
    # "fbx"
    print(Solution().subStrHash("fbxzaad", power=31, modulo=100, k=3, hashValue=32))
