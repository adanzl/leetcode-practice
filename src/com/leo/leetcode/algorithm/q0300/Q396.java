package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个长度为 n 的整数数组 nums 。
 * 假设 arr_k 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
 * F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1]
 * 返回 F(0), F(1), ..., F(n-1)中的最大值 。
 * 生成的测试用例让答案符合 32 位
 * 提示:
 * 1、n == nums.length
 * 2、1 <= n <= 10^5
 * 3、-100 <= nums[i] <= 100
 * 链接：https://leetcode-cn.com/problems/rotate-function
 */
public class Q396 {

    public static void main(String[] args) {
        // 26
        System.out.println(new Q396().maxRotateFunction(stringToIntegerArray("[4,3,2,6]")));
        // 0
        System.out.println(new Q396().maxRotateFunction(stringToIntegerArray("[100]")));
    }

    public int maxRotateFunction(int[] nums) {
        int ret = Integer.MIN_VALUE, n = nums.length, sum = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            ans += nums[i] * i;
        }
        for (int i = n - 1; i >= 0; i--) {
            ans = ans - nums[i] * n + sum;
            ret = Math.max(ret, ans);
        }
        return ret;
    }
}
