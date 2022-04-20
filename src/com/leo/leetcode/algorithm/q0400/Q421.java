package com.leo.leetcode.algorithm.q0400;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
 * 进阶：你可以在 O(n) 的时间解决这个问题吗？
 * 提示：
 * 1、1 <= nums.length <= 2 * 10^4
 * 2、0 <= nums[i] <= 2^31 - 1
 * 链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array
 */
public class Q421 {

    public static void main(String[] args) {
        // 28
        System.out.println(new Q421().findMaximumXOR(stringToIntegerArray("[3,10,5,25,2,8]")));
        // 0
        System.out.println(new Q421().findMaximumXOR(stringToIntegerArray("[0]")));
        // 6
        System.out.println(new Q421().findMaximumXOR(stringToIntegerArray("[2,4]")));
        // 10
        System.out.println(new Q421().findMaximumXOR(stringToIntegerArray("[8,10,2]")));
        // 127
        System.out.println(new Q421().findMaximumXOR(stringToIntegerArray("[14,70,53,83,49,91,36,80,92,51,66,70]")));
    }

    public int findMaximumXOR(int[] nums) {
        int ret = 0, N = 31;
        for (int i = 1; i <= N; i++) {
            int mask = ((1 << i) - 1) << (N - i);
            int target = ret | 1 << (N - i);
            Set<Integer> set = new HashSet<>();
            for (int num : nums) set.add(num & mask);
            for (int num : set) {
                if (set.contains(num ^ target)) {
                    ret = target;
                    break;
                }
            }
        }
        return ret;
    }
}
