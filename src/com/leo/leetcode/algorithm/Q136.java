package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

public class Q136 {
    @Test
    public void TestOJ() {
        System.out.println(singleNumber(LCUtil.stringToIntegerArray("[2,2,1]"))); // 1
        System.out.println(singleNumber(LCUtil.stringToIntegerArray("[4,1,2,1,2]"))); // 4
    }

    public int singleNumber(int[] nums) {
        int ret = nums[0];
        for (int i = 1; i < nums.length; i++) {
            ret ^= nums[i];
        }
        return ret;
    }
}
