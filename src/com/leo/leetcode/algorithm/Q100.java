package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定两个二叉树，编写一个函数来检验它们是否相同。
 * 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
 * 链接：https://leetcode-cn.com/problems/same-tree/
 */
public class Q100 {

    public static void main(String[] args) {
        System.out.println(new Q100().isSameTree(LCUtil.stringToTreeNode("[1,2,3]"), LCUtil.stringToTreeNode("[1,2,3]"))); // true
        System.out.println(new Q100().isSameTree(LCUtil.stringToTreeNode("[1,2]"), LCUtil.stringToTreeNode("[1,null,2]"))); // false
        System.out.println(new Q100().isSameTree(LCUtil.stringToTreeNode("[1,2,1]"), LCUtil.stringToTreeNode("[1,1,2]"))); // false
        System.out.println(new Q100().isSameTree(LCUtil.stringToTreeNode("[]"), LCUtil.stringToTreeNode("[1]"))); // false
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == q) return true;
        if (p == null || q == null) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right) && p.val == q.val;
    }
}