package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 二叉搜索树中的两个节点被错误地交换。
 * 请在不改变其结构的情况下，恢复这棵树。
 * 进阶:
 * 使用 O(n) 空间复杂度的解法很容易实现。
 * 你能想出一个只使用常数空间的解决方案吗？
 * 链接：https://leetcode-cn.com/problems/recover-binary-search-tree/
 */
public class Q99 {
    public static void main(String[] args) {
        TreeNode treeNode;
        treeNode = LCUtil.stringToTreeNode("[1,3,null,null,2]");
        new Q99().recoverTree(treeNode);
        System.out.println(LCUtil.treeNodeToString(treeNode)); // [3,1,null,null,2]

        treeNode = LCUtil.stringToTreeNode("[3,1,4,null,null,2]");
        new Q99().recoverTree(treeNode);
        System.out.println(LCUtil.treeNodeToString(treeNode)); // [2,1,4,null,null,3]

        treeNode = LCUtil.stringToTreeNode("[]");
        new Q99().recoverTree(treeNode);
        System.out.println(LCUtil.treeNodeToString(treeNode)); // []
    }

    TreeNode[] treeNodes = new TreeNode[2];
    int offset = 0;
    TreeNode preNode;

    public void recoverTree(TreeNode root) {
        process(root);
        if (offset == 0) return;
        int t = treeNodes[0].val;
        treeNodes[0].val = treeNodes[1].val;
        treeNodes[1].val = t;
    }

    public void process(TreeNode root) {
        if (root == null || offset == 2) return;
        process(root.left);
        if (preNode != null && preNode.val > root.val) {
            if (offset == 0) {
                treeNodes[offset++] = preNode;
                treeNodes[1] = root;
            } else treeNodes[offset++] = root;
        }
        preNode = root;
        process(root.right);
    }

}
