package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q617 {
    public void TestOJ() {
        System.out.println(
                LCUtil.treeNodeToString(
                        mergeTrees(
                                LCUtil.stringToTreeNode("[1,3,2,5]"),
                                LCUtil.stringToTreeNode("[2,1,3,null,4,null,7]")
                        )
                )
        ); // [3, 4, 5, 5, 4, null, 7, null, null, null, null, null, null]
    }

    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null) return t2;
        if (t2 == null) return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
    }
}
