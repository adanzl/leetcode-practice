package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Q94 {
    public void TestOJ() {
        System.out.println(inorderTraversal(null)); // 6
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        Stack<TreeNode> s = new Stack<>();
        TreeNode p = root;
        while (p != null || !s.empty()) {
            while (p != null) {
                s.push(p);
                p = p.left;
            }
            p = s.pop();
            ret.add(p.val);
            p = p.right;
        }
        return ret;
    }
}
