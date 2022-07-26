package com.leo.leetcode.algorithm.q1200;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * 不使用任何库函数，设计一个 跳表 。
 * 跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。
 * 例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作：
 * 跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。
 * 了解更多 : https://en.wikipedia.org/wiki/Skip_list
 * 在本题中，你的设计应该要包含这些函数：
 * 1、bool search(int target) : 返回target是否存在于跳表中。
 * 2、void add(int num): 插入一个元素到跳表。
 * 3、bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
 * 注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。
 * 提示:
 * 1、0 <= num, target <= 2 * 10^4
 * 2、调用search, add,  erase操作次数不大于 5 * 10^4
 * 链接：https://leetcode.cn/problems/design-skiplist
 */
public class Q1206 {

    public static void main(String[] args) {
        Skiplist skiplist = new Skiplist();
        skiplist.add(0);
        skiplist.add(5);
        skiplist.add(2);
        skiplist.add(1);
        // true
        System.out.println(skiplist.search(0));
        // true
        System.out.println(skiplist.erase(5));
        // true
        System.out.println(skiplist.search(2));
        // false
        System.out.println(skiplist.search(3));
        // true
        System.out.println(skiplist.search(2));

    }

    static class Skiplist {

        List<Node> head;

        public Skiplist() {
            head = new ArrayList<>();
            head.add(new Node(-1));
        }

        public boolean search(int target) {
            Node p = head.get(head.size() - 1);
            while (p != null) {
                while (p.next != null && p.next.val <= target) p = p.next;
                if (p.val == target) return true;
                p = p.down;
            }
            return false;
        }

        public void add(int num) {
            Node h = head.get(0), preNew = null;
            double r = 0;
            while (0.2 > r) {
                Node p = h;
                while (p.next != null && p.next.val <= num) p = p.next;
                Node newNode = new Node(num);
                newNode.next = p.next;
                if (p.next != null) p.next.pre = newNode;
                newNode.down = preNew;
                if (preNew != null) preNew.up = newNode;
                p.next = newNode;
                newNode.pre = p;
                r = new Random().nextDouble();
                preNew = newNode;
                if (h.up == null) {
                    h.up = new Node(-1);
                    h.up.down = h;
                    head.add(h.up);
                }
                h = h.up;
            }
        }

        public boolean erase(int num) {
            Node p = head.get(head.size() - 1), node = null;
            boolean find = false;
            while (p != null) {
                while (p.next != null && p.next.val <= num) p = p.next;
                if (p.val == num) {
                    node = p;
                    find = true;
                }
                p = p.down;
            }
            while (node != null) {
                node.pre.next = node.next;
                if (node.next != null) node.next.pre = node.pre;
                node = node.up;
            }
            return find;
        }

        static class Node {
            Node down, next, pre, up;
            int val;

            Node(int num) {
                this.val = num;
            }
        }
    }
}
