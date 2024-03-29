package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。
 * 如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
 * 1、子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
 * 2、子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
 * 3、子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
 * 如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array
 */
public class Q2369 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q2369().validPartition(stringToIntegerArray("[3,2,1]")));
        // true
        System.out.println(new Q2369().validPartition(stringToIntegerArray("[4,4,4,5,6]")));
        // false
        System.out.println(new Q2369().validPartition(stringToIntegerArray("[1,1,1,2]")));
    }

    public boolean validPartition(int[] nums) {
        int n = nums.length;
        boolean[] dp = new boolean[n];
        if (nums[0] == nums[1]) dp[1] = true;
        if (n >= 3 && nums[2] == nums[1] && nums[1] == nums[0]) dp[2] = true;
        if (n >= 3 && nums[2] - nums[1] == 1 && nums[1] - nums[0] == 1) dp[2] = true;
        for (int i = 2; i < n; i++) {
            dp[i] |= nums[i] == nums[i - 1] && dp[i - 2];
            if (i > 2) {
                dp[i] |= nums[i] == nums[i - 1] && nums[i - 1] == nums[i - 2] && dp[i - 3];
                dp[i] |= nums[i - 1] - nums[i - 2] == 1 && nums[i] - nums[i - 1] == 1 && dp[i - 3];
            }
        }
        return dp[n - 1];
    }
}
