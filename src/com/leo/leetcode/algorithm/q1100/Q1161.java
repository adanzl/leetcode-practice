package com.leo.leetcode.algorithm.q1100;

import com.leo.utils.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
 * 请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
 * 提示：
 * 1、树中的节点数在 [1, 104]范围内
 * 2、-10^5 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree
 */
public class Q1161 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1161().maxLevelSum(stringToTreeNode("[989,null,10250,98693,-89388,null,null,null,-32127]")));
        // 2
        System.out.println(new Q1161().maxLevelSum(stringToTreeNode("[1,7,0,7,-8,null,null]")));
    }

    public int maxLevelSum(TreeNode root) {
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        int ret = 0, sum = 0, max = Integer.MIN_VALUE, line = 1;
        TreeNode endLine = root;
        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            if (cur.left != null) q.offer(cur.left);
            if (cur.right != null) q.offer(cur.right);
            sum += cur.val;
            if (cur == endLine) {
                if (sum > max) {
                    max = sum;
                    ret = line;
                }
                if (q.isEmpty()) break;
                endLine = q.getLast();
                sum = 0;
                line++;
            }
        }
        if (sum > max) ret = line;
        return ret;
    }
}
