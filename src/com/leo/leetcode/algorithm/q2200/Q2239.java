package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度为 n 的整数数组 nums ，请你返回 nums 中最 接近 0 的数字。如果有多个答案，请你返回它们中的 最大值 。
 * 提示：
 * 1、1 <= n <= 1000
 * 2、-10^5 <= nums[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/find-closest-number-to-zero/
 */
public class Q2239 {
    public static void main(String[] args) {
        // 1
        System.out.println(new Q2239().findClosestNumber(stringToIntegerArray("[-4,-2,1,4,8]")));
        // 1
        System.out.println(new Q2239().findClosestNumber(stringToIntegerArray("[2,-1,1]")));
    }

    public int findClosestNumber(int[] nums) {
        int ret = nums[0], min = Integer.MAX_VALUE;
        for (int num : nums) {
            int abs = Math.abs(num);
            if (abs == min) ret = Math.max(ret, num);
            else if (abs < min) {
                min = abs;
                ret = num;
            }
        }
        return ret;
    }

}
