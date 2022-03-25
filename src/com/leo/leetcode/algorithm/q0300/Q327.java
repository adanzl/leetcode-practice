package com.leo.leetcode.algorithm.q0300;

import com.leo.utils.TestCase;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。
 * 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-2^31 <= nums[i] <= 2^31 - 1
 * 3、-10^5 <= lower <= upper <= 10^5
 * 4、题目数据保证答案是一个 32 位 的整数
 * 链接：https://leetcode-cn.com/problems/count-of-range-sum
 */
public class Q327 {
    // 线段树、前缀和
    public static void main(String[] args) {
        // 3
        System.out.println(new Q327().countRangeSum(stringToIntegerArray("[-2,5,-1]"), -2, 2));
        // 3
        System.out.println(new Q327().countRangeSum(stringToIntegerArray("[-2,0,2147483647, 2147483647]"), -2, 100000));
        // 1
        System.out.println(new Q327().countRangeSum(stringToIntegerArray("[0]"), 0, 0));
        TestCase tc = new TestCase("resources/Q327/Case002.txt");
        // 385647
        System.out.println(new Q327().countRangeSum(stringToIntegerArray(tc.getData(0)), tc.getDataInt(1), tc.getDataInt(2)));
        tc = new TestCase("resources/Q327/Case001.txt");
        // 289392
        System.out.println(new Q327().countRangeSum(stringToIntegerArray(tc.getData(0)), tc.getDataInt(1), tc.getDataInt(2)));
        tc = new TestCase("resources/Q327/Case003.txt");
        // 202935140
        System.out.println(new Q327().countRangeSum(stringToIntegerArray(tc.getData(0)), tc.getDataInt(1), tc.getDataInt(2)));
    }


    public int countRangeSum(int[] nums, int lower, int upper) {
        int ret = 0, len = nums.length;
        long preSum = 0;
        Node head = new Node(Integer.MIN_VALUE * 5000L, Integer.MAX_VALUE * 5000L);
        addNode(head, 0);
        for (int i = 1; i <= len; i++) {
            preSum += nums[i - 1];
            long low = preSum - upper, high = preSum - lower;
            ret += query(head, low, high);
            addNode(head, preSum);
        }
        return ret;
    }

    void addNode(Node root, long v) {
        root.c++;
        if (root.l == root.r) return;
        long mid = (root.l + root.r) >> 1;
        if (v <= mid) {
            if (root.left == null) root.left = new Node(root.l, mid);
            addNode(root.left, v);
        } else {
            if (root.right == null) root.right = new Node(mid + 1, root.r);
            addNode(root.right, v);
        }
    }

    int query(Node root, long l, long r) {
        if (root == null) return 0;
        if (root.l == l && root.r == r) return root.c;
        long mid = (root.l + root.r) >> 1;
        if (r <= mid) return query(root.left, l, r);
        if (l >= mid + 1) return query(root.right, l, r);
        return query(root.left, l, mid) + query(root.right, mid + 1, r);
    }

    static class Node {
        Node left, right;
        long l, r;
        int c = 0;

        Node(long l, long r) {
            this.l = l;
            this.r = r;
        }
    }
}
