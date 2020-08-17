package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定一个二叉树，判断它是否是高度平衡的二叉树。
 * 本题中，一棵高度平衡二叉树定义为：
 * 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
 * 链接：https://leetcode-cn.com/problems/balanced-binary-tree/
 */
public class Q110 {

    public static void main(String[] args) {
        System.out.println(new Q110().isBalanced(LCUtil.stringToTreeNode("[3,9,20,null,null,15,7]"))); // true
        System.out.println(new Q110().isBalanced(LCUtil.stringToTreeNode("[1,2,2,3,3,null,null,4,4]"))); // false
    }

    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        return isBalanced(root.left) && isBalanced(root.right) && Math.abs(deep(root.left) - deep(root.right)) <= 1;
    }

    int deep(TreeNode root) {
        if (null == root) return 0;
        return Math.max(deep(root.left), deep(root.right)) + 1;
    }
}