package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class Q102 {

    public static void main(String[] args) {
        System.out.println(new Q102().levelOrder(LCUtil.stringToTreeNode("[3,9,20,null,null,15,7]"))); // t
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<>();
        if (root == null) {
            return ret;
        }
        List<TreeNode> mark = new ArrayList<>();
        mark.add(root);
        while (!mark.isEmpty()) {
            List<TreeNode> nMark = new ArrayList<>();
            List<Integer> line = new ArrayList<>();
            for (TreeNode tn : mark) {
                line.add(tn.val);
                if (tn.left != null) {
                    nMark.add(tn.left);
                }
                if (tn.right != null) {
                    nMark.add(tn.right);
                }
            }
            ret.add(line);
            mark = nMark;
        }
        return ret;
    }
}
