"""
 * 给你一个字符串 s 和一个正整数 k 。
 * 用 vowels 和 consonants 分别表示字符串中元音字母和辅音字母的数量。
 * 如果某个字符串满足以下条件，则称其为 美丽字符串 ：
 * 1、vowels == consonants，即元音字母和辅音字母的数量相等。
 * 2、(vowels * consonants) % k == 0，即元音字母和辅音字母的数量的乘积能被 k 整除。
 * 返回字符串 s 中 非空美丽子字符串 的数量。
 * 子字符串是字符串中的一个连续字符序列。
 * 英语中的 元音字母 为 'a'、'e'、'i'、'o' 和 'u' 。
 * 英语中的 辅音字母 为除了元音字母之外的所有字母。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、1 <= k <= 1000
 * 3、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/count-beautiful-substrings-i/
"""
from collections import Counter


class Solution:

    def beautifulSubstrings(self, s: str, k: int) -> int:
        k = self.sqrt(k * 4)
        cnt = Counter([tuple((k - 1, 0))])  # k-1 和 -1 同余
        ans = pre_sum = 0
        for i, c in enumerate(s):
            pre_sum += 1 if c in "aeiou" else -1
            p = (i % k, pre_sum)
            ans += cnt[p]
            cnt[p] += 1
        return ans

    def sqrt(self, n: int) -> int:
        res = 1
        i = 2
        while i * i <= n:
            i2 = i * i
            while n % i2 == 0:
                res *= i
                n //= i2
            if n % i == 0:
                res *= i
                n //= i
            i += 1
        if n > 1:
            res *= n
        return res


if __name__ == '__main__':
    # 2
    print(Solution().beautifulSubstrings("baeyh", k=2))
    # 3
    print(Solution().beautifulSubstrings("abba", k=1))
    # 0
    print(Solution().beautifulSubstrings("bcdf", k=1))
