package com.leo.leetcode.algorithm.q1000;

/**
 * 给定正整数数组A，A[i]表示第 i 个观光景点的评分，并且两个景点i 和j之间的距离为j - i。
 * 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i- j）：景点的评分之和减去它们两者之间的距离。
 * 返回一对观光景点能取得的最高分。
 * 链接：https://leetcode-cn.com/problems/best-sightseeing-pair
 */
public class Q1014 {
    public static void main(String[] args) {
        System.out.println(new Q1014().maxScoreSightseeingPair(new int[]{4, 3, 2, 5, 1, 8, 10})); // 17
        System.out.println(new Q1014().maxScoreSightseeingPair(new int[]{8, 1, 5, 2, 6})); // 11
    }

    public int maxScoreSightseeingPair(int[] A) {
        int p = A[0]; // A[i] + i, A[j] - j
        int out = 0;
        for (int i = 1; i < A.length; i++) {
            out = Math.max(out, p + A[i] - i);
            p = Math.max(p, A[i] + i);
        }
        return out;
    }
}
