package com.leo.leetcode.algorithm.q1700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
 * 请你返回 nums 中唯一元素的 和 。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode-cn.com/problems/sum-of-unique-elements/
 */
public class Q1748 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q1748().sumOfUnique(stringToIntegerArray("[1,2,3,2]")));
        // 0
        System.out.println(new Q1748().sumOfUnique(stringToIntegerArray("[1,1,1,1,1]")));
        // 15
        System.out.println(new Q1748().sumOfUnique(stringToIntegerArray("[1,2,3,4,5]")));
    }

    public int sumOfUnique(int[] nums) {
        int[] marks = new int[101];
        int ret = 0;
        for (int v : nums) {
            if (marks[v] == 0) {
                ret += v;
                marks[v] = 1;
            } else if (marks[v] == 1) {
                ret -= v;
                marks[v] = 2;
            }
        }
        return ret;
    }
}
