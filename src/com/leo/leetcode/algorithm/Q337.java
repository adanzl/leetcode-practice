package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q337 {

    public void TestOJ() {
        System.out.println(rob(LCUtil.stringToTreeNode("[3,2,3,null,3,null,1]"))); // 7
        System.out.println(rob(LCUtil.stringToTreeNode("[3,4,5,1,3,null,1]"))); // 9
    }


    public int rob(TreeNode root) {
        if (root == null) return 0;
        int[] ret = dp(root);
        return Math.max(ret[0], ret[1]);
    }

    /**
     * arr[0] 选择根节点最大值
     * arr[1] 不选择根节点最大值
     */
    int[] dp(TreeNode root) {
        if (root == null) return new int[]{0, 0};
        int[] ret = new int[2];
        int[] left = dp(root.left);
        int[] right = dp(root.right);
        ret[0] = left[1] + right[1] + root.val;
        ret[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return ret;
    }
}
