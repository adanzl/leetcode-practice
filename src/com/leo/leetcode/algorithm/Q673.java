package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

/**
 * 给定一个未排序的整数数组，找到最长递增子序列的个数。
 * 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
 */
public class Q673 {
    @Test
    public void TestOJ() {
        System.out.println(findNumberOfLIS(LCUtil.stringToIntegerArray("[1,3,5,4,7]"))); // 2
        System.out.println(findNumberOfLIS(LCUtil.stringToIntegerArray("[2,2,2,2,2]"))); // 5
    }

    public int findNumberOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 1;
        int out = 0, max = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > nums[i]) {
                dp[i] = 1;
            } else {
                dp[i] = dp[i - 1] + 1;
                if (dp[i] == max) {
                    out++;
                } else if (dp[i] > max) {
                    out = 1;
                    max = dp[i];
                }
            }
        }
        return out;
    }
}
