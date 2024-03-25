"""
 * 给你一个下标从 0 开始的字符串 word 和一个整数 k 。
 * 在每一秒，你必须执行以下操作：
 * 1、移除 word 的前 k 个字符。
 * 2、在 word 的末尾添加 k 个任意字符。
 * 注意 添加的字符不必和移除的字符相同。但是，必须在每一秒钟都执行 两种 操作。
 * 返回将 word 恢复到其 初始 状态所需的 最短 时间（该时间必须大于零）。
 * 提示：
 * 1、1 <= word.length <= 50
 * 2、1 <= k <= word.length
 * 3、word仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-i/
"""


class Solution:

    def minimumTimeToInitialState(self, s: str, k: int) -> int:
        n = len(s)
        z = [0] * n  # KMP z函数
        l = r = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(z[i - l], r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                l, r = i, i + z[i]
                z[i] += 1
            if i % k == 0 and z[i] >= n - i:
                return i // k
        return (n - 1) // k + 1


if __name__ == '__main__':
    # 1
    print(Solution().minimumTimeToInitialState("abacaba", k=4))
    # 2
    print(Solution().minimumTimeToInitialState("abacaba", k=3))
    # 4
    print(Solution().minimumTimeToInitialState("abcbabcd", k=2))
