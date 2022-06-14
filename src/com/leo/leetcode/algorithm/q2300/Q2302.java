package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 一个数字的 分数 定义为数组之和 乘以 数组的长度。
 * 比方说，[1, 2, 3, 4, 5] 的分数为 (1 + 2 + 3 + 4 + 5) * 5 = 75 。
 * 给你一个正整数数组 nums 和一个整数 k ，请你返回 nums 中分数 严格小于 k 的 非空整数子数组数目。
 * 子数组 是数组中的一个连续元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、1 <= k <= 10^15
 * 链接：https://leetcode.cn/problems/count-subarrays-with-score-less-than-k
 */
public class Q2302 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2302().countSubArrays(stringToIntegerArray("[9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7]"), 4));
        // 13
        System.out.println(new Q2302().countSubArrays(stringToIntegerArray("[5,2,6,8,9,7]"), 50));
        // 6
        System.out.println(new Q2302().countSubArrays(stringToIntegerArray("[2,1,4,3,5]"), 10));
        // 5
        System.out.println(new Q2302().countSubArrays(stringToIntegerArray("[1,1,1]"), 5));
    }


    public long countSubArrays(int[] nums, long k) {
        long ret = 0;
        int n = nums.length;
        long[] preSum = new long[n + 1];
        for (int i = 1; i <= n; i++) preSum[i] = preSum[i - 1] + nums[i - 1];
        for (int i = 0; i < n; i++) {
            int l = i, r = n - 1, idx = i - 1;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                long sum = (preSum[mid + 1] - preSum[i]) * (mid - i + 1);
                if (sum < k) {
                    l = mid + 1;
                    idx = mid;
                } else r = mid - 1;
            }
            ret += idx - i + 1;
        }
        return ret;
    }
}
