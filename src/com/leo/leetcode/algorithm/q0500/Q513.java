package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.TreeNode;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.TreeMap;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
 * 假设二叉树中至少有一个节点。
 * 提示:
 * 1、二叉树的节点个数的范围是 [1,10^4]
 * 2、-2^31 <= Node.val <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/find-bottom-left-tree-value/
 */
public class Q513 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q513().findBottomLeftValue(stringToTreeNode("[2,1,3]")));
        // 7
        System.out.println(new Q513().findBottomLeftValue(stringToTreeNode("[1,2,3,4,null,5,6,null,null,7]")));
    }

    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        TreeNode ret = root;
        while (!q.isEmpty()) {
            int size = q.size();
            ret = null;
            while (size-- > 0 && !q.isEmpty()) {
                TreeNode cur = q.poll();
                if (ret == null) ret = cur;
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
        }
        return ret.val;
    }
}
