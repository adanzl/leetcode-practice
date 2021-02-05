package com.leo.leetcode.algorithm.q1400;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
 * 每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
 * 你的点数就是你拿到手中的所有卡牌的点数之和。
 * 给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
 * <p>
 * 提示：
 * 1、1 <= cardPoints.length <= 10^5
 * 2、1 <= cardPoints[i] <= 10^4
 * 3、1 <= k <= cardPoints.length
 * <p>
 * 链接：https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards
 */
public class Q1423 {

    public static void main(String[] args) {
        // 12
        System.out.println(new Q1423().maxScore(stringToIntegerArray("[1,2,3,4,5,6,1]"), 3));
        // 4
        System.out.println(new Q1423().maxScore(stringToIntegerArray("[2,2,2]"), 2));
        // 55
        System.out.println(new Q1423().maxScore(stringToIntegerArray("[9,7,7,9,7,7,9]"), 7));
        // 1
        System.out.println(new Q1423().maxScore(stringToIntegerArray("[1,1000,1]"), 1));
        // 202
        System.out.println(new Q1423().maxScore(stringToIntegerArray("[1,79,80,1,1,1,200,1]"), 3));
    }

    public int maxScore(int[] cardPoints, int k) {
        int score = 0, l = k - 1, r = cardPoints.length - 1;
        for (int i = 0; i < k; i++) score += cardPoints[i];
        int ret = score;
        while (r >= cardPoints.length - k) {
            score = score - cardPoints[l] + cardPoints[r];
            ret = Math.max(ret, score);
            l--;
            r--;
        }
        return ret;
    }
}
