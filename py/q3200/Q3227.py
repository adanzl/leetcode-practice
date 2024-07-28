"""
 * 小红和小明在玩一个字符串元音游戏。
 * 给你一个字符串 s，小红和小明将轮流参与游戏，小红 先 开始：
 * 1、在小红的回合，她必须移除 s 中包含 奇数 个元音的任意 非空 子字符串。
 * 2、在小明的回合，他必须移除 s 中包含 偶数 个元音的任意 非空 子字符串。
 * 第一个无法在其回合内进行移除操作的玩家输掉游戏。假设小红和小明都采取 最优策略 。
 * 如果小红赢得游戏，返回 true，否则返回 false。
 * 英文元音字母包括：a, e, i, o, 和 u。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/vowels-game-in-a-string/
"""


class Solution:

    def doesAliceWin(self, s: str) -> bool:
        return any([1 for c in s if c in 'aeiou'])


if __name__ == '__main__':
    # True
    print(Solution().doesAliceWin('ifld'))
    # True
    print(Solution().doesAliceWin("leetcoder"))
    # False
    print(Solution().doesAliceWin("bbcd"))
