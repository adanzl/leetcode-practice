package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，
 * 使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。
 * 请输出满足上述要求的最少需要补充的数字个数。
 * <p>
 * 链接：https://leetcode-cn.com/problems/patching-array
 */
public class Q330 {

    public static void main(String[] args) {
        // 28
        System.out.println(new Q330().minPatches(stringToIntegerArray("[1,2,31,33]"), 2147483647));
        // 2
        System.out.println(new Q330().minPatches(stringToIntegerArray("[1,5,10]"), 20));
        // 1
        System.out.println(new Q330().minPatches(stringToIntegerArray("[1,3]"), 6));
        // 0
        System.out.println(new Q330().minPatches(stringToIntegerArray("[1,2,2]"), 5));
    }

    public int minPatches(int[] nums, int n) {
        long total = 0;
        int i = 0, count = 0;
        while (total < n) {
            if (i < nums.length && total + 1 >= nums[i]) {
                total += nums[i];
                i++;
            } else {
                total += total + 1;
                ++count;
            }
        }
        return count;
    }
}
