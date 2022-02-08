package com.leo.leetcode.algorithm.q2000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组nums和一个整数k，请你返回数对(i, j)的数目，满足i < j且|nums[i] - nums[j]| == k。
 * |x|的值定义为：
 * 如果x >= 0，那么值为x。
 * 如果x < 0，那么值为-x。
 * 提示：
 * 1、1 <= nums.length <= 200
 * 2、1 <= nums[i] <= 100
 * 3、1 <= k <= 99
 * 链接：https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k
 */
public class Q2006 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q2006().countKDifference(stringToIntegerArray("[7,7,8,3,1,2,7,2,9,5]"), 6));
        // 3
        System.out.println(new Q2006().countKDifference(stringToIntegerArray("[3,2,1,5,4]"), 2));
        // 4
        System.out.println(new Q2006().countKDifference(stringToIntegerArray("[1,2,2,1]"), 1));
        // 0
        System.out.println(new Q2006().countKDifference(stringToIntegerArray("[1,3]"), 3));
    }

    public int countKDifference(int[] nums, int k) {
        int ret = 0;
        int[] count = new int[201];
        for (int num : nums) {
            ret += count[num + k] + (num >= k ? count[num - k] : 0);
            ++count[num];
        }
        return ret;
    }
}
