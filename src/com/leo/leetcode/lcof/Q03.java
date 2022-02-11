package com.leo.leetcode.lcof;

/**
 * 找出数组中重复的数字。
 * 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
 * 限制：
 * 1、2 <= n <= 100000
 * 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
 */
public class Q03 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q03().findRepeatNumber(new int[]{3, 4, 2, 0, 0, 1}));
        // 2 || 3
        System.out.println(new Q03().findRepeatNumber(new int[]{2, 3, 1, 0, 2, 5, 3}));
    }

    public int findRepeatNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int p = nums[i];
            while (p != i) {
                int t = nums[p];
                if (t == p)
                    return p;
                nums[p] = p;
                p = t;
            }
            nums[p] = i;
        }
        return -1;
    }
}
