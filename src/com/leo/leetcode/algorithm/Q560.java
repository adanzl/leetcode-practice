package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q560 {
    public void TestOJ() {
        System.out.println(subArraySum(LCUtil.stringToIntegerArray("[-1,-1,1]"), 0)); // 1
        System.out.println(subArraySum(LCUtil.stringToIntegerArray("[1,2,3]"), 3)); // 2
        System.out.println(subArraySum(LCUtil.stringToIntegerArray("[1,1,1]"), 0)); // 0
        System.out.println(subArraySum(LCUtil.stringToIntegerArray("[1,1,1]"), 2)); // 2
        System.out.println(subArraySum(LCUtil.stringToIntegerArray("[1]"), 2)); // 0
    }

    // sum(i,j) = sum(0,j) - sum(0,i) + nums[i]
    // sum[i] = sum[i-1] + nums[i];
    public int subArraySum(int[] nums, int k) {
        int out = 0;
        int[] sum = new int[nums.length + 1];
        for (int i = 1; i < sum.length; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        for (int i = 0; i < sum.length; i++) {
            for (int j = 0; j < i; j++) {
                if (sum[i] - sum[j] == k)
                    out++;
            }
        }
        return out;
    }
}
