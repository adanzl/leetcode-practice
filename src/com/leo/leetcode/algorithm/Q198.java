package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q198 {
    public void TestOJ() {
        System.out.println(rob(LCUtil.stringToIntegerArray("[1,2,3,1]"))); // 4
        System.out.println(rob(LCUtil.stringToIntegerArray("[2,7,9,3,1]"))); // 12
    }

    /**
     * dp[i] = s[i] + max(s[i-2], s[i-3])
     */
    public int rob(int[] nums) {
        if (nums.length == 0)
            return 0;
        if (nums.length == 1)
            return nums[0];
        if (nums.length == 2)
            return Math.max(nums[0], nums[1]);
        if (nums.length == 3)
            return Math.max(nums[0] + nums[2], nums[1]);
        nums[2] += nums[0];
        int ret = Math.max(nums[1], nums[2]);
        for (int i = 3; i < nums.length; i++) {
            nums[i] = Math.max(nums[i - 2], nums[i - 3]) + nums[i];
            ret = Math.max(ret, nums[i]);
        }
        return ret;
    }
}
