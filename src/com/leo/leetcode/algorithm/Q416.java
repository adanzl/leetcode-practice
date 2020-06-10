package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q416 {
    public void TestOJ() {
        System.out.println(canPartition(LCUtil.stringToIntegerArray("[1, 2, 5]"))); // f
        System.out.println(canPartition(LCUtil.stringToIntegerArray("[3, 3, 3, 4, 5]"))); // t
        System.out.println(canPartition(LCUtil.stringToIntegerArray("[1, 5, 11, 5]"))); // t
        System.out.println(canPartition(LCUtil.stringToIntegerArray("[1, 2, 3, 5]"))); // f
    }

    // flag[n] = flag[n-k] (k=s[0-n])

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int v : nums) {
            sum += v;
        }
        if (sum % 2 == 1) return false;
        int target = sum / 2;
        boolean[] flag = new boolean[target + 1];
        flag[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                if (flag[i - num]) {
                    flag[i] = true;
                    if (i == target) return true;
                }

            }
        }
        return flag[target];
    }
}
