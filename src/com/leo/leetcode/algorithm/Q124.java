package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q124 {

    public static void main(String[] args) {
        new Q124().TestOJ();
    }

    public void TestOJ() {
        System.out.println(maxPathSum(LCUtil.stringToTreeNode("[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]"))); // 16
        System.out.println(maxPathSum(LCUtil.stringToTreeNode("[2,-1]"))); // 2
        System.out.println(maxPathSum(LCUtil.stringToTreeNode("[1,1]"))); // 2
        System.out.println(maxPathSum(LCUtil.stringToTreeNode("[1,2,3]"))); // 6
        System.out.println(maxPathSum(LCUtil.stringToTreeNode("[-10,9,20,null,null,15,7]"))); // 42
    }

    // f(n) = node_max_path_val(node)
    // f(node) = node.val + max(f(node.left), f(node.right))
    // node == null, val = 0

    int MAX;

    public int maxPathSum(TreeNode root) {
        MAX = Integer.MIN_VALUE;
        search(root);
        return MAX;
    }

    int search(TreeNode root) {
        if (root == null) return 0;
        int left = search(root.left);
        int right = search(root.right);
        MAX = Math.max(MAX, root.val + left + right); // 内部完成
        MAX = Math.max(MAX, root.val); // 不走了
        root.val = root.val + Math.max(left, Math.max(right, 0));
        MAX = Math.max(MAX, root.val); // 向左或者向右
        return root.val;
    }
}
