package com.leo.leetcode.algorithm.q0100;

/**
 * 峰值元素是指其值大于左右相邻值的元素。
 * 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
 * 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
 * 你可以假设 nums[-1] = nums[n] = -∞。
 * 说明:
 *   你的解法应该是 O(logN) 时间复杂度的。
 * 链接：https://leetcode-cn.com/problems/find-peak-element
 */
public class Q163 {

    public static void main(String[] args) {
        System.out.println(new Q163().findPeakElement(new int[] { 2, 1 })); // 0
        System.out.println(new Q163().findPeakElement(new int[] { 1, 2, 3, 1 })); // 2
        System.out.println(new Q163().findPeakElement(new int[] { 1, 2, 1, 3, 5, 6, 4 })); // 1 || 5
        System.out.println(new Q163().findPeakElement(new int[] { 1 })); // 0
    }

    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length;
        while (l < r) {
            int mid = l + ((r - l) >> 1);
            if ((mid == 0 || nums[mid] > nums[mid - 1]) && (mid == nums.length - 1 || nums[mid] > nums[mid + 1])) {
                return mid;
            }
            if (mid == 0 || (mid != nums.length - 1 && nums[mid + 1] > nums[mid - 1])) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}