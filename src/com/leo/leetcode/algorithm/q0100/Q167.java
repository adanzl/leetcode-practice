package com.leo.leetcode.algorithm.q0100;

import java.util.Arrays;

/**
 * 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
 * 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
 * 说明:
 * 返回的下标值（index1 和 index2）不是从零开始的。
 * 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
 * 链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
 */
public class Q167 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q167().twoSum(new int[]{2, 7, 11, 15}, 9))); // [1,2]
    }

    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length;
        while (l < r) {
            int sum = numbers[l] + numbers[r - 1];
            if (sum == target) break;
            else if (sum < target) l++;
            else r--;
        }
        return new int[]{l + 1, r};
    }
}
