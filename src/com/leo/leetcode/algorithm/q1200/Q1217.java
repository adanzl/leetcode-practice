package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 有 n 个筹码。第 i 个筹码的位置是 position[i] 。
 * 我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:
 * 1、position[i] + 2 或 position[i] - 2 ，此时 cost = 0
 * 2、position[i] + 1 或 position[i] - 1 ，此时 cost = 1
 * 返回将所有筹码移动到同一位置上所需要的 最小代价 。
 * 提示：
 * 1、1 <= chips.length <= 100
 * 2、1 <= chips[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position
 */
public class Q1217 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q1217().minCostToMoveChips(stringToIntegerArray("[1,2,3]")));
        // 2
        System.out.println(new Q1217().minCostToMoveChips(stringToIntegerArray("[2,2,2,3,3]")));
        // 1
        System.out.println(new Q1217().minCostToMoveChips(stringToIntegerArray("[1,1000000000]")));
    }

    public int minCostToMoveChips(int[] position) {
        int odd = 0, even = 0;
        for (int pos : position) {
            if ((pos & 1) == 1) odd++;
            else even++;
        }
        return Math.min(odd, even);
    }
}
