package com.leo.leetcode.algorithm.q0100;

/**
 * 给定一个二叉树
 * struct Node {
 * int val;
 * Node *left;
 * Node *right;
 * Node *next;
 * }
 * 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
 * 初始状态下，所有 next 指针都被设置为 NULL。
 * <p>
 * 进阶：
 * 你只能使用常量级额外空间。
 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 * 提示：
 * 树中的节点数小于 6000
 * -100 <= node.val <= 100
 * 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
 */
public class Q117 {
    public static void main(String[] args) {
        System.out.println(new Q117().connect(null));
    }

    public Node connect(Node root) {
        Node lastNode = null, nextLine = null;
        Node pNode = root;
        while (pNode != null) {
            if (pNode.left != null) {
                if (lastNode != null) lastNode.next = pNode.left;
                else nextLine = pNode.left;
                lastNode = pNode.left;
            }
            if (pNode.right != null) {
                if (lastNode != null) lastNode.next = pNode.right;
                else nextLine = pNode.right;
                lastNode = pNode.right;
            }
            pNode = pNode.next;
            if (pNode == null) {
                pNode = nextLine;
                nextLine = null;
                lastNode = null;
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
