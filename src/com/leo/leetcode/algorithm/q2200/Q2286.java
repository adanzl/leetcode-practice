package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;

/**
 * 一个音乐会总共有 n 排座位，编号从 0 到 n - 1 ，每一排有 m 个座椅，编号为 0 到 m - 1 。你需要设计一个买票系统，针对以下情况进行座位安排：
 * 1、同一组的 k 位观众坐在 同一排座位，且座位连续 。
 * 2、k 位观众中 每一位 都有座位坐，但他们 不一定 坐在一起。
 * 由于观众非常挑剔，所以：
 * 1、只有当一个组里所有成员座位的排数都 小于等于 maxRow ，这个组才能订座位。每一组的 maxRow 可能 不同 。
 * 2、如果有多排座位可以选择，优先选择 最小 的排数。如果同一排中有多个座位可以坐，优先选择号码 最小 的。
 * 请你实现 BookMyShow 类：
 * 1、BookMyShow(int n, int m) ，初始化对象，n 是排数，m 是每一排的座位数。
 * 2、int[] gather(int k, int maxRow) 返回长度为 2 的数组，表示 k 个成员中 第一个座位 的排数和座位编号，这 k 位成员必须坐在 同一排座位，且座位连续 。换言之，返回最小可能的 r 和 c 满足第 r 排中 [c, c + k - 1] 的座位都是空的，且 r <= maxRow 。如果 无法 安排座位，返回 [] 。
 * 3、boolean scatter(int k, int maxRow) 如果组里所有 k 个成员 不一定 要坐在一起的前提下，都能在第 0 排到第 maxRow 排之间找到座位，那么请返回 true 。这种情况下，每个成员都优先找排数 最小 ，然后是座位编号最小的座位。如果不能安排所有 k 个成员的座位，请返回 false 。
 * 提示：
 * 1、1 <= n <= 5 * 10^4
 * 2、1 <= m, k <= 10^9
 * 3、0 <= maxRow <= n - 1
 * 4、gather 和 scatter 总 调用次数不超过 5 * 10^4 次。
 * 链接：https://leetcode.cn/problems/booking-concert-tickets-in-groups
 */
public class Q2286 {

    public static void main(String[] args) {
        BookMyShow q;
        q = new BookMyShow(5, 10);
        System.out.println(q.scatter(9, 1)); // true
        System.out.println(q.scatter(1, 3)); // true
        System.out.println(Arrays.toString(q.gather(3, 4))); // [1,0]
        System.out.println(Arrays.toString(q.gather(1, 1))); // [1,3]
        System.out.println(Arrays.toString(q.gather(10, 4))); // [2,0]
        System.out.println("================================================");
        q = new BookMyShow(3, 999_999_999);
        System.out.println(q.scatter(1_000_000_000, 2)); // true
        System.out.println(Arrays.toString(q.gather(999999999, 2))); // [2,0]
        System.out.println(Arrays.toString(q.gather(999999999, 2))); // []
        System.out.println(Arrays.toString(q.gather(999999999, 2))); // []
        System.out.println("================================================");
        q = new BookMyShow(5, 9);
        System.out.println(Arrays.toString(q.gather(10, 1))); // []
        System.out.println(q.scatter(3, 3)); // true
        System.out.println(Arrays.toString(q.gather(9, 1))); // [1,0]
        System.out.println(Arrays.toString(q.gather(10, 2))); // []
        System.out.println(Arrays.toString(q.gather(2, 0))); // [0,3]
        System.out.println("================================================");
    }

    // 维护区间最大值的线段树
    static class BookMyShow {

        int m;
        Node head;

        public BookMyShow(int n, int m) {
            head = new Node(0, n - 1);
            addNode(head, 0, n - 1, m);
            this.m = m;
        }

        public int[] gather(int k, int maxRow) {
            int l = 0, r = maxRow, line = -1;
            long[] ans = null;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                long[] q = query(head, 0, mid);
                if (q[0] >= k) {
                    r = mid - 1;
                    ans = q;
                    line = mid;
                } else l = mid + 1;
            }
            if (ans == null) return new int[0];
            addNode(head, line, line, ans[0] - k);
            return new int[]{line, m - (int) ans[0]};
        }

        public boolean scatter(int k, int maxRow) {
            int l = 0, r = maxRow, line = -1;
            long[] ans = null;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                long[] q = query(head, 0, mid);
                if (q[1] >= k) {
                    r = mid - 1;
                    ans = q;
                    line = mid;
                } else l = mid + 1;
            }
            if (ans == null) return false;
            if (line > 0) addNode(head, 0, line - 1, 0);
            addNode(head, line, line, ans[1] - k);
            return true;
        }

        void addNode(Node root, int l, int r, long v) {
            int mid = root.l + (root.r - root.l) / 2;
            if (root.left == null) root.left = new Node(root.l, mid);
            if (root.right == null) root.right = new Node(mid + 1, root.r);
            if (root.l == l && r == root.r) {
                root.dirty = v;
                root.v = (r - l + 1) * v;
                root.max = v;
                root.sum = (r - l + 1) * v;
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
            root.sum = root.left.sum + root.right.sum;
            root.v = v;
        }

        long[] query(Node root, int l, int r) {
            if (root == null) return new long[]{0, 0};
            if (root.l == l && root.r == r) return new long[]{root.max, root.sum};
            pushDown(root);
            int mid = root.l + (root.r - root.l) / 2;
            if (mid < l) return query(root.right, l, r);
            if (r <= mid) return query(root.left, l, r);
            long[] qLeft = query(root.left, l, mid), qRight = query(root.right, mid + 1, r);
            return new long[]{Math.max(qLeft[0], qRight[0]), qLeft[1] + qRight[1]};
        }

        void pushDown(Node root) {
            if (root.dirty == -1) return;
            addNode(root.left, root.left.l, root.left.r, root.dirty);
            addNode(root.right, root.right.l, root.right.r, root.dirty);
            root.dirty = -1;
        }

        static class Node {
            Node left, right;
            int l, r;
            long v, sum, max, dirty = -1;

            Node(int l, int r) {
                this.l = l;
                this.r = r;
            }
        }
    }
}

