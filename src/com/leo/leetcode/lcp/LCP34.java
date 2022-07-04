package com.leo.leetcode.lcp;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 小扣有一个根结点为 root 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 val 价值。
 * 小扣出于美观考虑，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 k 个，求所有染成蓝色的结点价值总和最大是多少？
 * 提示：
 * 1、1 <= k <= 10
 * 2、1 <= val <= 10000
 * 3、1 <= 结点数量 <= 10000
 * 链接：https://leetcode.cn/problems/er-cha-shu-ran-se-UGC
 */
public class LCP34 {

    public static void main(String[] args) {
        // 12
        System.out.println(new LCP34().maxValue(stringToTreeNode("[5,2,3,4]"), 2));
        // 16
        System.out.println(new LCP34().maxValue(stringToTreeNode("[4,1,3,9,null,null,2]"), 2));
    }

    public int maxValue(TreeNode root, int k) {
        int[] dp = dynamicProcess(root, k); // dp[1] 表示与当前根节点联通预期蓝色节点个数
        int ret = 0;
        for (int num : dp) ret = Math.max(ret, num);
        return ret;
    }

    // 树状dp
    int[] dynamicProcess(TreeNode root, int k) {
        int[] dp = new int[k + 1];
        if (null == root) return dp;
        int[] dp_left = dynamicProcess(root.left, k), dp_right = dynamicProcess(root.right, k);
        // root 为白色
        int ml = 0, mr = 0;
        for (int i = 0; i <= k; i++) {
            ml = Math.max(ml, dp_left[i]);
            mr = Math.max(mr, dp_right[i]);
        }
        dp[0] = ml + mr;
        // root 为蓝色
        for (int i = 0; i <= k - 1; i++) {
            for (int l = 0; l <= i; l++) {
                int r = i - l;
                dp[i + 1] = Math.max(dp[i + 1], dp_left[l] + dp_right[r] + root.val);
            }
        }
        return dp;
    }
}
