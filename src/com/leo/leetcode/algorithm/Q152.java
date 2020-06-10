package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q152 {
    public static void main(String[] args) {
        new Q152().TestOJ();
    }

    public void TestOJ() {
        System.out.println(maxProduct(LCUtil.stringToIntegerArray("[2,3,-2,4]"))); // 6
        System.out.println(maxProduct(LCUtil.stringToIntegerArray("[-2,0,-1]"))); // 0
        System.out.println(maxProduct(LCUtil.stringToIntegerArray("[-2]"))); // -2
        System.out.println(maxProduct(LCUtil.stringToIntegerArray("[2]"))); // 2
    }

    // dp[i][j] = dp[i][j-1] * s[j]
    public int maxProduct(int[] nums) {
        int ret = nums[0];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                nums[j] *= nums[i];
                ret = Math.max(ret, nums[j]);
            }
            ret = Math.max(ret, nums[i]);
        }
        return ret;
    }

    public int maxProduct1(int[] nums) {
        int max = Integer.MIN_VALUE, imax = 1, imin = 1;
        for (int num : nums) {
            if (num < 0) {
                int tmp = imax;
                imax = imin;
                imin = tmp;
            }
            imax = Math.max(imax * num, num);
            imin = Math.min(imin * num, num);

            max = Math.max(max, imax);
        }
        return max;
    }

}
