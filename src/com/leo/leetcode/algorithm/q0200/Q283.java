package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

import java.util.Arrays;

/**
 * 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
 * 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
 * 提示:
 * 1、1 <= nums.length <= 10^4
 * 2、-2^31 <= nums[i] <= 2^31 - 1
 * 进阶：你能尽量减少完成的操作次数吗？
 * 链接：https://leetcode-cn.com/problems/move-zeroes/
 */
public class Q283 {

    public static void main(String[] args) {
        new Q283().TestOJ();
    }

    public void TestOJ() {
        int[] nums = LCUtil.stringToIntegerArray("[0,1,0,3,12]");
        moveZeroes(nums);
        System.out.println(Arrays.toString(nums)); // [1,3,12,0,0]
    }

    public void moveZeroes(int[] nums) {
        int p = 0;
        for (int i = 0; i < nums.length; i++) {
            nums[p] = nums[i];
            if (nums[i] != 0) {
                p++;
            }
        }
        for (int i = p; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
