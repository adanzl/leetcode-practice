package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

/**
 * 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
 * 设计一个算法使得这 m 个子数组各自和的最大值最小。 注意:
 * 数组长度 n 满足以下条件: 1 ≤ n ≤ 1000 1 ≤ m ≤ min(50, n) 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/split-array-largest-sum
 */
// TODO
class Q410 {

    public static void main(String[] args) {
        System.out.println(new Q410().splitArray(LCUtil.stringToIntegerArray("[7,2,5,10,8]"), 2)); // 18
    }

    public int splitArray(int[] nums, int m) {
        return 0;
    }
}