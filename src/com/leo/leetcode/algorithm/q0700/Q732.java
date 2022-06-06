package com.leo.leetcode.algorithm.q0700;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

/**
 * 当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。
 * 给你一些日程安排 [start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。
 * 实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。
 * 1、MyCalendarThree() 初始化对象。
 * 2、int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。
 * 提示：
 * 1、0 <= start < end <= 10^9
 * 2、每个测试用例，调用 book 函数最多不超过 400次
 * 链接：https://leetcode.cn/problems/my-calendar-iii
 */
public class Q732 {

    public static void main(String[] args) {
        MyCalendarThree myCalendarThree = new MyCalendarThree();
        System.out.println(myCalendarThree.book(1, 10));  // 1
        System.out.println(myCalendarThree.book(20, 27)); // 1
        System.out.println(myCalendarThree.book(27, 36)); // 1
        System.out.println(myCalendarThree.book(40, 47)); // 1
        System.out.println(myCalendarThree.book(47, 50)); // 1
        System.out.println(myCalendarThree.book(15, 23)); // 2
        System.out.println(myCalendarThree.book(10, 18)); // 2
        System.out.println(myCalendarThree.book(27, 36)); // 2
        System.out.println(myCalendarThree.book(17, 25)); // 3
        System.out.println(myCalendarThree.book(8, 17)); // 3
        System.out.println(myCalendarThree.book(24, 33)); // 3
        System.out.println(myCalendarThree.book(23, 28)); // 4
        System.out.println(myCalendarThree.book(21, 27)); // 5
        System.out.println(myCalendarThree.book(47, 50)); // 5
        System.out.println(myCalendarThree.book(14, 21)); // 5
        System.out.println(myCalendarThree.book(26, 32)); // 5
        System.out.println(myCalendarThree.book(16, 21)); // 5
        System.out.println(myCalendarThree.book(2, 7)); // 5
        System.out.println(myCalendarThree.book(24, 33)); // 6
        System.out.println(myCalendarThree.book(6, 13)); // 6
        System.out.println(myCalendarThree.book(44, 50)); // 6
        System.out.println(myCalendarThree.book(33, 39)); // 6
        System.out.println(myCalendarThree.book(30, 36)); // 6
        System.out.println(myCalendarThree.book(6, 15)); // 6
        System.out.println(myCalendarThree.book(21, 27)); // 7
        System.out.println(myCalendarThree.book(49, 50)); // 7
        System.out.println(myCalendarThree.book(38, 45)); // 7
        System.out.println(myCalendarThree.book(4, 12)); // 7
        System.out.println(myCalendarThree.book(46, 50)); // 7
        System.out.println(myCalendarThree.book(13, 21)); // 7
        MyCalendar3 obj = new MyCalendar3();
        System.out.println(obj.book(50, 60)); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
        System.out.println(obj.book(10, 20)); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
        System.out.println(obj.book(10, 40)); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
        System.out.println(obj.book(5, 15)); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
        System.out.println(obj.book(5, 10)); // 返回 3
        System.out.println(obj.book(25, 55)); // 返回 3
        MyCalendarThree1 obj1 = new MyCalendarThree1();
        System.out.println(obj1.book(50, 60)); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
        System.out.println(obj1.book(10, 20)); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
        System.out.println(obj1.book(10, 40)); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
        System.out.println(obj1.book(5, 15)); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
        System.out.println(obj1.book(25, 55)); // 返回 3
        System.out.println(obj1.book(5, 10)); // 返回 3
    }

    // 无需查询的线段树
    static class MyCalendarThree {

        Node head = new Node(0, 1_000_000_000);

        public int book(int start, int end) {
            addNode(head, start, end - 1, 1);
            return head.max;
        }

        void addNode(Node node, int l, int r, int val) {
            int mid = node.l + (node.r - node.l) / 2;
            if (node.left == null) node.left = new Node(node.l, mid);
            if (node.right == null) node.right = new Node(mid + 1, node.r);
            if (node.l == l && node.r == r) {
                node.max += val;
                node.dirty += val; // 多次dirty要累加
                return;
            }
            pushDown(node);
            if (mid < l) addNode(node.right, l, r, val);
            else if (r <= mid) addNode(node.left, l, r, val);
            else {
                addNode(node.left, l, mid, val);
                addNode(node.right, mid + 1, r, val);
            }
            node.max = Math.max(node.left.max, node.right.max);
        }

        void pushDown(Node root) {
            if (root.dirty == 0) return;
            addNode(root.left, root.left.l, root.left.r, root.dirty);
            addNode(root.right, root.right.l, root.right.r, root.dirty);
            root.dirty = 0;
        }

        static class Node {
            Node left, right;
            int l, r, max, dirty;

            Node(int l, int r) {
                this.l = l;
                this.r = r;
            }
        }
    }

    // 这个线段树很慢
    static class MyCalendar3 {
        Map<Integer, Integer> tree = new HashMap<>();
        Map<Integer, Integer> lazy = new HashMap<>();

        public int book(int start, int end) {
            update(start, end - 1, 0, 1_000_000_000, 1);
            return tree.getOrDefault(1, 0);
        }

        void update(int s, int e, int l, int r, int idx) {
            if (r < s || e < l) return;
            if (s <= l && r <= e) {
                tree.put(idx, tree.getOrDefault(idx, 0) + 1);
                lazy.put(idx, lazy.getOrDefault(idx, 0) + 1);
            } else {
                int mid = (l + r) >> 1;
                update(s, e, l, mid, 2 * idx);
                update(s, e, mid + 1, r, 2 * idx + 1);
                tree.put(idx, lazy.getOrDefault(idx, 0) + Math.max(tree.getOrDefault(2 * idx, 0), tree.getOrDefault(2 * idx + 1, 0)));
            }
        }
    }

    // 查分计数器
    static class MyCalendarThree1 {
        private final TreeMap<Integer, Integer> cnt = new TreeMap<>();

        public int book(int start, int end) {
            int ans = 0;
            int maxBook = 0;
            cnt.put(start, cnt.getOrDefault(start, 0) + 1);
            cnt.put(end, cnt.getOrDefault(end, 0) - 1);
            for (Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
                int freq = entry.getValue();
                maxBook += freq;
                ans = Math.max(maxBook, ans);
            }
            return ans;
        }
    }
}
