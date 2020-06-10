package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q104 {

    public static void main(String[] args) {
        new Q104().TestOJ();
    }

    public void TestOJ() {
        System.out.println(maxDepth(LCUtil.stringToTreeNode("[3,9,20,null,null,15,7]"))); // 3
    }

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
