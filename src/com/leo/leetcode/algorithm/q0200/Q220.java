package com.leo.leetcode.algorithm.q0200;

import java.util.TreeSet;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。
 * 如果存在则返回 true，不存在返回 false。
 * 链接：https://leetcode-cn.com/problems/contains-duplicate-iii
 */
public class Q220 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q220().containsNearbyAlmostDuplicate(stringToIntegerArray("[-2147483648,2147483647]"), 1, 1));
        // true
        System.out.println(new Q220().containsNearbyAlmostDuplicate(stringToIntegerArray("[2147483647,2147483647]"), 3, 3));
        // true
        System.out.println(new Q220().containsNearbyAlmostDuplicate(stringToIntegerArray("[1,2,3,1]"), 3, 0));
        // true
        System.out.println(new Q220().containsNearbyAlmostDuplicate(stringToIntegerArray("[1,0,1,1]"), 1, 2));
        // false
        System.out.println(new Q220().containsNearbyAlmostDuplicate(stringToIntegerArray("[1,5,9,1,5,9]"), 2, 3));
    }

    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Integer> s = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            Integer n = s.ceiling(num);
            if (null != n && (long)n -  nums[i] <= t) return true;
            n = s.floor(num);
            if (null != n && (long) nums[i] - n <= t) return true;
            s.add(num);
            if (s.size() > k) s.remove(nums[i - k]);
        }
        return false;
    }
}
