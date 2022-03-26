package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.TestCase;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
 * 你需要返回给定数组中的重要翻转对的数量。
 * 注意:
 * 1、给定数组的长度不会超过50000。
 * 2、输入数组中的所有数字都在32位整数的表示范围内。
 * 链接：https://leetcode-cn.com/problems/reverse-pairs
 */
public class Q493 {

    public static void main(String[] args) {
        // 624975000
        TestCase tc = new TestCase("resources/Q493/Case001.txt");
        System.out.println(new Q493().reversePairs(stringToIntegerArray(tc.getData(0))));
        // 2
        System.out.println(new Q493().reversePairs(stringToIntegerArray("[1,3,2,3,1]")));
        // 3
        System.out.println(new Q493().reversePairs(stringToIntegerArray("[2,4,3,5,1]")));
    }

    public int reversePairs(int[] nums) {
        int ret = 0;
        Node head = new Node(Integer.MIN_VALUE, Integer.MAX_VALUE);
        for (long n : nums) {
            ret += query(head, (n << 1) + 1, Integer.MAX_VALUE);
            addNode(head, n);
        }
        return ret;
    }

    void addNode(Node root, long v) {
        root.c++;
        if (root.l == root.r) return;
        long mid = (root.r + root.l) >> 1;
        if (v <= mid) {
            if (root.left == null) root.left = new Node(root.l, mid);
            addNode(root.left, v);
        } else {
            if (root.right == null) root.right = new Node(mid + 1, root.r);
            addNode(root.right, v);
        }
    }

    int query(Node root, long l, long r) {
        if (root == null || l > root.r || r < root.l) return 0;
        if (root.l == l && r == root.r) return root.c;
        long mid = (root.r + root.l) >> 1;
        if (r <= mid) return query(root.left, l, r);
        if (l >= mid + 1) return query(root.right, l, r);
        return query(root.left, l, mid) + query(root.right, mid + 1, r);
    }

    static class Node {
        long l, r;
        int c = 0;
        Node left, right;

        Node(long l, long r) {
            this.l = l;
            this.r = r;
        }
    }
}
