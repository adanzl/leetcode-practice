package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，
 * 这样可以使数组变为 [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。
 * 此后，任何值小于或等于其索引的项都可以记作一分。
 * 例如，数组为 nums = [2,4,1,3,0]，我们按 k = 2 进行轮调后，它将变成 [1,3,0,2,4]。这将记为 3 分，
 * 因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。
 * 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] < nums.length
 * 链接：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score
 */
public class Q798 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q798().bestRotation(stringToIntegerArray("[2,3,1,4,0]")));
        // 0
        System.out.println(new Q798().bestRotation(stringToIntegerArray("[0,3,1,3,1]")));
        // 0
        System.out.println(new Q798().bestRotation(stringToIntegerArray("[1,3,0,2,4]")));
    }

    public int bestRotation(int[] nums) {
        int len = nums.length, ret = 0, size = 0, max;
        int[] dp = new int[len];
        for (int i = 0; i < len; i++) {
            dp[(i - nums[i] + len) % len]++;
            if (nums[i] <= i) size++;
        }
        max = size;
        for (int i = 1; i <= len; i++) {
            size = size - dp[i - 1] + 1;
            if (size > max) {
                ret = i;
                max = size;
            }
        }
        return ret;
    }
}
