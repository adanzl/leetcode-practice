package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 对数组 nums 执行 按位与 相当于对数组 nums 中的所有整数执行 按位与 。
 * 1、例如，对 nums = [1, 5, 3] 来说，按位与等于 1 & 5 & 3 = 1 。
 * 2、同样，对 nums = [7] 而言，按位与等于 7 。
 * 给你一个正整数数组 candidates 。计算 candidates 中的数字每种组合下 按位与 的结果。 candidates 中的每个数字在每种组合中只能使用 一次 。
 * 返回按位与结果大于 0 的 最长 组合的长度。
 * 提示：
 * 1、1 <= candidates.length <= 10^5
 * 2、1 <= candidates[i] <= 10^7
 * 链接：https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero
 */
public class Q2275 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2275().largestCombination(stringToIntegerArray("[8,8]")));
        // 4
        System.out.println(new Q2275().largestCombination(stringToIntegerArray("[16,17,71,62,12,24,14]")));
    }

    public int largestCombination(int[] candidates) {
        int max = 0;
        int[] mark = new int[32];
        for (int candidate : candidates) {
            for (int i = 0; i < mark.length; i++) {
                if ((candidate & (1 << i)) != 0) mark[i]++;
                max = Math.max(max, mark[i]);
            }
        }
        return max;
    }
}
