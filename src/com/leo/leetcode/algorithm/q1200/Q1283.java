package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
 * 请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
 * 每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
 * 题目保证一定有解。
 * 提示：
 * 1、1 <= nums.length <= 5 * 10^4
 * 2、1 <= nums[i] <= 10^6
 * 3、nums.length <= threshold <= 10^6
 * 链接：https://leetcode-cn.com/problems/find-the-smallest-divisor-given-a-threshold
 */
public class Q1283 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q1283().smallestDivisor(stringToIntegerArray("[1,2,5,9]"), 6));
        // 3
        System.out.println(new Q1283().smallestDivisor(stringToIntegerArray("[2,3,5,7,11]"), 11));
        // 4
        System.out.println(new Q1283().smallestDivisor(stringToIntegerArray("[19]"), 5));
    }

    public int smallestDivisor(int[] nums, int threshold) {
        int l = 1, r = 1000_000;
        while (l <= r) {
            int mid = (r + l) >> 1, sum = 0;
            for (int num : nums) {
                sum += num / mid;
                if (num % mid != 0) sum++;
                if (sum > threshold) break;
            }
            if (sum > threshold) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}
