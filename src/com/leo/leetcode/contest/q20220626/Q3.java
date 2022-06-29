package com.leo.leetcode.contest.q20220626;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 链接：https://leetcode.cn/contest/sf-tech/problems/8oimK4/
 */
public class Q3 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q3().findMaxCI(stringToIntegerArray("[54,42,62,75,82,86,86]")));
    }

    public int findMaxCI(int[] nums) {
        if (nums.length == 0) return 0;
        int ret = 1, cnt = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                cnt++;
            } else {
                cnt = 1;
            }
            ret = Math.max(ret, cnt);
        }
        return ret;
    }
}
