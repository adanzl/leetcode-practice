package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下表从 0 开始的整数数组 nums 。每次操作中，你可以将数组中任何一个元素替换为 任意两个 和为该元素的数字。
 * 比方说，nums = [5,6,7] 。一次操作中，我们可以将 nums[1] 替换成 2 和 4 ，将 nums 转变成 [5,2,4,7] 。
 * 请你执行上述操作，将数组变成元素按 非递减 顺序排列的数组，并返回所需的最少操作次数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-replacements-to-sort-the-array
 */
public class Q2366 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q2366().minimumReplacement(stringToIntegerArray("[12,9,7,6,17,19,21]")));
        // 2
        System.out.println(new Q2366().minimumReplacement(stringToIntegerArray("[3,9,3]")));
        // 0
        System.out.println(new Q2366().minimumReplacement(stringToIntegerArray("[1,2,3,4,5]")));
    }

    public long minimumReplacement(int[] nums) {
        long ret = 0;
        int n = nums.length, last = Integer.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] <= last) {
                last = nums[i];
            } else {
                int a = nums[i] / last;
                if (nums[i] % last == 0) {
                    ret += a - 1;
                } else {
                    ret += a;
                    last = nums[i] / (a + 1);
                }
            }
        }
        return ret;
    }
}
