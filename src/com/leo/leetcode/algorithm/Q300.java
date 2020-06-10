package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q300 {
    public void TestOJ() {
        System.out.println(lengthOfLIS(LCUtil.stringToIntegerArray("[10,9,2,5,3,4]"))); // 3
        System.out.println(lengthOfLIS(LCUtil.stringToIntegerArray("[10,9,2,5,3,7,101,18]"))); // 4
        System.out.println(lengthOfLIS(LCUtil.stringToIntegerArray("[0]"))); // 4
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
