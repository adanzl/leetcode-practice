package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

public class Q287 {

    public void TestOJ() {
        System.out.println(findDuplicate(LCUtil.stringToIntegerArray("[1,3,4,2,2]"))); // 2
        System.out.println(findDuplicate(LCUtil.stringToIntegerArray("[3,1,3,4,2]"))); // 3
    }

    private int findDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = nums.length - 1; j >= 0; j--) {
                if (nums[i] == nums[j]) {
                    if (i != j) {
                        return nums[i];
                    }
                    break;
                }
            }
        }
        return 0;
    }

}
