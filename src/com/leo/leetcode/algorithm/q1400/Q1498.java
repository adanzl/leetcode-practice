package com.leo.leetcode.algorithm.q1400;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个整数 target 。
 * 请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
 * 由于答案可能很大，请将结果对 10^9 + 7 取余后返回。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 3、1 <= target <= 10^6
 * 链接：https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition
 */
public class Q1498 {

    public static void main(String[] args) {
        // 688052206
        System.out.println(new Q1498().numSubSeq(stringToIntegerArray("[27,21,14,2,15,1,19,8,12,24,21,8,12,10,11,30,15,18,28,14,26,9,2,24,23,11,7,12,9,17,30,9,28,2,14,22,19,19,27,6,15,12,29,2,30,11,20,30,21,20,2,22,6,14,13,19,21,10,18,30,2,20,28,22]")
                , 31));
        // 4
        System.out.println(new Q1498().numSubSeq(stringToIntegerArray("[3,5,6,7]"), 9));
        // 6
        System.out.println(new Q1498().numSubSeq(stringToIntegerArray("[3,3,6,8]"), 10));
        // 61
        System.out.println(new Q1498().numSubSeq(stringToIntegerArray("[2,3,3,4,6,7]"), 12));
    }

    public int numSubSeq(int[] nums, int target) {
        int mod = 1_000_000_007, n = nums.length;
        long ret = 0;
        int[] pow2 = new int[n];
        pow2[0] = 1;
        for (int i = 1; i < pow2.length; i++) pow2[i] = (pow2[i - 1] << 1) % mod;
        Arrays.sort(nums);
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            if (nums[l] + nums[r] > target) r--;
            else {
                ret = (ret + pow2[r - l]) % mod;
                l++;
            }
        }
        return (int) ret;
    }
}
