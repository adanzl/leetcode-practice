package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.LCUtil;

/**
 * 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
 * <p>
 * 注意:
 * 1、每个数组中的元素不会超过 100
 * 2、数组的大小不会超过 200
 * <p>
 * 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
 */
public class Q416 {

    public static void main(String[] args) {
        System.out.println(new Q416().canPartition(LCUtil.stringToIntegerArray("[1, 2, 5]"))); // f
        System.out.println(new Q416().canPartition(LCUtil.stringToIntegerArray("[3, 3, 3, 4, 5]"))); // t
        System.out.println(new Q416().canPartition(LCUtil.stringToIntegerArray("[1, 5, 11, 5]"))); // t
        System.out.println(new Q416().canPartition(LCUtil.stringToIntegerArray("[1, 2, 3, 5]"))); // f
    }

    // flag[n] = flag[n-k] (k=s[0-n])

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int v : nums) {
            sum += v;
        }
        if (sum % 2 == 1) return false;
        int target = sum / 2;
        boolean[] flag = new boolean[target + 1];
        flag[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                if (flag[i - num]) {
                    flag[i] = true;
                    if (i == target) return true;
                }

            }
        }
        return flag[target];
    }
}
