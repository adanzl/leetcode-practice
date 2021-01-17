package com.leo.leetcode.algorithm.q0200;

import java.util.ArrayList;
import java.util.List;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定一个二叉树，返回所有从根节点到叶子节点的路径。
 * 说明: 叶子节点是指没有子节点的节点。
 * 链接：https://leetcode-cn.com/problems/binary-tree-paths/
 */
public class Q257 {

    public static void main(String[] args) {
        System.out.println(new Q257().binaryTreePaths(LCUtil.stringToTreeNode("[1,2,3,null,5]"))); // ["1->2->5", "1->3"]
        System.out.println(new Q257().binaryTreePaths(LCUtil.stringToTreeNode("[1,2,3,null,null,5]"))); // ["1->2", "1->3->5"]
        System.out.println(new Q257().binaryTreePaths(LCUtil.stringToTreeNode("[1,2,3,null,null,null,5]"))); // ["1->2", "1->3->5"]
        System.out.println(new Q257().binaryTreePaths(LCUtil.stringToTreeNode("[1]"))); // ["1"]
        System.out.println(new Q257().binaryTreePaths(LCUtil.stringToTreeNode("[]"))); // []
    }

    public List<String> binaryTreePaths(TreeNode root) {
        List<String> out = new ArrayList<>();
        if (root == null) return out;
        buildPath(root, new ArrayList<>(), out);
        return out;
    }

    void buildPath(TreeNode root, List<Integer> path, List<String> out) {
        path.add(root.val);
        if (root.left == null && root.right == null) {
            StringBuilder sb = new StringBuilder();
            for (int v : path) {
                sb.append(v).append("->");
            }
            out.add(sb.substring(0, sb.length() - 2));
            path.remove(path.size() - 1);
            return;
        }
        if (null != root.left) buildPath(root.left, path, out);
        if (null != root.right) buildPath(root.right, path, out);
        path.remove(path.size() - 1);
    }
}