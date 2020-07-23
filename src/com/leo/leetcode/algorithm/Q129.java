package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
 * 例如，从根到叶子节点路径 1->2->3 代表数字 123。
 * 计算从根到叶子节点生成的所有数字之和。
 * 说明: 叶子节点是指没有子节点的节点。
 * 链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
 */
public class Q129 {

    public static void main(String[] args) {
        System.out.println(new Q129().sumNumbers(LCUtil.stringToTreeNode("[1,2,3]"))); // 25
        System.out.println(new Q129().sumNumbers(LCUtil.stringToTreeNode("[4,9,0,5,1]"))); // 1026
    }

    public int sumNumbers(TreeNode root) {
        return buildSumList(root, 0, 0);
    }

    int buildSumList(TreeNode node, int n, int out) {
        if (node == null) return out;
        int v = n * 10 + node.val;
        if (node.left == null && node.right == null) return out + v;
        out = buildSumList(node.left, v, out);
        return buildSumList(node.right, v, out);
    }
}
