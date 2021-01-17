package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.TreeNode;

import java.util.LinkedList;
import java.util.List;

import static com.leo.utils.LCUtil.treeNodeArrayToString;

/**
 * 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
 * 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
 */
public class Q95 {

    public static void main(String[] args) {
        System.out.println(treeNodeArrayToString(new Q95().generateTrees(4))); //
        System.out.println(treeNodeArrayToString(new Q95().generateTrees(3))); // [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
    }

    public LinkedList<TreeNode> generate_trees(int start, int end) {
        LinkedList<TreeNode> all_trees = new LinkedList<>();
        if (start > end) {
            all_trees.add(null);
            return all_trees;
        }
        // pick up a root
        for (int i = start; i <= end; i++) {
            // all possible left subtrees if i is chosen to be a root
            LinkedList<TreeNode> left_trees = generate_trees(start, i - 1);
            // all possible right subtrees if i is chosen to be a root
            LinkedList<TreeNode> right_trees = generate_trees(i + 1, end);
            // connect left and right trees to the root i
            for (TreeNode l : left_trees) {
                for (TreeNode r : right_trees) {
                    TreeNode current_tree = new TreeNode(i);
                    current_tree.left = l;
                    current_tree.right = r;
                    all_trees.add(current_tree);
                }
            }
        }
        return all_trees;
    }

    public List<TreeNode> generateTrees(int n) {
        if (n == 0) {
            return new LinkedList<>();
        }
        return generate_trees(1, n);
    }
}
