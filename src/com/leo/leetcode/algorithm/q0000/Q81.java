package com.leo.leetcode.algorithm.q0000;

/**
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 * ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
 * 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
 * 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
 */
public class Q81 {
    public static void main(String[] args) {
        System.out.println(new Q81().search(new int[]{1, 3, 1, 1}, 3)); // true
        System.out.println(new Q81().search(new int[]{2, 5, 6, 0, 0, 1, 2}, 0)); // true
        System.out.println(new Q81().search(new int[]{2, 5, 6, 0, 0, 1, 2}, 3)); // false
    }

    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return false;
        int start = 0, end = nums.length - 1, mid;
        while (start <= end) {
            mid = start + ((end - start) >> 1);
            if (nums[mid] == target) return true;
            if (nums[start] == nums[mid]) {
                start++;
                continue;
            }
            //前半部分有序
            if (nums[start] < nums[mid]) {
                //target在前半部分 否则，去后半部分找
                if (nums[mid] >= target && nums[start] <= target) end = mid;
                else start = mid + 1;
            } else {
                //后半部分有序 target在后半部分 否则，去后半部分找
                if (nums[mid] <= target && nums[end] >= target) start = mid;
                else end = mid - 1;
            }
        }
        return false;
    }
}
