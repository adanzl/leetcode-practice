package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.LCUtil;

/**
 * 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
 * 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
 * <p>
 * 提示：
 * 1、数组非空，且长度不会超过 20 。
 * 2、初始的数组的和不会超过 1000 。
 * 3、保证返回的最终结果能被 32 位整数存下。
 * <p>
 * 链接：https://leetcode-cn.com/problems/target-sum
 */
public class Q494 {
    public static void main(String[] args) {
        System.out.println(new Q494().findTargetSumWays(LCUtil.stringToIntegerArray("[1, 1, 1, 1, 1]"), 3)); // 5
        System.out.println(new Q494().findTargetSumWays(LCUtil.stringToIntegerArray("[0,0,0,0]"), 3)); // 0
    }

    private int count;

    public int findTargetSumWays(int[] nums, int S) {
        this.count = 0;
        process(nums, S, 0, 0);
        return this.count;
    }

    private void process(int[] nums, int S, int index, int s) {
        if (index == nums.length - 1) {
            if (s + nums[index] == S) this.count++;
            if (s - nums[index] == S) this.count++;
            return;
        }
        process(nums, S, index + 1, s + nums[index]);
        process(nums, S, index + 1, s - nums[index]);
    }
}
