package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
 * 提示:
 * 1、1 <= nums.length <= 1000
 * 2、0 <= nums[i] <= 1000
 * 链接：https://leetcode-cn.com/problems/valid-triangle-number/
 */
public class Q611 {

    public static void main(String[] args) {
        // 21
        System.out.println(new Q611().triangleNumber(stringToIntegerArray("[2,2,4,4]")));
        // 3
        System.out.println(new Q611().triangleNumber(stringToIntegerArray("[2,2,3,4]")));
        // 4
        System.out.println(new Q611().triangleNumber(stringToIntegerArray("[4,2,3,4]")));
    }

    public int triangleNumber(int[] nums) {
        int ret = 0, n = nums.length;
        if (n < 3) return ret;
        Arrays.sort(nums);
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                int left = j + 1, right = n - 1, k = j;
                while (left <= right) {
                    int mid = (left + right) >> 1;
                    if (nums[mid] < nums[i] + nums[j]) {
                        k = mid;
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }
                }
                ret += k - j;
            }
        }
        return ret;
    }
}
