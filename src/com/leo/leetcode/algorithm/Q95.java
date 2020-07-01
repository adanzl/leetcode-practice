package com.leo.leetcode.algorithm;

import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
 * 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
 */
public class Q95 {

    public static void main(String[] args) {
        System.out.println(new Q95().generateTrees(3)); // [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
    }

    int count = 0;
    int limit;
    int[] arr;
    List<TreeNode> out = new ArrayList<>();

    public List<TreeNode> generateTrees(int n) {
        arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = i + 1;
        this.limit = n;
        for (int i = 0; i < arr.length; i++) {
            this.count = 1;
            TreeNode root = new TreeNode(arr[i]);
            buildTree(0, i, 0, root, root);
            buildTree(i + 1, arr.length, 1, root, root);
        }
        return out;
    }

    void buildTree(int l, int r, int flag, TreeNode node, TreeNode root) {
        if (l >= r) {
            return;
        }
        int preCount = count;
        for (int i = l; i < r; i++) {
            TreeNode tNode = new TreeNode(arr[i]);
            if (flag == 0) node.left = tNode;
            else node.right = tNode;
            count++;
            if (count == limit) {
                out.add(cloneTreeNode(root));
                if (flag == 0) node.left = null;
                else node.right = null;
                count--;
                continue;
            }
            buildTree(l, i, 0, tNode, root);
            buildTree(i + 1, r, 1, tNode, root);
        }
        this.count = preCount;
    }

    TreeNode cloneTreeNode(TreeNode node) {
        if (node == null) return null;
        return new TreeNode(node.val, cloneTreeNode(node.left), cloneTreeNode(node.right));
    }
}
