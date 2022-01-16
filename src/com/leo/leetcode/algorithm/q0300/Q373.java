package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 给定两个以升序排列的整数数组 nums1 和 nums2  ,  以及一个整数 k  。
 * 定义一对值  (u,v)，其中第一个元素来自  nums1，第二个元素来自 nums2  。
 * 请找到和最小的 k  个数对  (u1,v1),   (u2,v2)   ...   (uk,vk)  。
 * 提示:
 * 1、1 <= nums1.length, nums2.length <= 10^4
 * 2、-10^9 <= nums1[i], nums2[i] <= 10^9
 * 3、nums1, nums2 均为升序排列
 * 4、1 <= k <= 1000
 * 链接：https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums
 */
public class Q373 {

    public static void main(String[] args) {
        // [[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]]
        System.out.println(new Q373().kSmallestPairs(stringToIntegerArray("[1,7,11]"), stringToIntegerArray("[2,4,6]"), 10));
        // [1,2],[1,4],[1,6]
        System.out.println(new Q373().kSmallestPairs(stringToIntegerArray("[1,7,11]"), stringToIntegerArray("[2,4,6]"), 3));
        // [1,1],[1,1]
        System.out.println(new Q373().kSmallestPairs(stringToIntegerArray("[1,1,2]"), stringToIntegerArray("[1,2,3]"), 2));
        // [1,3],[2,3]
        System.out.println(new Q373().kSmallestPairs(stringToIntegerArray("[1,2]"), stringToIntegerArray("[3]"), 2));
        // [1,3]
        System.out.println(new Q373().kSmallestPairs(stringToIntegerArray("[1]"), stringToIntegerArray("[3]"), 3));
    }

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        int len0 = nums1.length, len1 = nums2.length;
        List<List<Integer>> ret = new ArrayList<>(k);
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(o -> (nums1[o[0]] + nums2[o[1]])));
        for (int i = 0; i < Math.min(k, len0); i++) q.offer(new int[]{i, 0});
        while (k-- > 0 && !q.isEmpty()) {
            int[] ans = q.poll();
            ret.add(Arrays.asList(nums1[ans[0]], nums2[ans[1]]));
            if (ans[1] + 1 < len1) q.offer(new int[]{ans[0], ans[1] + 1});
        }
        return ret;
    }
}
