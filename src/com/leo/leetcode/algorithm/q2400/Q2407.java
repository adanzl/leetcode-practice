package com.leo.leetcode.algorithm.q2400;


import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个整数 k 。
 * 找到 nums 中满足以下要求的最长子序列：
 * 1、子序列 严格递增
 * 2、子序列中相邻元素的差值 不超过 k 。
 * 请你返回满足上述要求的 最长子序列 的长度。
 * 子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i], k <= 10^5
 * 链接：https://leetcode.cn/problems/longest-increasing-subsequence-ii
 */
public class Q2407 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q2407().lengthOfLIS(stringToIntegerArray("[4,2,1,4,3,4,5,8,15]"), 3));
        // 4
        System.out.println(new Q2407().lengthOfLIS(stringToIntegerArray("[7,4,5,1,8,12,4,7]"), 5));
        // 1
        System.out.println(new Q2407().lengthOfLIS(stringToIntegerArray("[1,5]"), 1));
    }

    public int lengthOfLIS(int[] nums, int k) {
        for (int num : nums) {
            int max = query(head, num - k, num - 1);
            addNode(head, num, num, max + 1);
        }
        return head.max;
    }

    Node head = new Node(0, 200_001);

    void addNode(Node root, int l, int r, int v) {
        int mid = (root.l + root.r) >> 1;
        if (root.left == null) root.left = new Node(root.l, mid);
        if (root.right == null) root.right = new Node(mid + 1, root.r);
        if (root.l == l && r == root.r) {
            root.dirty = 1;
            root.v = v;
            root.max = v;
            return;
        }
        pushDown(root);
        if (r <= mid) {
            addNode(root.left, l, r, v);
        } else if (l >= mid + 1) {
            addNode(root.right, l, r, v);
        } else {
            addNode(root.left, l, mid, v);
            addNode(root.right, mid + 1, r, v);
        }
        root.max = Math.max(root.left.max, root.right.max);
    }

    int query(Node root, int l, int r) {
        if (root == null) return 0;
        if (root.l == l && root.r == r) return root.max;
        pushDown(root);
        int mid = (root.l + root.r) >> 1;
        if (r <= mid) return query(root.left, l, r);
        if (l >= mid + 1) return query(root.right, l, r);
        return Math.max(query(root.left, l, mid), query(root.right, mid + 1, r));
    }

    void pushDown(Node root) {
        if (root.dirty == 0) return;
        addNode(root.left, root.left.l, root.left.r, root.left.v);
        addNode(root.right, root.right.l, root.right.r, root.right.v);
        root.dirty = 0;
    }

    static class Node {
        Node left, right;
        int l, r, v, dirty, max;

        Node(int l, int r) {
            this.l = l;
            this.r = r;
        }
    }
}
