package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组nums，你可以对它进行一些操作。
 * 每次操作中，选择任意一个nums[i]，删除它并获得nums[i]的点数。之后，你必须删除 所有 等于nums[i] - 1 和 nums[i] + 1的元素。
 * 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
 * 提示：
 * 1、1 <= nums.length <= 2 * 10^4
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode-cn.com/problems/delete-and-earn
 */
public class Q740 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q740().deleteAndEarn(stringToIntegerArray("[1]")));
        // 6
        System.out.println(new Q740().deleteAndEarn(stringToIntegerArray("[3,4,2]")));
        // 9
        System.out.println(new Q740().deleteAndEarn(stringToIntegerArray("[2,2,3,3,3,4]")));
    }

    public int deleteAndEarn(int[] nums) {
        int len = 0;
        for (int n : nums) len = Math.max(len, n);
        int[] sums = new int[len + 1];
        for (int n : nums) sums[n] += n;
        int[] flag = new int[4];
        for (int i = sums.length - 1; i >= 0; i--) {
            flag[3] = Math.max(flag[0], flag[1]) + sums[i];
            flag[0] = flag[1];
            flag[1] = flag[2];
            flag[2] = flag[3];
        }
        return Math.max(flag[1], flag[2]);
    }
}
