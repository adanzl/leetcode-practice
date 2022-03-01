package com.leo.leetcode.algorithm.q0600;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个未排序的整数数组，找到最长递增子序列的个数。
 * 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
 * 提示:
 * 1、1 <= n <= 2000
 * 2、-10^6 <= nums[i] <= 10^6
 * 链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/
 */
public class Q673 {

    public static void main(String[] args) {
        new Q673().TestOJ();
    }

    public void TestOJ() {
        // 1
        System.out.println(findNumberOfLIS(stringToIntegerArray("[3,1,2]")));
        // 2
        System.out.println(findNumberOfLIS(stringToIntegerArray("[1,3,5,4,7]")));
        // 5
        System.out.println(findNumberOfLIS(stringToIntegerArray("[2,2,2,2,2]")));
    }

    public int findNumberOfLIS(int[] nums) {
        int n = nums.length, maxLen = 0, ans = 0;
        int[] dp = new int[n];
        int[] cnt = new int[n];
        for (int i = 0; i < n; ++i) {
            dp[i] = 1;
            cnt[i] = 1;
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j]) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        cnt[i] = cnt[j]; // 重置计数
                    } else if (dp[j] + 1 == dp[i]) {
                        cnt[i] += cnt[j];
                    }
                }
            }
            if (dp[i] > maxLen) {
                maxLen = dp[i];
                ans = cnt[i]; // 重置计数
            } else if (dp[i] == maxLen) {
                ans += cnt[i];
            }
        }
        return ans;
    }
}
