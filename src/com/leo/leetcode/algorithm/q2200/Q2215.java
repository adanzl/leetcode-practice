package com.leo.leetcode.algorithm.q2200;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，请你返回一个长度为 2 的列表 answer ，其中：
 * answer[0] 是 nums1 中所有 不 存在于 nums2 中的 不同 整数组成的列表。
 * answer[1] 是 nums2 中所有 不 存在于 nums1 中的 不同 整数组成的列表。
 * 注意：列表中的整数可以按 任意 顺序返回。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 1000
 * 2、-1000 <= nums1[i], nums2[i] <= 1000
 * 链接：https://leetcode-cn.com/problems/find-the-difference-of-two-arrays
 */
public class Q2215 {

    public static void main(String[] args) {
        // [[1,3],[4,6]]
        System.out.println(new Q2215().findDifference(stringToIntegerArray("[1,2,3]"), stringToIntegerArray("[2,4,6]")));
        // [[3],[]]
        System.out.println(new Q2215().findDifference(stringToIntegerArray("[1,2,3,3]"), stringToIntegerArray("[1,1,2,2]")));
    }

    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> ret = new ArrayList<>(2);
        Set<Integer> s1 = new HashSet<>(), s2 = new HashSet<>();
        for (int n : nums1) s1.add(n);
        for (int n : nums2) s2.add(n);
        for (int n : nums2) {
            if (s1.contains(n)) {
                s1.remove(n);
                s2.remove(n);
            }
        }
        ret.add(new ArrayList<>(s1));
        ret.add(new ArrayList<>(s2));
        return ret;
    }
}
