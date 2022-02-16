package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

import java.util.Arrays;

/**
 * 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
 * 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
 * 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、-30 <= nums[i] <= 30
 * 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
 * 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
 * 链接：https://leetcode-cn.com/problems/product-of-array-except-self
 */
public class Q238 {
    public static void main(String[] args) {
        new Q238().TestOJ();
    }

    public void TestOJ() {
        // [120, 60, 40, 30, 24]
        System.out.println(Arrays.toString(productExceptSelf(LCUtil.stringToIntegerArray("[1,2,3,4,5]"))));
        // [2,1]
        System.out.println(Arrays.toString(productExceptSelf(LCUtil.stringToIntegerArray("[1,2]"))));
    }

    private int[] productExceptSelf(int[] nums) {
        int[] ret = new int[nums.length];
        int flag = nums[0];
        ret[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            ret[i] = flag;
            flag *= nums[i];
        }
        flag = nums[nums.length - 1];
        for (int i = nums.length - 2; i >= 0; i--) {
            ret[i] *= flag;
            flag *= nums[i];
        }
        return ret;
    }
}
