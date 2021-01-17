package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.LCUtil;

import java.util.Arrays;

/**
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
 * 返回这三个数的和。假定每组输入只存在唯一答案。
 * 链接：https://leetcode-cn.com/problems/3sum-closest
 */
public class Q16 {

    public static void main(String[] args) {
        new Q16().TestOJ();
    }

    public void TestOJ() {
        System.out.println(threeSumClosest(LCUtil.stringToIntegerArray("[0,2,1,-3]"), 1)); // t
        System.out.println(threeSumClosest(LCUtil.stringToIntegerArray("[1,1,1,1]"), 0)); // t
    }

    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int out = target, delta = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l = i + 1, r = nums.length - 1;
            int v1 = nums[i];
            while (l < r) {
                int sum = v1 + nums[l] + nums[r];
                int d = Math.abs(sum - target);
                if (d == 0) return target;
                else if (sum < target) l++;
                else if (sum > target) r--;
                if (delta > d) {
                    delta = d;
                    out = sum;
                }
            }
        }
        return out;
    }
}
