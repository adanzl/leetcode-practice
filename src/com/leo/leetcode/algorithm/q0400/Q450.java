package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;
import static com.leo.utils.LCUtil.treeNodeToString;

/**
 * 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
 * 返回二叉搜索树（有可能被更新）的根节点的引用。
 * 一般来说，删除节点可分为两个步骤：
 * 1、首先找到需要删除的节点；
 * 2、如果找到了，删除它。
 * 提示:
 * 1、节点数的范围 [0, 10^4].
 * 2、-10^5 <= Node.val <= 10^5
 * 3、节点值唯一
 * 4、root 是合法的二叉搜索树
 * 5、-10^5 <= key <= 10^5
 * 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
 * 链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
 */
public class Q450 {

    public static void main(String[] args) {
        // [6,3,7,2,4]
        System.out.println(treeNodeToString(new Q450().deleteNode(stringToTreeNode("[5,3,6,2,4,null,7]"), 5)));
        // [5,4,6,2,null,null,7]
        System.out.println(treeNodeToString(new Q450().deleteNode(stringToTreeNode("[5,3,6,2,4,null,7]"), 3)));
        // [5,3,6,2,4,null,7]
        System.out.println(treeNodeToString(new Q450().deleteNode(stringToTreeNode("[5,3,6,2,4,null,7]"), 0)));
        // []
        System.out.println(treeNodeToString(new Q450().deleteNode(stringToTreeNode("[0]"), 0)));
        // []
        System.out.println(treeNodeToString(new Q450().deleteNode(stringToTreeNode("[]"), 0)));
    }

    public TreeNode deleteNode(TreeNode root, int key) {
        TreeNode p = root, head = new TreeNode(0), pre = head;
        int flag = 0; // left
        head.left = root;
        while (p != null && p.val != key) {
            pre = p;
            if (p.val > key) {
                p = p.left;
                flag = 0;
            } else {
                p = p.right;
                flag = 1;
            }
        }
        if (p != null) {
            if (p.left != null && p.right != null) {
                TreeNode lNode = p.right;
                while (lNode.left != null) lNode = lNode.left;
                p.val = lNode.val;
                p.right = deleteNode(p.right, lNode.val);
            } else {
                TreeNode node = null;
                if (p.left == null && p.right != null) {
                    node = p.right;
                } else if (p.left != null) {
                    node = p.left;
                }
                if (flag == 0) pre.left = node;
                else pre.right = node;
            }
        }
        return head.left;
    }
}
