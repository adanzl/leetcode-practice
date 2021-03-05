package com.leo.leetcode.algorithm.q0500;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
 * 数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
 * 如果不存在，则输出 -1。
 * 注意: 输入数组的长度不会超过 10000。
 * <p>
 * 链接：https://leetcode-cn.com/problems/next-greater-element-ii
 */
public class Q503 {

    public static void main(String[] args) {
        // [2,3,4,5,6,-1,6,5,6,2,3,4]
        System.out.println(Arrays.toString(new Q503().nextGreaterElements(stringToIntegerArray("[1,2,3,4,5,6,5,4,5,1,2,3]"))));
        // [5,6,6,8,-1]
        System.out.println(Arrays.toString(new Q503().nextGreaterElements(stringToIntegerArray("[1,5,3,6,8]"))));
        // [-1,5,5,5,5]
        System.out.println(Arrays.toString(new Q503().nextGreaterElements(stringToIntegerArray("[5,4,3,2,1]"))));
        // [2,-1,2]
        System.out.println(Arrays.toString(new Q503().nextGreaterElements(stringToIntegerArray("[1,2,1]"))));
        // [2,-1,2,2,-1]
        System.out.println(Arrays.toString(new Q503().nextGreaterElements(stringToIntegerArray("[1,2,1,1,2]"))));
        // []
        System.out.println(Arrays.toString(new Q503().nextGreaterElements(stringToIntegerArray("[]"))));
    }

    public int[] nextGreaterElements(int[] nums) {
        int len = nums.length, top = -1;
        int[] ret = new int[len], si = new int[len];
        for (int i = 0; i < len; i++) {
            si[++top] = i;
            int idx = i + 1;
            while (idx < len && top != -1 && nums[si[top]] < nums[idx]) ret[si[top--]] = nums[idx];
        }
        for (int num : nums) while (top != -1 && nums[si[top]] < num) ret[si[top--]] = num;
        while (top != -1) ret[si[top--]] = -1;
        return ret;
    }

}
