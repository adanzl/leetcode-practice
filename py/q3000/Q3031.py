"""
 * 给你一个下标从 0 开始的字符串 word 和一个整数 k 。
 * 在每一秒，你必须执行以下操作：
 * 1、移除 word 的前 k 个字符。
 * 2、在 word 的末尾添加 k 个任意字符。
 * 注意 添加的字符不必和移除的字符相同。但是，必须在每一秒钟都执行 两种 操作。
 * 返回将 word 恢复到其 初始 状态所需的 最短 时间（该时间必须大于零）。
 * 提示：
 * 1、1 <= word.length <= 10^6
 * 2、1 <= k <= word.length
 * 3、word仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-ii/
"""


class Solution:

    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        def get_z(s):
            l = r = 0
            n = len(s)
            z = [0] * n
            z[0] = n
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z

        z, n = get_z(word), len(word)
        ans = 1
        for i in range(k, n, k):
            if z[i] == n - i:
                break
            ans += 1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().minimumTimeToInitialState("abcbabcd", k=2))
    # 2
    print(Solution().minimumTimeToInitialState("abacaba", k=3))
    # 1
    print(Solution().minimumTimeToInitialState("abacaba", k=4))
