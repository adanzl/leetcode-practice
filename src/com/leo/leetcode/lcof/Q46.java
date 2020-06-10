package com.leo.leetcode.lcof;

public class Q46 {

    public static void main(String[] args) {
        System.out.println(new Q46().translateNum(12258)); // 5
    }

    public int translateNum(int num) {
        char[] nums = Integer.toString(num).toCharArray();
        if (nums.length == 1) return 1;
        int v1 = (nums[0] - '0') * 10 + nums[1] - '0' < 26 ? 2 : 1;
        if (nums.length == 2) return v1;
        int[] dp = new int[nums.length];
        dp[0] = 1;
        dp[1] = v1;
        for (int i = 2; i < nums.length; i++) {
            dp[i] = dp[i - 1] + (nums[i - 1] != '0' && (nums[i - 1] - '0') * 10 + nums[i] - '0' < 26 ? dp[i - 2] : 0);
        }
        return dp[dp.length - 1];
    }
}
