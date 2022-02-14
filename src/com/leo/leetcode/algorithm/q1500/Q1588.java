package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
 * 子数组 定义为原数组中的一个连续子序列。
 * 请你返回 arr 中 所有奇数长度子数组的和 。
 * 提示：
 * 1、1 <= arr.length <= 100
 * 2、1 <= arr[i] <= 1000
 * 链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
 */
public class Q1588 {

    public static void main(String[] args) {
        // 58
        System.out.println(new Q1588().sumOddLengthSubArrays(stringToIntegerArray("[1,4,2,5,3]")));
        // 3
        System.out.println(new Q1588().sumOddLengthSubArrays(stringToIntegerArray("[1,2]")));
        // 66
        System.out.println(new Q1588().sumOddLengthSubArrays(stringToIntegerArray("[10,11,12]")));
    }

    public int sumOddLengthSubArrays(int[] arr) {
        int ret = 0;
        for (int i = 0; i < arr.length; i++) {
            int rightCount = arr.length - i - 1;
            int leftOdd = (i + 1) / 2;
            int rightOdd = (rightCount + 1) / 2;
            int leftEven = i / 2 + 1;
            int rightEven = rightCount / 2 + 1;
            ret += arr[i] * (leftOdd * rightOdd + leftEven * rightEven);
        }
        return ret;
    }
}
