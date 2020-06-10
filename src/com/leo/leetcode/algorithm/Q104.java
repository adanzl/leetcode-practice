package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;
import org.junit.Test;

public class Q104 {
    @Test
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
