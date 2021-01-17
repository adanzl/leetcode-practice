package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Q144 {
    public void TestOJ() {
        System.out.println(preOrderTraversal(LCUtil.stringToTreeNode("[1,null,2,3]"))); // [1,2,3]
    }

    /**
     *
     */
    public List<Integer> preOrderTraversal(TreeNode root) {
        Stack<TreeNode> s = new Stack<>();
        List<Integer> out = new ArrayList<>();
        TreeNode p = root;
        while (!s.empty() || p != null) {
            if (p != null) {
                // preOrder
                out.add(p.val);
                s.push(p);
                p = p.left;
            } else {
                p = s.pop();
                // midOrder
                p = p.right;
            }
        }
        return out;
    }
}
