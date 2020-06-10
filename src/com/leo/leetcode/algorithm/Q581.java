package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q581 {

    public static void main(String[] args) {
        new Q581().TestOJ();
    }

    public void TestOJ() {
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[1,2,3,4,5]"))); // 0
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[2,1,1,1,1]"))); // 5
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[1,2,4,5,3]"))); // 3
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[2,3,3,2,4]"))); // 3
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[2,1]"))); // 2
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[2,1,2]"))); // 2
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[2, 6, 4, 8, 10, 9, 15]"))); // 5
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[2]"))); // 0
        System.out.println(findUnsortedSubarray(LCUtil.stringToIntegerArray("[1,2]"))); // 0
    }

    public int findUnsortedSubarray(int[] nums) {
        int l = Integer.MIN_VALUE, r = Integer.MIN_VALUE, max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < max) {
                if (l == Integer.MIN_VALUE) {
                    l = i - 1;
                }
                while (l >= 0) {
                    if (nums[l] <= nums[i]) break;
                    l--;
                }
                r = i;
            }
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        return r - l;
    }
}
