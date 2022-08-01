package com.leo.leetcode.algorithm.q2300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个非负整数数组 nums 。在一步操作中，你必须：
 * 1、选出一个正整数 x ，x 需要小于或等于 nums 中 最小 的 非零 元素。
 * 2、nums 中的每个正整数都减去 x。
 * 返回使 nums 中所有元素都等于 0 需要的 最少 操作数。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、0 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/make-array-zero-by-subtracting-equal-amounts
 */
public class Q2357 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2357().minimumOperations(stringToIntegerArray("[1,5,0,3,5]")));
        // 0
        System.out.println(new Q2357().minimumOperations(stringToIntegerArray("[0]")));
    }

    public int minimumOperations(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : nums) if (num != 0) pq.add(num);
        int ret = 0;
        while (!pq.isEmpty()) {
            int size = pq.size();
            int v = pq.peek();
            PriorityQueue<Integer> nq = new PriorityQueue<>();
            while (size-- > 0 && !pq.isEmpty()) {
                int nv = pq.poll() - v;
                if (nv != 0) nq.add(nv);
            }
            pq = nq;
            ret++;
        }
        return ret;
    }
}
