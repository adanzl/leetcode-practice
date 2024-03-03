"""
 * 给你一个字符串 word，由 不同 小写英文字母组成。
 * 电话键盘上的按键与 不同 小写英文字母集合相映射，可以通过按压按键来组成单词。
 * 例如，按键 2 对应 ["a","b","c"]，我们需要按一次键来输入 "a"，按两次键来输入 "b"，按三次键来输入 "c"。
 * 现在允许你将编号为 2 到 9 的按键重新映射到 不同 字母集合。
 * 每个按键可以映射到 任意数量 的字母，但每个字母 必须 恰好 映射到 一个 按键上。
 * 你需要找到输入字符串 word 所需的 最少 按键次数。
 * 返回重新映射按键后输入 word 所需的 最少 按键次数。
 * 下面给出了一种电话键盘上字母到按键的映射作为示例。注意 1，*，# 和 0 不 对应任何字母。
 * 提示：
 * 1、1 <= word.length <= 26
 * 2、word 仅由小写英文字母组成。
 * 3、word 中的所有字母互不相同。
 * 链接：https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-i/
"""
from typing import Counter


class Solution:

    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8: return n
        cnt = Counter(word)
        ans = 0
        for i, v in enumerate(sorted(cnt.values(), reverse=True)):
            a = i // 8
            ans += (a + 1) * v
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().minimumPushes("abcde"))
    # 12
    print(Solution().minimumPushes("xycdefghij"))
