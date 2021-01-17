package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;

public class Q169 {
    public void TestOJ() {
        System.out.println(majorityElement(LCUtil.stringToIntegerArray("[3,2,3]"))); // 3
        System.out.println(majorityElement(LCUtil.stringToIntegerArray("[2,2,1,1,1,2,2]"))); // 2
    }

    public int majorityElement(int[] nums) {

        int ret = 0;
        int c = 0;
        for (int num : nums) {
            if (c == 0) {
                ret = num;
                c++;
            } else if (ret == num) {
                c++;
            } else {
                c--;
            }

        }
        return ret;
    }
}
