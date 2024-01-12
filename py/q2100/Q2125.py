"""
 * 银行内部的防盗安全装置已经激活。给你一个下标从 0 开始的二进制字符串数组 bank ，
 * 表示银行的平面图，这是一个大小为 m x n 的二维矩阵。 
 * bank[i] 表示第 i 行的设备分布，由若干 '0' 和若干 '1' 组成。
 * '0' 表示单元格是空的，而 '1' 表示单元格有一个安全设备。
 * 对任意两个安全设备而言，如果同时 满足下面两个条件，则二者之间存在 一个 激光束：
 * 1、两个设备位于两个 不同行 ：r1 和 r2 ，其中 r1 < r2 。
 * 2、满足 r1 < i < r2 的 所有 行 i ，都 没有安全设备 。
 * 激光束是独立的，也就是说，一个激光束既不会干扰另一个激光束，也不会与另一个激光束合并成一束。
 * 返回银行中激光束的总数量。
 * 提示：
 * 1、m == bank.length
 * 2、n == bank[i].length
 * 3、1 <= m, n <= 500
 * 4、bank[i][j] 为 '0' 或 '1'
 * 链接：https://leetcode.cn/problems/number-of-laser-beams-in-a-bank/
"""

from typing import List

#
# @lc app=leetcode.cn id=2125 lang=python3
#
# [2125] 银行中的激光束数量
#

# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, pre = 0, 0
        for line in bank:
            cur = 0
            for c in line:
                if c == '1':
                    cur += 1
                    ans += pre
            if cur:
                pre = cur
        return ans
# @lc code=end



if __name__ == '__main__':
    # 8
    print(Solution().numberOfBeams(["011001","000000","010100","001000"]))
    # 0
    print(Solution().numberOfBeams(["000","111","000"]))