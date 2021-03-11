package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.Arrays;

/**
 * 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
 * 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 2500
 * 2、-10^4 <= nums[i] <= 10^4
 * <p>
 * 进阶：
 * 1、你可以设计时间复杂度为 O(n2) 的解决方案吗？
 * 2、你能将算法的时间复杂度降低到 O(n log(n)) 吗?
 * <p>
 * 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
 */
public class Q300 {
    public static void main(String[] args) {
        // 3
        System.out.println(new Q300().lengthOfLIS(stringToIntegerArray("[10,9,2,5,3,4]")));
        // 4
        System.out.println(new Q300().lengthOfLIS(stringToIntegerArray("[10,9,2,5,3,7,101,18]")));
        // 4
        System.out.println(new Q300().lengthOfLIS(stringToIntegerArray("[0]")));
    }

    private int lengthOfLIS(int[] nums) {
        if (nums.length == 0) return 0;
        int max = 1;
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                    max = Math.max(max, dp[i]);
                }
            }
        }
        return max;
    }
}
