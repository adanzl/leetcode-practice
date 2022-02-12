package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
 * 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
 * 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。
 * 如果不存在下一个更大元素，那么本次查询的答案是 -1 。
 * 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
 * 提示：
 * 1、1 <= nums1.length <= nums2.length <= 1000
 * 2、0 <= nums1[i], nums2[i] <= 10^4
 * 3、nums1和nums2中所有整数 互不相同
 * 4、nums1 中的所有整数同样出现在 nums2 中
 * 进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？
 * <p>
 * 链接：https://leetcode-cn.com/problems/next-greater-element-i
 */
public class Q496 {

    public static void main(String[] args) {
        // [-1,3,-1]
        System.out.println(Arrays.toString(new Q496().nextGreaterElement(stringToIntegerArray("[4,1,2]"), stringToIntegerArray("[1,3,4,2]"))));
        // [3,-1]
        System.out.println(Arrays.toString(new Q496().nextGreaterElement(stringToIntegerArray("[2,4]"), stringToIntegerArray("[1,2,3,4]"))));
    }

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] ret = new int[nums1.length];
        Stack<Integer> s = new Stack<>();
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = nums2.length - 1; i >= 0; i--) {
            while (!s.isEmpty() && s.peek() < nums2[i]) s.pop();
            m.put(nums2[i], s.isEmpty() ? -1 : s.peek());
            s.push(nums2[i]);
        }
        for (int i = 0; i < nums1.length; i++) ret[i] = m.get(nums1[i]);
        return ret;
    }
}
