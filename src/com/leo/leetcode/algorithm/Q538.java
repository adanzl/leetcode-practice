package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;
import org.junit.Test;

public class Q538 {
    @Test
    public void TestOJ() {
        System.out.println(LCUtil.treeNodeToString(convertBST(LCUtil.stringToTreeNode("[1,0,4,-2,null,3]")))); // [8,8,4,6,null,7]
        System.out.println(LCUtil.treeNodeToString(convertBST(LCUtil.stringToTreeNode("[2,0,3,-4,1]")))); // [5, 6, 3, 2, 6]
        System.out.println(LCUtil.treeNodeToString(convertBST(LCUtil.stringToTreeNode("[5,2,13]")))); // [18, 20, 13]
    }

    public TreeNode convertBST(TreeNode root) {
        dp(root, 0);
        return root;
    }

    int dp(TreeNode root, int v) {
        if (root == null) return 0;
        if (root.right != null) root.val += dp(root.right, v);
        else root.val += v;
        if (root.left != null) return dp(root.left, root.val);
        else return root.val;
    }
}
