package com.leo.leetcode.algorithm.q0700;

/**
 * Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。
 * 半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。
 * 实现 RangeModule 类:
 * 1、RangeModule() 初始化数据结构的对象。
 * 2、void addRange(int left, int right) 添加 半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
 * 3、boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true ，否则返回 false 。
 * 4、void removeRange(int left, int right) 停止跟踪 半开区间 [left, right) 中当前正在跟踪的每个实数。
 * 提示：
 * 1、1 <= left < right <= 10^9
 * 2、在单个测试用例中，对 addRange 、  queryRange 和 removeRange 的调用总数不超过 10^4 次
 * 链接：https://leetcode-cn.com/problems/range-module
 */
public class Q715 {

    public static void main(String[] args) {
        RangeModule rangeModule = new RangeModule();
        rangeModule.addRange(10, 180);
        rangeModule.addRange(150, 200);
        rangeModule.addRange(250, 500);
        System.out.println(rangeModule.queryRange(180, 300));
        System.out.println("=============================");
        rangeModule = new RangeModule();
        rangeModule.addRange(10, 20);
        rangeModule.removeRange(14, 16);
        System.out.println(rangeModule.queryRange(10, 14)); // true
        System.out.println(rangeModule.queryRange(13, 15)); // false
        System.out.println(rangeModule.queryRange(16, 17)); // true
    }

    static class RangeModule {

        Node head;

        public RangeModule() {
            head = new Node(1, 1_000_000_000);
        }

        public void addRange(int left, int right) {
            addNode(head, left, right - 1, 1);
        }

        void addNode(Node root, int l, int r, int v) {
            int mid = (root.l + root.r) >> 1;
            if (null == root.left) root.left = new Node(root.l, mid);
            if (null == root.right) root.right = new Node(mid + 1, root.r);
            if (root.l == l && root.r == r) {
                root.v = v;
                root.dirty = v;
                return;
            }
            pushDown(root);
            if (mid < l) addNode(root.right, l, r, v);
            else if (r <= mid) addNode(root.left, l, r, v);
            else {
                addNode(root.left, l, mid, v);
                addNode(root.right, mid + 1, r, v);
            }
            root.v = (root.left.v == 1 && root.right.v == 1) ? 1 : -1;
        }

        boolean query(Node root, int l, int r) {
            if (root == null) return false;
            if (root.l == l && root.r == r) return root.v == 1;
            pushDown(root);
            int mid = (root.l + root.r) >> 1;
            if (mid < l) return query(root.right, l, r);
            if (r <= mid) return query(root.left, l, r);
            return query(root.left, l, mid) && query(root.right, mid + 1, r);
        }

        public boolean queryRange(int left, int right) {
            return query(head, left, right - 1);
        }

        void pushDown(Node root) {
            if (root.dirty == 0) return;
            addNode(root.left, root.left.l, root.left.r, root.dirty);
            addNode(root.right, root.right.l, root.right.r, root.dirty);
            root.dirty = 0;
        }

        public void removeRange(int left, int right) {
            addNode(head, left, right - 1, -1);
        }

        static class Node {
            Node left, right;
            int l, r, dirty, v = -1;

            Node(int l, int r) {
                this.l = l;
                this.r = r;
            }
        }
    }
}
