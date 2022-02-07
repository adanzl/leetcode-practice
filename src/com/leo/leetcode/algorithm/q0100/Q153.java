package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;

/**
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 * ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
 * 请找出其中最小的元素。
 * 你可以假设数组中不存在重复元素。
 * 链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
 */
public class Q153 {
    public void TestOJ() {
        System.out.println(findMin(LCUtil.stringToIntegerArray("[5,1,2,3,4]"))); // 1
        System.out.println(findMin(LCUtil.stringToIntegerArray("[1,2]"))); // 1
        System.out.println(findMin(LCUtil.stringToIntegerArray("[3,4,5,1,2]"))); // 1
        System.out.println(findMin(LCUtil.stringToIntegerArray("[4,5,6,7,0,1,2,3,4]"))); // 0
    }

    public int findMin(int[] nums) {
        int pos = nums.length / 2;
        int t = nums[pos];
        for (int i = pos; i < nums.length; i++) { // right
            if (nums[i] < t) {
                return nums[i];
            }

        }
        t = nums[pos];
        for (int i = pos; i >= 0; i--) { // left
            if (nums[i] > t) {
                return t;
            }
            t = nums[i];
        }
        return nums[0];
    }
}
