package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;
import java.util.Random;

/**
 * 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
 * 实现 Solution class:
 * Solution(int[] nums) 使用整数数组 nums 初始化对象
 * int[] reset() 重设数组到它的初始状态并返回
 * int[] shuffle() 返回数组随机打乱后的结果
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 200
 * 2、-10^6 <= nums[i] <= 10^6
 * 3、nums 中的所有元素都是 唯一的
 * 4、最多可以调用 5 * 104 次 reset 和 shuffle
 * <p>
 * 链接：https://leetcode-cn.com/problems/shuffle-an-array
 */
public class Q384 {

    public static void main(String[] args) {
        int[] nums;
        nums = new int[]{1, 2, 3};
        Solution obj = new Solution(nums);
        System.out.println(Arrays.toString(obj.shuffle())); // [3, 1, 2]
        System.out.println(Arrays.toString(obj.reset())); // [1, 2, 3]
        System.out.println(Arrays.toString(obj.shuffle())); // [1, 3, 2]]
    }

    static class Solution {

        int[] nums;
        int[] original;
        Random random = new Random();

        public Solution(int[] nums) {
            this.nums = nums;
            this.original = nums.clone();
        }

        public int[] reset() {
            return original;
        }

        public int[] shuffle() {
            for (int i = 0; i < nums.length; i++) {
                int index = random.nextInt(nums.length - i) + i;
                int v = nums[i];
                nums[i] = nums[index];
                nums[index] = v;
            }
            return nums;
        }
    }
}
