package com.leo.leetcode.contest.q20220708;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 现有一个黑白棋游戏，初始时给出一排棋子，记作数组 chess，其中白色棋子记作 0，黑色棋子记作 1。用户可以每次交换 任意位置 的两颗棋子的位置。
 * 为了使得所有黑色棋子相连，请返回最少需要交换多少次。
 * 提示:
 * 1、1 <= chess.length <= 10^5
 * 2、chess[i] == 0 或 1.
 * 链接：https://leetcode.cn/contest/zj-future2022/problems/GVbKaI/
 */
public class Q2 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2().minSwaps(stringToIntegerArray("[1,0,1,0,1,0]")));
        // 0
        System.out.println(new Q2().minSwaps(stringToIntegerArray("[0,0,0,1,0]")));
        // 2
        System.out.println(new Q2().minSwaps(stringToIntegerArray("[1,1,0,1,0,1,0,0,1,0,1]")));
    }

    public int minSwaps(int[] chess) {
        int n = chess.length;
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + chess[i];
        }
        int len = preSum[n], ret = 0;
        for (int i = len; i <= n; i++) {
            ret = Math.max(ret, preSum[i] - preSum[i - len]);
        }
        return len - ret;
    }
}
