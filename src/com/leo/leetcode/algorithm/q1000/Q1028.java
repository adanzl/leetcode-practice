package com.leo.leetcode.algorithm.q1000;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 我们从二叉树的根节点 root 开始进行深度优先搜索。
 * 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
 * 如果节点只有一个子节点，那么保证该子节点为左子节点。
 * 给出遍历输出 S，还原树并返回其根节点 root。
 * 链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal
 */
public class Q1028 {
    public static void main(String[] args) {
        System.out.println(LCUtil.treeNodeToString(new Q1028().recoverFromPreorder("1-2--3--4-5--6--7"))); // [1,2,5,3,4,6,7]
        System.out.println(LCUtil.treeNodeToString(new Q1028().recoverFromPreorder("1-2--3---4-5--6---7"))); // [1,2,5,3,null,6,null,4,null,7]
        System.out.println(LCUtil.treeNodeToString(new Q1028().recoverFromPreorder("1-401--349---90--88"))); // [1,401,null,349,88,90]
    }

    public TreeNode recoverFromPreorder(String S) {
        return buildTree(S.toCharArray(), 0);
    }

    int offset = 0;

    TreeNode buildTree(char[] str, int deep) {
        if (offset == str.length) return null;
        int v = 0, d = 0;
        while (str[offset] == '-') {
            d++;
            offset++;
        }
        if (d != deep) {
            offset -= d;
            return null;
        }
        while (offset != str.length && str[offset] != '-') {
            v = v * 10 + str[offset] - '0';
            offset++;
        }
        TreeNode root = new TreeNode(v);
        root.left = buildTree(str, d + 1);
        root.right = buildTree(str, d + 1);
        return root;
    }
}
