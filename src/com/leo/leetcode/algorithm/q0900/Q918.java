package com.leo.leetcode.algorithm.q0900;

import com.leo.utils.TestCase;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。
 * 在此处，环形数组意味着数组的末端将会与开头相连呈环状。
 * （形式上，当 0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]）
 * 此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。
 * （形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）
 * 提示：
 * 1、-30000 <= A[i] <= 30000
 * 2、1 <= A.length <= 30000
 * 链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray
 */
public class Q918 {

    public static void main(String[] args) {
        // -2
        System.out.println(new Q918().maxSubarraySumCircular(stringToIntegerArray("[-2]")));
        // -1
        System.out.println(new Q918().maxSubarraySumCircular(stringToIntegerArray("[-2,-3,-1]")));
        // 3
        System.out.println(new Q918().maxSubarraySumCircular(stringToIntegerArray("[1,-2,3,-2]")));
        // 3516893
        TestCase tc = new TestCase("resources/Q918/Case001.txt");
        System.out.println(new Q918().maxSubarraySumCircular(stringToIntegerArray(tc.getData(0))));
        // 10
        System.out.println(new Q918().maxSubarraySumCircular(stringToIntegerArray("[5,-3,5]")));
        // 4
        System.out.println(new Q918().maxSubarraySumCircular(stringToIntegerArray("[3,-1,2,-1]")));
        // 3
        System.out.println(new Q918().maxSubarraySumCircular(stringToIntegerArray("[3,-2,2,-3]")));

    }

    public int maxSubarraySumCircular(int[] nums) {
        int subMax = nums[0], subMin = nums[0], localMax = nums[0], localMin = nums[0], sum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sum += nums[i];
            localMax = Math.max(nums[i], localMax + nums[i]);
            subMax = Math.max(subMax, localMax);
            localMin = Math.min(nums[i], localMin + nums[i]);
            subMin = Math.min(subMin, localMin);
        }
        if (subMax < 0) return subMax;
        return Math.max(subMax, sum - subMin);
    }
}
