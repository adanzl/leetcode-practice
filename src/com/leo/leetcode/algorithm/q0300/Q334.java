package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
 * 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-2^31 <= nums[i] <= 2^31 - 1
 * <p>
 * 进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？
 * <p>
 * 链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
 */
public class Q334 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q334().increasingTriplet(stringToIntegerArray("[1,1,-2,6]")));
        // true
        System.out.println(new Q334().increasingTriplet(stringToIntegerArray("[1,2,3,4,5]")));
        // false
        System.out.println(new Q334().increasingTriplet(stringToIntegerArray("[5,4,3,2,1]")));
        // true
        System.out.println(new Q334().increasingTriplet(stringToIntegerArray("[2,1,5,0,4,6]")));
    }

    public boolean increasingTriplet(int[] nums) {
        int v1 = Integer.MAX_VALUE, v2 = v1, f1 = 0;
        for (int n : nums) {
            if (f1 == 0 || n <= v1) {
                v1 = n;
                f1 = 1;
            } else if (n <= v2) {
                v2 = n;
            } else {
                return true;
            }
        }
        return false;
    }
}
