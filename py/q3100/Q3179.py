"""
 * 给你两个整数 n 和 k。
 * 最初，你有一个长度为 n 的整数数组 a，对所有 0 <= i <= n - 1，都有 a[i] = 1 。
 * 每过一秒，你会同时更新每个元素为其前面所有元素的和加上该元素本身。
 * 例如，一秒后，a[0] 保持不变，a[1] 变为 a[0] + a[1]，a[2] 变为 a[0] + a[1] + a[2]，以此类推。
 * 返回 k 秒后 a[n - 1] 的值。
 * 由于答案可能非常大，返回其对 10^9 + 7 取余 后的结果。
 * 提示：1 <= n, k <= 1000
 * 链接：https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds/
"""


class Solution:

    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr = [1] * n
        for _ in range(k):
            for j in range(1, n):
                arr[j] = (arr[j] + arr[j - 1]) % (10**9 + 7)
        return arr[-1]


if __name__ == '__main__':
    # 56
    print(Solution().valueAfterKSeconds(4, k=5))
    # 35
    print(Solution().valueAfterKSeconds(5, k=3))
