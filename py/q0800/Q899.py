"""
 * 给定一个字符串 s 和一个整数 k 。你可以从 s 的前 k 个字母中选择一个，并把它加到字符串的末尾。
 * 返回 在应用上述步骤的任意数量的移动后，字典上最小的字符串 。
 * 提示：
 * 1、1 <= k <= S.length <= 1000
 * 2、s 只由小写字母组成。
 * 链接：https://leetcode.cn/problems/orderly-queue/
"""


class Solution:

    def orderlyQueue(self, s: str, k: int) -> str:
        # 只要k不是1，就可以任意更改两个字符串的位置，所以可以是整体排序
        # 如果是1，则循环遍历一遍字符串，找到最小开头即可
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return ''.join(sorted(s))


if __name__ == '__main__':
    # "hku"
    print(Solution().orderlyQueue("kuh", 1))
    # "aaabc"
    print(Solution().orderlyQueue("baaca", k=3))
    # "acb"
    print(Solution().orderlyQueue("cba", k=1))
