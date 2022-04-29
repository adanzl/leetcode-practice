package com.leo.leetcode.algorithm.q0400;

import java.util.Stack;

/**
 * 你会得到一个双链表，其中包含的节点有一个下一个指针、一个前一个指针和一个额外的 子指针 。
 * 这个子指针可能指向一个单独的双向链表，也包含这些特殊的节点。
 * 这些子列表可以有一个或多个自己的子列表，以此类推，以生成如下面的示例所示的 多层数据结构 。
 * 给定链表的头节点 head ，将链表 扁平化 ，以便所有节点都出现在单层双链表中。
 * 让 curr 是一个带有子列表的节点。子列表中的节点应该出现在扁平化列表中的 curr 之后 和 curr.next 之前 。
 * 返回 扁平列表的 head 。列表中的节点必须将其 所有 子指针设置为 null 。
 * 提示：
 * 1、节点数目不超过 1000
 * 2、1 <= Node.val <= 10^5
 * 链接：https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list
 */
public class Q430 {
    // 解题10分钟、解析输入输入半小时
    public static void main(String[] args) {
        // [1,2,3]
        System.out.println(listNodeToString(new Q430().flatten(stringToListNode("[1,null,2,null,3,null]"))));
        // [1,2,3,7,8,11,12,9,10,4,5,6]
        System.out.println(listNodeToString(new Q430().flatten(stringToListNode("[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]"))));
        // [1,3,2]
        System.out.println(listNodeToString(new Q430().flatten(stringToListNode("[1,2,null,3]"))));
        // []
        System.out.println(listNodeToString(new Q430().flatten(stringToListNode("[]"))));
    }

    public Node flatten(Node head) {
        Node p = head;
        Stack<Node> stack = new Stack<>();
        while (p != null) {
            if (p.child != null) {
                Node child = p.child;
                stack.push(p.next);
                p.next = child;
                child.prev = p;
                p.child = null;
            }
            if (p.next == null && !stack.empty()) {
                Node last = stack.pop();
                p.next = last;
                if (last != null) {
                    last.prev = p;
                    p = last;
                }
            } else {
                p = p.next;
            }
        }
        return head;
    }

    static class Node {
        public int val;
        public Node prev;
        public Node next;
        public Node child;

        Node(int v) {
            this.val = v;
        }
    }


    public static Node stringToListNode(String input) {
        input = input.trim().substring(1, input.length() - 1);
        if (input.length() == 0) return null;
        String[] parts = input.split(",");
        Node dummyRoot = new Node(-1);
        Node ptr = dummyRoot, point = dummyRoot;
        for (String item : parts) {
            if ("null".equals(item)) {
                point = point.next;
                ptr = null;
                continue;
            }
            Node node = new Node(Integer.parseInt(item));
            if (ptr == null) {
                point.child = node;
                point = new Node(-1);
                point.next = node;
            } else {
                ptr.next = node;
                node.prev = ptr;
            }
            ptr = node;
        }
        return dummyRoot.next;
    }

    public static String listNodeToString(Node node) {
        if (null == node) return "[]";
        StringBuilder output = new StringBuilder();
        while (null != node) {
            output.append(node.val).append(",");
            node = node.next;
        }
        return "[" + output.substring(0, output.length() - 1) + "]";
    }
}