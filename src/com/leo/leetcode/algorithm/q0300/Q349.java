package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 1000
 * 2、0 <= nums1[i], nums2[i] <= 1000
 * 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays/
 */
public class Q349 {

    public static void main(String[] args) {
        // [2]
        System.out.println(Arrays.toString(new Q349().intersection(stringToIntegerArray("[1,2,2,1]"), stringToIntegerArray("[2,2]"))));
        // [4,9]
        System.out.println(Arrays.toString(new Q349().intersection(stringToIntegerArray("[4,9,5]"), stringToIntegerArray("[9,4,9,8,4]"))));
    }

    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>(), inter = new HashSet<>();
        for (int num : nums1) set.add(num);
        for (int num : nums2) if (set.contains(num)) inter.add(num);
        int[] ret = new int[inter.size()];
        int i = 0;
        for (int num : inter) ret[i++] = num;
        return ret;
    }
}
