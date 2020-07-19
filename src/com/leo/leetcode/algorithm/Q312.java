package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

/**
 * 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
 * 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
 * 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
 * 求所能获得硬币的最大数量。
 * 说明:
 * 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
 * 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
 * 链接：https://leetcode-cn.com/problems/burst-balloons
 */
public class Q312 {
    public static void main(String[] args) {
        new Q312().TestOJ();
    }

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
