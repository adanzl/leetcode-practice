package com.leo.leetcode.algorithm.q0300;


import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
 * 题目数据保证答案符合 32 位整数范围。
 * 提示：
 * 1、1 <= nums.length <= 200
 * 2、1 <= nums[i] <= 1000
 * 3、nums 中的所有元素 互不相同
 * 4、1 <= target <= 1000
 * 进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？
 * 链接：https://leetcode-cn.com/problems/combination-sum-iv
 */
public class Q377 {

    public static void main(String[] args) {
        // 7
        System.out.println(new Q377().combinationSum4(stringToIntegerArray("[1,2,3]"), 4));
        // 0
        System.out.println(new Q377().combinationSum4(stringToIntegerArray("[9]"), 3));
    }

    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int i = 1; i < dp.length; i++) {
            for (int num : nums) {
                if (i >= num) dp[i] += dp[i - num];
            }
        }
        return dp[target];
    }
}
