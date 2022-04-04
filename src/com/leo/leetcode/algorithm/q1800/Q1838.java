package com.leo.leetcode.algorithm.q1800;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 元素的 频数 是该元素在一个数组中出现的次数。
 * 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
 * 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、1 <= k <= 10^5
 * 链接：https://leetcode-cn.com/problems/frequency-of-the-most-frequent-elementO
 */
public class Q1838 {
    // 滑动窗口
    public static void main(String[] args) {
        // 73
        System.out.println(new Q1838().maxFrequency(stringToIntegerArray("[9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]"), 3056));
        // 3
        System.out.println(new Q1838().maxFrequency(stringToIntegerArray("[1,2,4]"), 5));
        // 2
        System.out.println(new Q1838().maxFrequency(stringToIntegerArray("[1,4,8,13]"), 5));
        // 1
        System.out.println(new Q1838().maxFrequency(stringToIntegerArray("[3,9,6]"), 2));
    }

    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int ret = 1, n = nums.length;
        long cost = 0;
        for (int l = 0, r = 1; r < n; r++) {
            cost += (long) (r - l) * (nums[r] - nums[r - 1]);
            while (cost > k && l < r) {
                cost -= nums[r] - nums[l];
                l++;
            }
            ret = Math.max(ret, r - l + 1);
        }
        return ret;
    }
}
