package com.leo.leetcode.lcof;

import com.leo.utils.LCUtil;

public class Q53 {

    public static void main(String[] args) {
        new Q53().TestOJ();
    }

    public void TestOJ() {
        System.out.println(search(LCUtil.stringToIntegerArray("[1,2,3]"), 1)); // 1
        System.out.println(search(LCUtil.stringToIntegerArray("[2,2]"), 2)); // 2
        System.out.println(search(LCUtil.stringToIntegerArray("[1]"), 1)); // 1
        System.out.println(search(LCUtil.stringToIntegerArray("[5,7,7,8,8,10]"), 8)); // 2
    }

    public int search(int[] nums, int target) {
        int l = getMinIndex(nums, 0, nums.length, target);
        if (l < 0) return 0;
        int r = getMaxIndex(nums, l, nums.length, target);
        return r - l + 1;
    }

    int getMinIndex(int[] nums, int s, int e, int target) {
        if (e - s < 1) return -1;
        int m = (s + e - 1) / 2;
        if (target == nums[m]) {
            if (m == s) return m;
            return nums[m - 1] != target ? m : getMinIndex(nums, s, m, target);
        } else if (target < nums[m]) {
            return getMinIndex(nums, s, m, target);
        }
        return getMinIndex(nums, m + 1, e, target);
    }

    int getMaxIndex(int[] nums, int s, int e, int target) {
        if (e - s < 1) return -1;
        int m = (s + e - 1) / 2;
        if (target == nums[m]) {
            if (m == e - 1) return m;
            return nums[m + 1] != target ? m : getMaxIndex(nums, m + 1, e, target);
        } else if (target < nums[m]) {
            return getMaxIndex(nums, s, m, target);
        }
        return getMaxIndex(nums, m + 1, e, target);
    }
}
