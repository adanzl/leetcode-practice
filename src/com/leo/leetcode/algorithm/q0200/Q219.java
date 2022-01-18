package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

import java.util.HashSet;
import java.util.Set;

/**
 * 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
 * 如果存在，返回 true ；否则，返回 false 。
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-109 <= nums[i] <= 10^9
 * 3、0 <= k <= 10^5
 * <p>
 * 链接：https://leetcode-cn.com/problems/contains-duplicate-ii
 */
public class Q219 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q219().containsNearbyDuplicate(LCUtil.stringToIntegerArray("[1,0,1,1]"), 1));
        // false
        System.out.println(new Q219().containsNearbyDuplicate(LCUtil.stringToIntegerArray("[1,2,3,1,2,3]"), 2));
        // true
        System.out.println(new Q219().containsNearbyDuplicate(LCUtil.stringToIntegerArray("[1,2,3,1]"), 3));
        // false
        System.out.println(new Q219().containsNearbyDuplicate(LCUtil.stringToIntegerArray("[1]"), 1));
        // false
        System.out.println(new Q219().containsNearbyDuplicate(LCUtil.stringToIntegerArray("[1,2,1]"), 1));
    }

    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> cMap = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i];
            if (cMap.contains(v)) return true;
            cMap.add(v);
            if (i >= k) cMap.remove(nums[i - k]);
        }
        return false;
    }
}
