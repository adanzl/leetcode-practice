package com.leo.leetcode.algorithm.q0700;

/**
 * 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。
 * 如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
 * 在链表类中实现这些功能：
 * get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
 * addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
 * addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
 * addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。
 * 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
 * deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 * 提示：
 * 1、所有val值都在 [1, 1000] 之内。
 * 2、操作次数将在  [1, 1000] 之内。
 * 3、请不要使用内置的 LinkedList 库。
 * 链接：https://leetcode-cn.com/problems/design-linked-list
 */
public class Q707 {

    public static void main(String[] args) {
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        linkedList.addAtTail(3);
        // 链表变为1-> 2-> 3
        linkedList.addAtIndex(1, 2);
        // 返回2
        System.out.println(linkedList.get(1));
        // 现在链表是1-> 3
        linkedList.deleteAtIndex(1);
        // 返回3
        System.out.println(linkedList.get(1));
        linkedList.addAtIndex(2, 2);
        // -1
        System.out.println(linkedList.get(10));

        linkedList = new MyLinkedList();
        linkedList.addAtHead(7); // 7
        linkedList.addAtHead(2); // 2-7
        linkedList.addAtHead(1); // 1-2-7
        linkedList.addAtIndex(3, 0); // 1-2-7-0
        linkedList.deleteAtIndex(2); // 1-2-0
        linkedList.addAtHead(6); // 6-1-2-0
        linkedList.addAtTail(4); // 6-1-2-0-4
        System.out.println(linkedList.get(4)); // 4
        linkedList.addAtHead(4); // 4-6-1-2-0-4
        linkedList.addAtIndex(5, 0); // 4-6-1-2-0-4-0
        linkedList.addAtHead(6); // 6-4-6-1-2-0-4-0
        System.out.println(linkedList.get(5)); // 0
    }

    static class MyLinkedList {

        static class MNode {
            MNode(int v) {
                this.v = v;
            }

            int v;
            MNode next;
        }

        MNode head = new MNode(-1);
        MNode tail = head;
        int len = 0;

        public MyLinkedList() {

        }

        public int get(int index) {
            MNode n = node(index);
            return null == n ? -1 : n.v;
        }

        public void addAtHead(int val) {
            MNode n = new MNode(val);
            n.next = head.next;
            head.next = n;
            if (len == 0) tail = n;
            len++;
        }

        public void addAtTail(int val) {
            MNode n = new MNode(val);
            tail.next = n;
            tail = n;
            len++;
        }

        public void addAtIndex(int index, int val) {
            MNode n = node(index);
            MNode pre = node(index - 1);
            if (pre == null) return;
            MNode node = new MNode(val);
            node.next = n;
            pre.next = node;
            if (len == index) tail = node;
            len++;
        }

        public void deleteAtIndex(int index) {
            MNode n = node(index);
            if (n == null) return;
            MNode pre = node(index - 1);
            if (pre == null) return;
            pre.next = n.next;
            if (len - 1 == index) tail = pre;
            --len;
        }

        private MNode node(int idx) {
            if (idx >= len) return null;
            MNode p = head;
            while (idx-- >= 0) p = p.next;
            return p;
        }
    }
}
