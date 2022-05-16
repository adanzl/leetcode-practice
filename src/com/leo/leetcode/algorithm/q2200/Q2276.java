package com.leo.leetcode.algorithm.q2200;

/**
 * 给你区间的 空 集，请你设计并实现满足要求的数据结构：
 * 1、新增：添加一个区间到这个区间集合中。
 * 2、统计：计算出现在 至少一个 区间中的整数个数。
 * 实现 CountIntervals 类：
 * 1、CountIntervals() 使用区间的空集初始化对象
 * 2、void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
 * 3、int count() 返回出现在 至少一个 区间中的整数个数。
 * 注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。
 * 提示：
 * 1、1 <= left <= right <= 10^9
 * 2、最多调用  add 和 count 方法 总计 10^5 次
 * 3、调用 count 方法至少一次
 * 链接：https://leetcode.cn/problems/count-integers-in-intervals
 */
public class Q2276 {

    public static void main(String[] args) {
        CountIntervals countIntervals;
        // =====================================
        countIntervals = new CountIntervals();
        countIntervals.add(5, 10);
        countIntervals.add(5, 10);
        System.out.println(countIntervals.count()); // 6
        // =====================================
        countIntervals = new CountIntervals();
        countIntervals.add(5, 10);
        countIntervals.add(3, 5);
        System.out.println(countIntervals.count()); // 8
        // =====================================
        countIntervals = new CountIntervals();
        countIntervals.add(39, 44);
        countIntervals.add(13, 49);
        System.out.println(countIntervals.count()); // 37
        // =====================================
        countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
        countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
        countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
        System.out.println(countIntervals.count()); // 6
        countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
        System.out.println(countIntervals.count()); // 8
    }

    static class CountIntervals {

        Node head = new Node(0, 1_000_000_001);

        public void add(int left, int right) {
            addNode(head, left, right);
        }

        public int count() {
            return head.v;
        }

        void addNode(Node root, int l, int r) {
            int mid = (root.l + root.r) >> 1;
            if (root.left == null) root.left = new Node(root.l, mid);
            if (root.right == null) root.right = new Node(mid + 1, root.r);
            if (root.l == l && r == root.r) {
                root.dirty = 1;
                root.v = r - l + 1;
                return;
            }
            pushDown(root);
            if (r <= mid) {
                addNode(root.left, l, r);
            } else if (l >= mid + 1) {
                addNode(root.right, l, r);
            } else {
                addNode(root.left, l, mid);
                addNode(root.right, mid + 1, r);
            }
            root.v = root.left.v + root.right.v;
        }

        void pushDown(Node root) {
            if (root.dirty == 0) return;
            addNode(root.left, root.left.l, root.left.r);
            addNode(root.right, root.right.l, root.right.r);
            root.dirty = 0;
        }

        static class Node {
            Node left, right;
            int l, r, v, dirty;

            Node(int l, int r) {
                this.l = l;
                this.r = r;
            }
        }
    }

}