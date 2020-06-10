package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

public class Q312 {
    @Test
    public void TestOJ() {
        System.out.println(maxCoins(LCUtil.stringToIntegerArray("[3,1,5,8]"))); // 167
    }

    /**
     * dp[i][j] i,j之间，不包括ij的最大值
     * dp[i][j] = max{dp[i][k]+dp[k][j]+num[i]*num[k]*num[j]}(i<k<j)
     * 特例：dp[i][i+1] = 0
     */
    public int maxCoins(int[] nums) {
        if (nums == null) return 0;
        int[] nums2 = new int[nums.length + 2];
        System.arraycopy(nums, 0, nums2, 1, nums.length);
        nums2[0] = 1;
        nums2[nums2.length - 1] = 1;
        int[][] dp = new int[nums2.length][nums2.length];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = new int[nums2.length];
        }

        // 开始dp：i为begin，j为end，k为在i、j区间划分子问题时的边界
        for (int i = dp.length - 2; i > -1; i--) {
            for (int j = i + 2; j < dp[i].length; j++) {
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i][k] + dp[k][j] + nums2[i] * nums2[k] * nums2[j]);
                }
            }
        }

        return dp[0][nums2.length - 1];
    }
}
