"""
 * 给你一个下标从 0 开始的字符串 s ，将 s 中的元素重新 排列 得到新的字符串 t ，它满足：
 * 1、所有辅音字母都在原来的位置上。更正式的，如果满足 0 <= i < s.length 的下标 i 处的 s[i] 是个辅音字母，那么 t[i] = s[i] 。
 * 2、元音字母都必须以他们的 ASCII 值按 非递减 顺序排列。更正式的，对于满足 0 <= i < j < s.length 的下标 i 和 j  ，
 *    如果 s[i] 和 s[j] 都是元音字母，那么 t[i] 的 ASCII 值不能大于 t[j] 的 ASCII 值。
 * 请你返回结果字母串。
 * 元音字母为 'a' ，'e' ，'i' ，'o' 和 'u' ，它们可能是小写字母也可能是大写字母，辅音字母是除了这 5 个字母以外的所有字母。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含英语字母表中的 大写 和 小写 字母。
 * 链接：https://leetcode.cn/problems/sort-vowels-in-a-string/
"""


class Solution:

    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        p_vowels = [(c, i) for i, c in enumerate(s) if c in vowels]
        ans = list(s)
        idx = 0
        for c, i in sorted(p_vowels):
            ans[p_vowels[idx][1]] = c
            idx += 1
        return ''.join(ans)


if __name__ == '__main__':
    # "lEOtcede"
    print(Solution().sortVowels("lEetcOde"))
    # "lYmpH"
    print(Solution().sortVowels("lYmpH"))