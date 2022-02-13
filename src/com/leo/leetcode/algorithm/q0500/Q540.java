package com.leo.leetcode.algorithm.q0500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
 * 请你找出并返回只出现一次的那个数。
 * 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
 * 提示:
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
 */
public class Q540 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q540().singleNonDuplicate(stringToIntegerArray("[1,1,2,3,3]")));
        // 2
        System.out.println(new Q540().singleNonDuplicate(stringToIntegerArray("[1,1,2,3,3,4,4,8,8]")));
        // 1
        System.out.println(new Q540().singleNonDuplicate(stringToIntegerArray("[1]")));
        // 0
        System.out.println(new Q540().singleNonDuplicate(stringToIntegerArray("[0,1,1,3,3,4,4,8,8]")));
        // 9
        System.out.println(new Q540().singleNonDuplicate(stringToIntegerArray("[1,1,3,3,4,4,8,8,9]")));
        // 10
        System.out.println(new Q540().singleNonDuplicate(stringToIntegerArray("[3,3,7,7,10,11,11]")));
    }

    public int singleNonDuplicate(int[] nums) {
        int l = 0, r = nums.length;
        while (l < r - 1) {
            int m = (l + r) / 2;
            if ((m & 1) == 1) { // 奇数
                if (nums[m] == nums[m - 1]) l = m + 1;
                else r = m;
            } else { // 偶数
                if (nums[m] == nums[m - 1]) r = m - 1;
                else l = m;
            }
        }
        return nums[l];
    }
}
