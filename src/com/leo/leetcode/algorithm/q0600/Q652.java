package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.TreeNode;

import java.util.*;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给定一棵二叉树 root，返回所有重复的子树。
 * 对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
 * 如果两棵树具有相同的结构和相同的结点值，则它们是重复的。
 * 提示：
 * 1、树中的结点数在[1,10^4]范围内。
 * 2、-200 <= Node.val <= 200
 * 链接：https://leetcode-cn.com/problems/find-duplicate-subtrees
 */
public class Q652 {

    public static void main(String[] args) {
        // [[2,4],[4]]
        printTreeList(new Q652().findDuplicateSubtrees(stringToTreeNode("[1,2,3,4,null,2,4,null,null,4]")));
        // [[1]]
        printTreeList(new Q652().findDuplicateSubtrees(stringToTreeNode("[2,1,1]")));
        // [[2,3],[3]]
        printTreeList(new Q652().findDuplicateSubtrees(stringToTreeNode("[2,2,2,3,null,3,null]")));
    }

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> ret = new ArrayList<>();
        func(ret, new HashSet<>(), new HashSet<>(), root);
        return ret;
    }

    void func(List<TreeNode> out, Set<String> set, Set<String> added, TreeNode root) {
        if (root == null) return;
        String hash = treeNodeToString(root);
        if (set.contains(hash)) {
            if (!added.contains(hash)) {
                out.add(root);
                added.add(hash);
            }
        } else set.add(hash);
        func(out, set, added, root.left);
        func(out, set, added, root.right);
    }

    public static String treeNodeToString(TreeNode root) {
        if (root == null) return "[]";
        StringBuilder output = new StringBuilder();
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();
            if (node == null) {
                output.append("null,");
                continue;
            }
            output.append(node.val).append(",");
            nodeQueue.add(node.left);
            nodeQueue.add(node.right);
        }
        return ("[" + output.substring(0, output.length() - 1) + "]");
    }

    static void printTreeList(List<TreeNode> list) {
        System.out.print("[");
        for (TreeNode treeNode : list) {
            System.out.print(treeNodeToString(treeNode));
        }
        System.out.println("]");
    }
}
