package com.leo.leetcode.algorithm.q0200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
 * 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
 * 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、0 <= nums[i] <= 1000
 * 链接：https://leetcode-cn.com/problems/house-robber-ii
 */
public class Q213 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q213().rob(stringToIntegerArray("[2,1,1,2]")));
        // 14
        System.out.println(new Q213().rob(stringToIntegerArray("[4,1,2,7,5,3,1]")));
        // 3
        System.out.println(new Q213().rob(stringToIntegerArray("[3,2]")));
        // 3
        System.out.println(new Q213().rob(stringToIntegerArray("[2,3,2]")));
        // 4
        System.out.println(new Q213().rob(stringToIntegerArray("[1,2,3,1]")));
        // 1
        System.out.println(new Q213().rob(stringToIntegerArray("[1]")));
    }

    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        return Math.max(func(nums, nums[0], nums.length - 1), func(nums, 0, nums.length));
    }

    int func(int[] nums, int n_2, int len) {
        int n_1 = Math.max(n_2, nums[1]), ret = n_1;
        for (int i = 2; i < len; i++) {
            int v = Math.max(n_2 + nums[i], n_1);
            ret = Math.max(ret, v);
            n_2 = n_1;
            n_1 = v;
        }
        return ret;
    }
}
