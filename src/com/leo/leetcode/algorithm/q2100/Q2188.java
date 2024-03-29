package com.leo.leetcode.algorithm.q2100;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个下标从 0 开始的二维整数数组 tires ，其中 tires[i] = [fi, ri] 表示第 i 种轮胎如果连续使用，第 x 圈需要耗时 fi * ri^(x-1) 秒。
 * 比方说，如果 fi = 3 且 ri = 2 ，且一直使用这种类型的同一条轮胎，那么该轮胎完成第 1 圈赛道耗时 3 秒，完成第 2 圈耗时 3 * 2 = 6 秒，完成第 3 圈耗时 3 * 22 = 12 秒，依次类推。
 * 同时给你一个整数 changeTime 和一个整数 numLaps 。
 * 比赛总共包含 numLaps 圈，你可以选择 任意 一种轮胎开始比赛。每一种轮胎都有 无数条 。每一圈后，你可以选择耗费 changeTime 秒 换成 任意一种轮胎（也可以换成当前种类的新轮胎）。
 * 请你返回完成比赛需要耗费的 最少 时间。
 * 提示：
 * 1、1 <= tires.length <= 10^5
 * 2、tires[i].length == 2
 * 3、1 <= fi, changeTime <= 10^5
 * 4、2 <= ri <= 10^5
 * 5、1 <= numLaps <= 1000
 * 链接：https://leetcode-cn.com/problems/minimum-time-to-finish-the-race
 */
public class Q2188 {

    public static void main(String[] args) {
        // 100084915
        System.out.println(new Q2188().minimumFinishTime(stringToInt2dArray("[[100000,100000]]"), 85, 1000));
        // 17205
        System.out.println(new Q2188().minimumFinishTime(stringToInt2dArray("[[97,2]]"), 85, 95));
        // 21
        System.out.println(new Q2188().minimumFinishTime(stringToInt2dArray("[[2,3],[3,4]]"), 5, 4));
        // 25
        System.out.println(new Q2188().minimumFinishTime(stringToInt2dArray("[[1,10],[2,2],[3,4]]"), 6, 5));
    }

    public int minimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        long[] dp = new long[numLaps + 1];
        long[] tireTimes = new long[tires.length];
        long[] tireSumTimes = new long[tires.length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        for (int i = 0; i < tires.length; i++) {
            tireTimes[i] = tires[i][0];
            tireSumTimes[i] = tires[i][0];
            dp[1] = Math.min(dp[1], tireTimes[i]);
        }
        for (int i = 1; i <= numLaps; i++) {
            for (int j = 0; i > 1 && j < tires.length; j++) {
                int[] tire = tires[j];
                tireTimes[j] = Math.min(tire[1] * tireTimes[j], Integer.MAX_VALUE);
                tireSumTimes[j] = Math.min(tireTimes[j] + tireSumTimes[j], Integer.MAX_VALUE);
                dp[i] = Math.min(dp[i], tireSumTimes[j]);
            }
            for (int j = 1; j <= i / 2; j++) {
                dp[i] = Math.min(dp[i], dp[i - j] + dp[j] + changeTime);
            }
        }
        return (int) dp[numLaps];
    }
}
