package com.leo.leetcode.algorithm.q0500;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组和一个整数 k，你需要在数组里找到 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。
 * 这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：
 * 1、0 <= i < j < nums.length
 * 2、|nums[i] - nums[j]| == k
 * 注意，|val| 表示 val 的绝对值。
 * 提示：
 * 1、1 <= nums.length <= 10^4
 * 2、-10^7 <= nums[i] <= 10^7
 * 3、0 <= k <= 10^7
 * 链接：https://leetcode.cn/problems/k-diff-pairs-in-an-array
 */
public class Q532 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q532().findPairs(stringToIntegerArray("[3, 1, 4, 1, 5]"), 2));
        // 4
        System.out.println(new Q532().findPairs(stringToIntegerArray("[1, 2, 3, 4, 5]"), 1));
        // 1
        System.out.println(new Q532().findPairs(stringToIntegerArray("[1, 3, 1, 5, 4]"), 0));
    }

    public int findPairs(int[] nums, int k) {
        Arrays.sort(nums);
        int ret = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int v = nums[i] + k;
            int idx = Arrays.binarySearch(nums, i + 1, nums.length, v);
            if (idx >= 0) ret++;
        }
        return ret;
    }
}
