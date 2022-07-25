package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 给你一个下标从 0 开始的正整数数组 nums 和一个正整数 k 。
 * 如果满足下述条件，则数对 (num1, num2) 是 优质数对 ：
 * 1、num1 和 num2 都 在数组 nums 中存在。
 * 2、num1 OR num2 和 num1 AND num2 的二进制表示中值为 1 的位数之和大于等于 k ，其中 OR 是按位 或 操作，而 AND 是按位 与 操作。
 * 返回 不同 优质数对的数目。
 * 如果 a != c 或者 b != d ，则认为 (a, b) 和 (c, d) 是不同的两个数对。例如，(1, 2) 和 (2, 1) 不同。
 * 注意：如果 num1 在数组中至少出现 一次 ，则满足 num1 == num2 的数对 (num1, num2) 也可以是优质数对。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= 60
 * 链接：https://leetcode.cn/problems/number-of-excellent-pairs
 */
public class Q2354 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q2354().countExcellentPairs(stringToIntegerArray("[1,2,3,1]"), 3));
        // 0
        System.out.println(new Q2354().countExcellentPairs(stringToIntegerArray("[5,1,1]"), 10));
    }

    public long countExcellentPairs(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        long ret = 0;
        long[] bCount = new long[32];
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            bCount[Integer.bitCount(nums[i])]++;
        }
        for (int i = 0; i < 32; i++) {
            for (int j = Math.max(k - i, 0); j < 32; j++) {
                ret += bCount[j] * bCount[i];
            }
        }
        return ret;
    }
}
