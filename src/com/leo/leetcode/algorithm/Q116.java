package com.leo.leetcode.algorithm;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
 * struct Node {
 * int val;
 * Node *left;
 * Node *right;
 * Node *next;
 * }
 * 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
 * 初始状态下，所有 next 指针都被设置为 NULL。
 * 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
 */
public class Q116 {

    public static void main(String[] args) {
        System.out.println(new Q116().connect(null));
    }

    public Node connect(Node root) {
        if (root == null) return null;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        Node lineEnd = root, pre = null;
        while (!q.isEmpty()) {
            Node p = q.poll();
            if (p.left != null) q.add(p.left);
            if (p.right != null) q.add(p.right);
            if (pre != null) pre.next = p;
            pre = p;
            if (p == lineEnd) {
                p.next = null;
                if (p.left != null) lineEnd = p.left;
                if (p.right != null) lineEnd = p.right;
                pre = null;
            }
        }
        return root;
    }

    static class Node {
        public int val;
        public Node left;
        public Node right;
        public Node next;
    }

}
