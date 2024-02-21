"""
 * 给你一个下标从 0 开始的字符串数组 words ，数组的长度为 n ，且包含下标从 0 开始的若干字符串。
 * 你可以执行以下操作 任意 次数（包括零次）：
 * 选择整数i、j、x和y，满足0 <= i, j < n，0 <= x < words[i].length，0 <= y < words[j].length，交换 字符 words[i][x] 和 words[j][y] 。
 * 返回一个整数，表示在执行一些操作后，words 中可以包含的回文字符串的 最大 数量。
 * 注意：在操作过程中，i 和 j 可以相等。
 * 提示：
 * 1、1 <= words.length <= 1000
 * 2、1 <= words[i].length <= 100
 * 3、words[i] 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/maximum-palindromes-after-operations/
"""
from typing import Counter, List


class Solution:

    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnt = Counter(''.join(words))
        ans = 0
        pairs = 0
        for v in cnt.values():
            pairs += v // 2
        for c in sorted([len(word) for word in words]):
            if pairs >= c // 2:
                ans += 1
                pairs -= c // 2
            else:
                break
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maxPalindromesAfterOperations(["abbb", "ba", "aa"]))
    # 2
    print(Solution().maxPalindromesAfterOperations(["abc", "ab"]))
    # 1
    print(Solution().maxPalindromesAfterOperations(["cd", "ef", "a"]))
