package com.leo.leetcode.algorithm.q0500;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
 * 返回该 最大总和 。
 * <p>
 * 提示：
 * 1、1 <= n <= 10^4
 * 2、nums.length == 2 * n
 * 3、-10^4 <= nums[i] <= 10^4
 * <p>
 * 链接：https://leetcode-cn.com/problems/array-partition-i
 */
public class Q561 {

    public static void main(String[] args) {
        // 64
        System.out.println(new Q561().arrayPairSum(stringToIntegerArray("[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]")));
        // 4
        System.out.println(new Q561().arrayPairSum(stringToIntegerArray("[1,4,3,2]")));
        // 9
        System.out.println(new Q561().arrayPairSum(stringToIntegerArray("[6,2,6,5,1,2]")));
    }

    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int ret = nums[0];
        for(int i = 1; i<nums.length >> 1; i++) {
            ret += nums[i << 1];
        }
        return ret;
    }
}
