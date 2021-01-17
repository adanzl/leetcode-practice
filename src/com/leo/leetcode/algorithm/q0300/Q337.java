package com.leo.leetcode.algorithm.q0300;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
 * 这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
 * 一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
 * 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
 * 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
 * 链接：https://leetcode-cn.com/problems/house-robber-iii
 */
public class Q337 {

    public static void main(String[] args) {
        System.out.println(new Q337().rob(LCUtil.stringToTreeNode("[2,1,3,null,4]"))); // 7
        System.out.println(new Q337().rob(LCUtil.stringToTreeNode("[3,2,3,null,3,null,1]"))); // 7
        System.out.println(new Q337().rob(LCUtil.stringToTreeNode("[3,4,5,1,3,null,1]"))); // 9
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
        if (root == null) return new int[] { 0, 0 };
        int[] ret = new int[2];
        int[] left = dp(root.left);
        int[] right = dp(root.right);
        ret[0] = left[1] + right[1] + root.val;
        ret[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return ret;
    }
}
