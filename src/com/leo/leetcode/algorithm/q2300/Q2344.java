package com.leo.leetcode.algorithm.q2300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个正整数数组 nums 和 numsDivide 。你可以从 nums 中删除任意数目的元素。
 * 请你返回使 nums 中 最小 元素可以整除 numsDivide 中所有元素的 最少 删除次数。如果无法得到这样的元素，返回 -1 。
 * 如果 y % x == 0 ，那么我们说整数 x 整除 y 。
 * 提示：
 * 1、1 <= nums.length, numsDivide.length <= 10^5
 * 2、1 <= nums[i], numsDivide[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-deletions-to-make-array-divisible
 */
public class Q2344 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q2344().minOperations(stringToIntegerArray("[44,7,10,8,19,15,44,35,25,29,40,41,26,1,48,29,26,7,10,50,40,4,34,20,46,9,23,26,28,47,15,46,2,49,44,1,7,24,2,13,39,3,40,20,42,3,43,7,26,1,6,15,43,33,28,14,35,11]")
                , stringToIntegerArray("[17,28,13,17,33,10,27,17,16]")));
        // 1
        System.out.println(new Q2344().minOperations(stringToIntegerArray("[40,38,18,19,18,18,16]"), stringToIntegerArray("[430222122,345833946,609158196,173124594,25468560,990277596,295095510,354571344,931500936,636837210]")));
        // -1
        System.out.println(new Q2344().minOperations(stringToIntegerArray("[4,3,6]"), stringToIntegerArray("[8,2,6,10]")));
        // 2
        System.out.println(new Q2344().minOperations(stringToIntegerArray("[2,3,3,18,3,2,3,16]"), stringToIntegerArray("[573595257,616368999,782586708,555836748,128826519,10729950,660848235,459842193,986538021,509885907]")));
        // 2
        System.out.println(new Q2344().minOperations(stringToIntegerArray("[2,3,2,4,3]"), stringToIntegerArray("[9,6,9,3,15]")));
        // -1
        System.out.println(new Q2344().minOperations(stringToIntegerArray("[4,3,6]"), stringToIntegerArray("[8,2,6,10]")));
    }

    public int minOperations(int[] nums, int[] numsDivide) {
        int num = numsDivide[0];
        for (int i = 1; i < numsDivide.length; i++) {
            num = gcd(num, numsDivide[i]);
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (num % nums[i] == 0) return i;
        }
        return -1;
    }

    // 最大公约数
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

}
