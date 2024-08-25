"""
 * 给你一个正整数数组 nums 。
 * 如果我们执行以下操作 至多一次 可以让两个整数 x 和 y 相等，那么我们称这个数对是 近似相等 的：
 * 选择 x 或者 y  之一，将这个数字中的两个数位交换。
 * 请你返回 nums 中，下标 i 和 j 满足 i < j 且 nums[i] 和 nums[j] 近似相等 的数对数目。
 * 注意 ，执行操作后一个整数可以有前导 0 。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/count-almost-equal-pairs-i/
"""
from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        for num in nums:
            s = str(num)
            c_s = Counter(s)
            for k, v in cnt.items():
                if num == k:
                    ans += v
                else:
                    pre = str(k)
                    c_d = Counter()
                    c_pre = Counter(pre)
                    for kk in range(10):
                        c_d[str(kk)] = abs(c_pre[str(kk)] - c_s[str(kk)])
                    dd = 0
                    for kk in range(1, 10):
                        dd += abs(c_d[str(kk)])
                    if dd: continue
                    i_s, i_pre, diff, z = len(s) - 1, len(pre) - 1, 0, 0
                    while i_s >= 0 and i_pre >= 0:
                        if s[i_s] == pre[i_pre]:
                            ...
                        elif s[i_s] == '0' or pre[i_pre] == '0':
                            z += 1
                        else:
                            diff += 1
                        i_s -= 1
                        i_pre -= 1
                        if diff + z > 2: break
                    while i_s >= 0 and s[i_s] == '0':
                        i_s -= 1
                    while i_pre >= 0 and pre[i_pre] == '0':
                        i_pre -= 1
                    if diff + z + i_pre + 1 + i_s + 1 <= 2:
                        ans += v
            cnt[num] += 1
        return ans


if __name__ == '__main__':
    # 44
    print(Solution().countPairs([
        886595, 767627, 6691, 593887, 857750, 919155, 830918, 593887, 593788, 593788, 660078, 598873, 310196, 668007,
        597883, 983587, 897853, 668700, 435383, 953887, 631608, 897853, 953887, 240754, 593887, 597883, 455127, 627877,
        643862, 660087, 893587, 129173, 228736, 627877, 775850, 875750, 500701, 830255, 751
    ]))
    # 23
    print(Solution().countPairs([
        490693, 900498, 448195, 24359, 126032, 584252, 26132, 124479, 586672, 855404, 24359, 418495, 243450, 106232,
        690685, 410981, 871863, 419180, 242524, 23549, 284759, 26132, 271146, 966337, 781863, 418495, 242524, 126032,
        411980, 621032, 271641, 25349, 900894
    ]))
    # 1
    print(Solution().countPairs([490693, 900498, 448195, 24359, 126032, 584252, 26132]))
    # 48
    print(Solution().countPairs([
        226726, 387862, 880512, 611522, 343461, 420841, 334461, 10813, 226726, 334461, 80113, 314364, 10813, 163067,
        134364, 332548, 413463, 343416, 236429, 164332, 566432, 226726, 334164, 343461, 143463, 163229, 667555, 667555,
        343461, 657565, 343461, 770521, 285866, 930657, 236429, 502387, 313446, 334461, 12219, 163760
    ]))
    # 2
    print(Solution().countPairs([3, 12, 30, 17, 21]))
    # 1
    print(Solution().countPairs([11, 8, 10, 5, 14, 8]))
    # 10
    print(Solution().countPairs([1, 1, 1, 1, 1]))
    # 0
    print(Solution().countPairs([123, 231]))
