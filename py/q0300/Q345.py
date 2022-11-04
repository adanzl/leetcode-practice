"""
 * 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
 * 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
 * 提示：
 * 1、1 <= s.length <= 3 * 10^5
 * 2、s 由 可打印的 ASCII 字符组成
 * 链接：https://leetcode.cn/problems/reverse-vowels-of-a-string/
"""


class Solution:

    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        o = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        oo = [i for i in range(len(arr)) if arr[i] in o]
        for i in range(len(oo) // 2):
            arr[oo[i]], arr[oo[len(oo) - 1 - i]] = arr[oo[len(oo) - 1 - i]], arr[oo[i]]
        return ''.join(arr)


if __name__ == '__main__':
    # "holle"
    print(Solution().reverseVowels("hello"))
    # "leotcede"
    print(Solution().reverseVowels("leetcode"))