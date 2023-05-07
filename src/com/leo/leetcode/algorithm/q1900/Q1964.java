package com.leo.leetcode.algorithm.q1900;

import java.util.Arrays;

/**
 * 你打算构建一些障碍赛跑路线。给你一个 下标从 0 开始 的整数数组 obstacles ，数组长度为 n ，其中 obstacles[i] 表示第 i 个障碍的高度。
 * 对于每个介于 0 和 n - 1 之间（包含 0 和 n - 1）的下标  i ，在满足下述条件的前提下，请你找出 obstacles 能构成的最长障碍路线的长度：
 * 1、你可以选择下标介于 0 到 i 之间（包含 0 和 i）的任意个障碍。
 * 2、在这条路线中，必须包含第 i 个障碍。
 * 3、你必须按障碍在 obstacles 中的 出现顺序 布置这些障碍。
 * 4、除第一个障碍外，路线中每个障碍的高度都必须和前一个障碍 相同 或者 更高 。
 * 返回长度为 n 的答案数组 ans ，其中 ans[i] 是上面所述的下标 i 对应的最长障碍赛跑路线的长度。
 * 提示：
 * 1、n == obstacles.length
 * 2、1 <= n <= 10^5
 * 3、1 <= obstacles[i] <= 10^7
 * 链接：https://leetcode.cn/problems/find-the-longest-valid-obstacle-course-at-each-position/
 */
public class Q1964 {


    public static void main(String[] args) {
        // [1,1,2,3,2,2]
        System.out.println(Arrays.toString(new Q1964().longestObstacleCourseAtEachPosition(new int[]{3, 1, 5, 6, 4, 2})));
        // [1,2,3,3]
        System.out.println(Arrays.toString(new Q1964().longestObstacleCourseAtEachPosition(new int[]{1, 2, 3, 2})));
        // [1,2,1]
        System.out.println(Arrays.toString(new Q1964().longestObstacleCourseAtEachPosition(new int[]{2, 2, 1})));
    }

    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        SegTree segTree = new SegTree(0, 10_000_000 + 1);
        int n = obstacles.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int o = obstacles[i];
            int v = (int) segTree.query(0, o) + 1;
            ans[i] = v;
            segTree.addNode(o, o, v);
        }
        return ans;
    }

    static class SegTree {
        static class Node {
            long l, r, v, mx, dirty;
            Node left, right;

            public Node(long l, long r) {
                this.l = l;
                this.r = r;
            }
        }

        Node head;

        SegTree(long l, long r) {
            this.head = new Node(l, r);
        }

        void addNode(long l, long r, long v) {
            this._addNode(head, l, r, v);
        }

        long query(long l, long r) {
            return this._query(head, l, r);
        }

        private void _addNode(Node root, long l, long r, long v) {
            long mid = root.l + (root.r - root.l) / 2;
            if (root.left == null) root.left = new Node(root.l, mid);
            if (root.right == null) root.right = new Node(mid + 1, root.r);
            if (l == root.l && r == root.r) {
                root.v = v;
                root.dirty = v;
                root.mx = v;
                return;
            }
            this.pushDown(root);
            if (r <= mid) this._addNode(root.left, l, r, v);
            else if (l >= mid + 1) this._addNode(root.right, l, r, v);
            else {
                this._addNode(root.left, l, mid, v);
                this._addNode(root.right, mid + 1, r, v);
            }
            root.mx = Math.max(root.left.mx, root.right.mx);
        }

        private long _query(Node root, long l, long r) {
            if (null == root) return 0;
            if (l == root.l && r == root.r) return root.mx;
            this.pushDown(root);
            long mid = root.l + (root.r - root.l) / 2;
            if (r <= mid) return this._query(root.left, l, r);
            if (l >= mid + 1) return this._query(root.right, l, r);
            return Math.max(this._query(root.left, l, mid), this._query(root.right, mid + 1, r));
        }

        private void pushDown(Node root) {
            if (root.dirty == 0) return;
            if (root.left != null)
                this._addNode(root.left, root.left.l, root.left.r, root.dirty);
            if (null != root.right)
                this._addNode(root.right, root.right.l, root.right.r, root.dirty);
            root.dirty = 0;
        }
    }
}
