package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.LCUtil;

/**
 * 给定一个未排序的整数数组，找到最长递增子序列的个数。
 * 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
 * 提示:
 * 1、1 <= nums.length <= 2000
 * 2、-10^6 <= nums[i] <= 10^6
 * 链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/
 */
public class Q673 {

    public static void main(String[] args) {
        new Q673().TestOJ();
    }

    public void TestOJ() {
        // 1
        System.out.println(findNumberOfLIS(LCUtil.stringToIntegerArray("[3,1,2]")));
        // 2
        System.out.println(findNumberOfLIS(LCUtil.stringToIntegerArray("[1,3,5,4,7]")));
        // 5
        System.out.println(findNumberOfLIS(LCUtil.stringToIntegerArray("[2,2,2,2,2]")));
    }

    public int findNumberOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 1;
        int out = 1, max = 1;
        for (int i = 1; i < nums.length; i++) {
            int p = i, len = 1;
            while (p >= 0 && nums[p] >= nums[i]) p--;
            if (p != -1) len = dp[p] + 1;
            dp[i] = Math.max(dp[i - 1], len);
            if (len > max) max = len;
            else if (len == max) out++;
        }
        return out;
    }
}
