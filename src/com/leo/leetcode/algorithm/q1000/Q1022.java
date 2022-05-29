package com.leo.leetcode.algorithm.q1000;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
 * 例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
 * 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
 * 返回这些数字之和。题目数据保证答案是一个 32 位 整数。
 * 提示：
 * 1、树中的节点数在 [1, 1000] 范围内
 * 2、Node.val 仅为 0 或 1
 * 链接：https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers
 */
public class Q1022 {

    public static void main(String[] args) {
        // 22
        System.out.println(new Q1022().sumRootToLeaf(stringToTreeNode("[1,0,1,0,1,0,1]")));
        // 5
        System.out.println(new Q1022().sumRootToLeaf(stringToTreeNode("[0,1,0,0,null,0,0,null,null,null,1,null,null,null,1]")));
        // 0
        System.out.println(new Q1022().sumRootToLeaf(stringToTreeNode("[0]")));
        // 1
        System.out.println(new Q1022().sumRootToLeaf(stringToTreeNode("[1]")));
    }

    public int sumRootToLeaf(TreeNode root) {
        return sumRootToLeaf(root, 0);
    }

    int sumRootToLeaf(TreeNode root, int val) {
        if (root == null) return 0;
        int v = (val << 1) | root.val;
        if (root.left == null && root.right == null) return v;
        return sumRootToLeaf(root.left, v) + sumRootToLeaf(root.right, v);
    }
}
