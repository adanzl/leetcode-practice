package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Q107 {


    public static void main(String[] args) {
        System.out.println(new Q107().levelOrderBottom(LCUtil.stringToTreeNode("[3,9,20,null,null,15,7]"))); // [[15,7], [9,20], [3]]
        System.out.println(new Q107().levelOrderBottom(LCUtil.stringToTreeNode("[]"))); // []
    }

    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> out = new LinkedList<>();
        TreeNode p = root;
        LinkedList<TreeNode> q = new LinkedList<>();
        if (root != null) q.push(root);
        List<Integer> ans = null;
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (ans == null) {
                ans = new ArrayList<>();
                out.addFirst(ans);
            }
            ans.add(n.val);
            if (n.left != null) q.addLast(n.left);
            if (n.right != null) q.addLast(n.right);
            if (p == n) {
                ans = null;
                if (!q.isEmpty()) p = q.getLast();
            }
        }
        return out;
    }
}
