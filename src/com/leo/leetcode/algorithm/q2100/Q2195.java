package com.leo.leetcode.algorithm.q2100;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。
 * 返回追加到 nums 中的 k 个整数之和。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i], k <= 10^9
 * 链接：https://leetcode.cn/problems/append-k-integers-with-minimal-sum
 */
public class Q2195 {

    public static void main(String[] args) {
        // 25
        System.out.println(new Q2195().minimalKSum(stringToIntegerArray("[5,6]"), 6));
        // 794
        System.out.println(new Q2195().minimalKSum(stringToIntegerArray("[96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]"), 35));
        // 4510056693322271
        System.out.println(new Q2195().minimalKSum(stringToIntegerArray("[835,434,236,562]"), 94974274));
    }

    public long minimalKSum(int[] nums, int k) {
        Arrays.sort(nums);
        long ret = 0;
        int idx = 0, num = 0, n = nums.length;
        while (k > 0 && idx < n) {
            long r = Math.min(nums[idx] - 1, num + k), len = r - num;
            if (len > 0) {
                ret += len * (len + num + num + 1) / 2;
                k -= len;
            }
            num = nums[idx];
            while (idx < n && nums[idx] == num) idx++;
        }
        num = nums[n - 1] + 1;
        if (k > 0) ret += (long) (num + k - 1 + num) * k / 2;
        return ret;
    }
}
