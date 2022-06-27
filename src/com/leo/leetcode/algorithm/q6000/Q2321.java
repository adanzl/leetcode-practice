package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度都是 n 。
 * 你可以选择两个整数 left 和 right ，其中 0 <= left <= right < n ，接着 交换 两个子数组 nums1[left...right] 和 nums2[left...right] 。
 * 例如，设 nums1 = [1,2,3,4,5] 和 nums2 = [11,12,13,14,15] ，整数选择 left = 1 和 right = 2，那么 nums1 会变为 [1,12,13,4,5] 而 nums2 会变为 [11,2,3,14,15] 。
 * 你可以选择执行上述操作 一次 或不执行任何操作。
 * 数组的 分数 取 sum(nums1) 和 sum(nums2) 中的最大值，其中 sum(arr) 是数组 arr 中所有元素之和。
 * 返回 可能的最大分数 。
 * 子数组 是数组中连续的一个元素序列。arr[left...right] 表示子数组包含 nums 中下标 left 和 right 之间的元素（含 下标 left 和 right 对应元素）。
 * 提示：
 * 1、n == nums1.length == nums2.length
 * 2、1 <= n <= 10^5
 * 3、1 <= nums1[i], nums2[i] <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-score-of-spliced-array
 */
public class Q2321 {

    public static void main(String[] args) {
        // 210
        System.out.println(new Q2321().maximumsSplicedArray(stringToIntegerArray("[60,60,60]"), stringToIntegerArray("[10,90,10]")));
        // 220
        System.out.println(new Q2321().maximumsSplicedArray(stringToIntegerArray("[20,40,20,70,30]"), stringToIntegerArray("[50,20,50,40,20]")));
        // 31
        System.out.println(new Q2321().maximumsSplicedArray(stringToIntegerArray("[7,11,13]"), stringToIntegerArray("[1,1,1]")));
    }


    public int maximumsSplicedArray(int[] nums1, int[] nums2) {
        int n = nums1.length, sum1 = 0, sum2 = 0, maxDela = Integer.MIN_VALUE, minDela = Integer.MAX_VALUE;
        int[] nums = new int[n], dpMax = new int[n], dpMin = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = nums2[i] - nums1[i];
            sum1 += nums1[i];
            sum2 += nums2[i];
            if (i > 0) {
                dpMax[i] = Math.max(dpMax[i - 1] + nums[i], nums[i]);
                dpMin[i] = Math.min(dpMin[i - 1] + nums[i], nums[i]);
            } else {
                dpMax[i] = nums[i];
                dpMin[i] = nums[i];
            }
            maxDela = Math.max(dpMax[i], maxDela);
            minDela = Math.min(dpMin[i], minDela);
        }
        return Math.max(sum1 + maxDela, sum2 - minDela);
    }

}
