package com.leo.leetcode.algorithm.q2000;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 现有一份 n + m 次投掷单个 六面 骰子的观测数据，骰子的每个面从 1 到 6 编号。观测数据中缺失了 n 份，你手上只拿到剩余 m 次投掷的数据。
 * 幸好你有之前计算过的这 n + m 次投掷数据的 平均值 。
 * 给你一个长度为 m 的整数数组 rolls ，其中 rolls[i] 是第 i 次观测的值。同时给你两个整数 mean 和 n 。
 * 返回一个长度为 n 的数组，包含所有缺失的观测数据，且满足这 n + m 次投掷的 平均值 是 mean 。如果存在多组符合要求的答案，只需要返回其中任意一组即可。
 * 如果不存在答案，返回一个空数组。
 * k 个数字的 平均值 为这些数字求和后再除以 k 。
 * 注意 mean 是一个整数，所以 n + m 次投掷的总和需要被 n + m 整除。
 * 提示：
 * 1、m == rolls.length
 * 2、1 <= n, m <= 10^5
 * 3、1 <= rolls[i], mean <= 6
 * 链接：https://leetcode-cn.com/problems/find-missing-observations
 */
public class Q2028 {

    public static void main(String[] args) {
        // [6,6]
        System.out.println(Arrays.toString(new Q2028().missingRolls(stringToIntegerArray("[3,2,4,3]"), 4, 2)));
        // [2,3,2,2]
        System.out.println(Arrays.toString(new Q2028().missingRolls(stringToIntegerArray("[1,5,6]"), 3, 4)));
        // []
        System.out.println(Arrays.toString(new Q2028().missingRolls(stringToIntegerArray("[1,2,3,4]"), 6, 4)));
        // [5]
        System.out.println(Arrays.toString(new Q2028().missingRolls(stringToIntegerArray("[1]"), 3, 1)));
    }

    public int[] missingRolls(int[] rolls, int mean, int n) {
        int[] ret = new int[n];
        int m = rolls.length, sum = mean * (n + m), sumM = 0;
        for (int roll : rolls) sumM += roll;
        sum -= sumM;
        if (sum < n || sum > 6 * n) return new int[0];
        sum -= n;
        for (int i = 0; i < n; i++) {
            if (sum > 0) {
                ret[i] += Math.min(sum, 5) + 1;
                sum -= ret[i] - 1;
            } else {
                ret[i] = 1;
            }
        }
        return ret;
    }
}
