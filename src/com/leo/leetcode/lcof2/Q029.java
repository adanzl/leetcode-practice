package com.leo.leetcode.lcof2;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。
 * 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
 * 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
 * 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。
 * 提示：
 * 1、0 <= Number of Nodes <= 5 * 10^4
 * 2、-10^6 <= Node.val <= 10^6
 * 3、-10^6 <= insertVal <= 10^6
 * 链接：https://leetcode.cn/problems/4ueAj6
 */

public class Q029 {

    public static void main(String[] args) {
        // [3,5,6,1]
        print(new Q029().insert(stringToLoopNode("[3,5,1]"), 6));
        // [3,5,0,1]
        print(new Q029().insert(stringToLoopNode("[3,5,1]"), 0));
        // [3,4,1,2]
        print(new Q029().insert(stringToLoopNode("[3,4,1]"), 2));
        // [1]
        print(new Q029().insert(stringToLoopNode("[]"), 1));
        // [1,0]
        print(new Q029().insert(stringToLoopNode("[1]"), 0));
    }

    public Node insert(Node head, int insertVal) {
        Node cur = head, node = new Node(insertVal);
        if (head == null) {
            node.next = node;
            return node;
        }
        while (cur.next != head) {
            if (cur.val <= cur.next.val) {
                if (insertVal >= cur.val && insertVal <= cur.next.val) {
                    node.next = cur.next;
                    cur.next = node;
                    return head;
                }
            } else {
                if (insertVal <= cur.next.val || insertVal >= cur.val) {
                    node.next = cur.next;
                    cur.next = node;
                    return head;
                }
            }
            cur = cur.next;
        }
        cur.next = node;
        node.next = head;
        return head;
    }

    static void print(Node head) {
        Node cur = head;
        System.out.print("[");
        while (cur != null) {
            System.out.print(cur.val + ",");
            cur = cur.next;
            if (cur == head) break;
        }
        System.out.println("]");
    }

    public static Node stringToLoopNode(String input) {
        // Generate array from the input
        int[] nodeValues = stringToIntegerArray(input);
        // Now convert that list into linked list
        Node dummyRoot = new Node(0);
        Node ptr = dummyRoot;
        for (int item : nodeValues) {
            ptr.next = new Node(item);
            ptr = ptr.next;
        }
        ptr.next = dummyRoot.next;
        return dummyRoot.next;
    }

    static class Node {
        int val;
        Node next;

        Node(int x) {
            val = x;
        }
    }
}
