package com.leo.leetcode.algorithm.q2000;


import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ，请你计算 nums[j] - nums[i] 能求得的 最大差值 ，其中 0 <= i < j < n 且 nums[i] < nums[j] 。
 * 返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。
 * 提示：
 * 1、n == nums.length
 * 2、2 <= n <= 1000
 * 3、1 <= nums[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements
 */
public class Q2016 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2016().maximumDifference(stringToIntegerArray("[7,1,5,4]")));
        // -1
        System.out.println(new Q2016().maximumDifference(stringToIntegerArray("[9,4,3,2]")));
        // 9
        System.out.println(new Q2016().maximumDifference(stringToIntegerArray("[1,5,2,10]")));
    }

    public int maximumDifference(int[] nums) {
        int ret = -1, len = nums.length, min = nums[0];
        int[] arrMax = new int[len];
        arrMax[len - 1] = nums[len - 1];
        for (int i = len - 2; i >= 0; i--) arrMax[i] = Math.max(arrMax[i + 1], nums[i]);
        for (int i = 0; i < len; i++) {
            min = Math.min(min, nums[i]);
            if (min < arrMax[i]) ret = Math.max(ret, arrMax[i] - min);
        }
        return ret;
    }
}
