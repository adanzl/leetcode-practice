package com.leo.leetcode.algorithm.q0600;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
 * <p>
 * 提示：
 * 1、1 <= k <= n <= 30,000。
 * 2、所给数据范围 [-10,000，10,000]。
 * <p>
 * 链接：https://leetcode-cn.com/problems/maximum-average-subarray-i/
 */
public class Q643 {

    public static void main(String[] args) {
        // 12.75
        System.out.println(new Q643().findMaxAverage(stringToIntegerArray("[1,12,-5,-6,50,3]"), 4));
    }

    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        double ret = sum;
        for (int i = k; i < nums.length; i++) {
            sum = sum - nums[i - k] + nums[i];
            ret = Math.max(ret, sum);
        }
        return ret / k;
    }
}
