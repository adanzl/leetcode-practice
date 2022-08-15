package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.Executor;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 设计实现双端队列。
 * 实现 MyCircularDeque 类:
 * MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
 * boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
 * boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
 * boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
 * boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
 * int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
 * int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
 * boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
 * boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。
 * 提示：
 * 1、1 <= k <= 1000
 * 2、0 <= value <= 1000
 * 3、insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull  调用次数不大于 2000 次
 * 链接：https://leetcode.cn/problems/design-circular-deque
 */
public class Q641 {

    public static void main(String[] args) {
        MyCircularDeque circularDeque = new MyCircularDeque(3); // 设置容量大小为3
        System.out.println(circularDeque.insertLast(1));                    // 返回 true
        System.out.println(circularDeque.insertLast(2));                    // 返回 true
        System.out.println(circularDeque.insertFront(3));                    // 返回 true
        System.out.println(circularDeque.insertFront(4));                    //) 已经满了，返回 false
        System.out.println(circularDeque.getRear());                // 返回 2
        System.out.println(circularDeque.isFull());                        // 返回 true
        System.out.println(circularDeque.deleteLast());                    // 返回 true
        System.out.println(circularDeque.insertFront(4));                    // 返回 true
        System.out.println(circularDeque.getFront());                // 返回 4
        System.out.println(circularDeque.deleteFront()); // true
        // [null, true, true, true, false, 2, true, true, true, 4]
        new Executor(Q641.class).execute(
                "[\"MyCircularDeque\", \"insertLast\", \"insertLast\", \"insertFront\", \"insertFront\", \"getRear\", \"isFull\", \"deleteLast\", \"insertFront\", \"getFront\"]",
                "[[3], [1], [2], [3], [4], [], [], [], [4], []]");
        // [null,true,true,7,true,7,true,3,9,9,true,0]
        new Executor(Q641.class).execute(
                "[\"MyCircularDeque\",\"insertFront\",\"insertLast\",\"getFront\",\"insertLast\",\"getFront\",\"insertFront\",\"getRear\",\"getFront\",\"getFront\",\"deleteLast\",\"getRear\"]",
                "[[5],[7],[0],[],[3],[],[9],[],[],[],[],[]]");
    }

    static class MyCircularDeque {
        private final Deque<Integer> q;
        private final int limit;

        public MyCircularDeque(int k) {
            q = new ArrayDeque<>(k);
            limit = k;
        }

        public boolean insertFront(int value) {
            if (q.size() >= limit) return false;
            q.addFirst(value);
            return true;
        }

        public boolean insertLast(int value) {
            if (q.size() >= limit) return false;
            q.addLast(value);
            return true;
        }

        public boolean deleteFront() {
            if (q.isEmpty()) return false;
            q.removeFirst();
            return true;
        }

        public boolean deleteLast() {
            if (q.isEmpty()) return false;
            q.removeLast();
            return true;
        }

        public int getFront() {
            if (q.isEmpty()) return -1;
            return q.getFirst();
        }

        public int getRear() {
            if (q.isEmpty()) return -1;
            return q.getLast();
        }

        public boolean isEmpty() {
            return q.isEmpty();
        }

        public boolean isFull() {
            return q.size() == limit;
        }
    }
}
