package com.leo.leetcode.algorithm.q0000;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 * 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
 * 链接：https://leetcode-cn.com/problems/two-sum
 */
public class Q1 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q1().twoSum(new int[]{2, 7, 11, 15}, 9)));
    }

    public int[] twoSum(int[] nums, int target) {
        int[] ret = new int[2];
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i];
            int right = target - v;
            if (m.containsKey(right)) return new int[]{i, m.get(right)};
            else m.put(v, i);
        }

        return ret;
    }

}
