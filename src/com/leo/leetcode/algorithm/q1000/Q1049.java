package com.leo.leetcode.algorithm.q1000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 有一堆石头，用整数数组  stones 表示。其中  stones[i] 表示第 i 块石头的重量。
 * 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为  x 和  y，且  x <= y。那么粉碎的可能结果如下：
 * 如果  x == y，那么两块石头都会被完全粉碎；
 * 如果  x != y，那么重量为  x  的石头将会完全粉碎，而重量为  y  的石头新重量为  y-x。
 * 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
 * <p>
 * 提示：
 * 1、1 <= stones.length <= 30
 * 2、1 <= stones[i] <= 100
 * <p>
 * 链接：https://leetcode-cn.com/problems/last-stone-weight-ii
 */
public class Q1049 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q1049().lastStoneWeightII(stringToIntegerArray("[2,7,4,1,8,1]")));
        // 5
        System.out.println(new Q1049().lastStoneWeightII(stringToIntegerArray("[31,26,33,21,40]")));
        // 1
        System.out.println(new Q1049().lastStoneWeightII(stringToIntegerArray("[1,2]")));
        // 1
        System.out.println(new Q1049().lastStoneWeightII(stringToIntegerArray("[1]")));
    }

    public int lastStoneWeightII(int[] stones) {
        int sum = 0;
        for (int v : stones) sum += v;
        int limit = sum / 2;
        int[] dp = new int[limit + 1];
        for (int stone : stones) {
            for (int j = limit; j > 0; j--) {
                if (stone <= j) dp[j] = Math.max(dp[j], dp[j - stone] + stone);
            }
        }
        return sum - dp[limit] * 2;
    }
}
