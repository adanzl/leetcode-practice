package com.leo.leetcode.algorithm.q0500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、nums[i] 不是 0 就是 1
 * <p>
 * 链接：https://leetcode-cn.com/problems/contiguous-array/
 */
public class Q525 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q525().findMaxLength(stringToIntegerArray("[0,1]")));
        // 8
        System.out.println(new Q525().findMaxLength(stringToIntegerArray("[0,1,1,1,1,0,0,0]")));
        // 2
        System.out.println(new Q525().findMaxLength(stringToIntegerArray("[0,0,1]")));
        // 0
        System.out.println(new Q525().findMaxLength(stringToIntegerArray("[0]")));
        // 0
        System.out.println(new Q525().findMaxLength(stringToIntegerArray("[1,1,1,1,1,1,1,1]")));
        // 0
        System.out.println(new Q525().findMaxLength(stringToIntegerArray("[1]")));
        // 2
        System.out.println(new Q525().findMaxLength(stringToIntegerArray("[0,1,0]")));
    }


    public int findMaxLength(int[] nums) {
        int ret = 0, sum = 0, n = nums.length;
        int[] marks = new int[(n << 1) + 2];
        marks[n] = 1;
        for (int i = 0; i < n; i++) {
            sum += nums[i] == 0 ? 1 : -1;
            int key = sum + n, v = marks[key];
            if (v == 0) {
                marks[key] = i + 2;
            } else {
                ret = Math.max(ret, i + 2 - v);
            }
        }
        return ret;
    }
}
