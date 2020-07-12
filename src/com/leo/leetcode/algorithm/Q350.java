package com.leo.leetcode.algorithm;

import java.util.*;

/**
 * 给定两个数组，编写一个函数来计算它们的交集。
 * 说明：
 * 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
 * 我们可以不考虑输出结果的顺序。
 * 进阶:
 * 如果给定的数组已经排好序呢？你将如何优化你的算法？
 * 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
 * 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
 * 链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
 */
public class Q350 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q350().intersect(new int[]{1, 2, 2, 1}, new int[]{2, 2}))); // [2,2]
        System.out.println(Arrays.toString(new Q350().intersect(new int[]{4, 9, 5}, new int[]{9, 4, 9, 8, 4}))); // [4,9]
    }

    public int[] intersect(int[] nums1, int[] nums2) {
        int[] n1 = nums1.length > nums2.length ? nums1 : nums2;
        int[] n2 = nums1.length > nums2.length ? nums2 : nums1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : n1) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        int[] out = new int[n1.length];
        int index = 0;
        for (int n : n2) {
            if (map.containsKey(n)) {
                int c = map.get(n);
                out[index++] = n;
                if (c == 1) map.remove(n);
                else map.put(n, c - 1);
            }
        }
        return Arrays.copyOfRange(out, 0, index);
    }
}
