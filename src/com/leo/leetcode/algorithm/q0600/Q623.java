package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

import static com.leo.utils.LCUtil.stringToTreeNode;
import static com.leo.utils.LCUtil.treeNodeToString;

/**
 * 给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。
 * 注意，根节点 root 位于深度 1 。
 * 加法规则如下:
 * 1、给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。
 * 2、cur 原来的左子树应该是新的左子树根的左子树。
 * 3、cur 原来的右子树应该是新的右子树根的右子树。
 * 4、如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。
 * 提示:
 * 1、节点数在 [1, 10^4] 范围内
 * 2、树的深度在 [1, 10^4]范围内
 * 3、-100 <= Node.val <= 100
 * 4、-10^5 <= val <= 10^5
 * 5、1 <= depth <= the depth of tree + 1
 * 链接：https://leetcode.cn/problems/add-one-row-to-tree
 */
public class Q623 {

    public static void main(String[] args) {
        // [4,1,1,2,null,null,6,3,1,5]
        System.out.println(treeNodeToString(new Q623().addOneRow(stringToTreeNode("[4,2,6,3,1,5]"), 1, 2)));
        // [4,2,null,1,1,3,null,null,1]
        System.out.println(treeNodeToString(new Q623().addOneRow(stringToTreeNode("[4,2,null,3,1]"), 1, 3)));
        // [4, 1, 1, 2, null, null, 6, 3, 1, 5]
        System.out.println(treeNodeToString(new Q623().addOneRow(stringToTreeNode("[4,2,6,3,1,5]"), 1, 2)));
        // [4,1,1,2,null,null,null,3,1]
        System.out.println(treeNodeToString(new Q623().addOneRow(stringToTreeNode("[4,2,null,3,1]"), 1, 2)));
    }

    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            TreeNode ret = new TreeNode(val);
            ret.left = root;
            return ret;
        }
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        int d = 1;
        TreeNode p = root;
        while (!q.isEmpty() && d < depth - 1) {
            TreeNode cur = q.poll();
            if (cur.left != null) q.add(cur.left);
            if (cur.right != null) q.add(cur.right);
            if (cur == p && !q.isEmpty()) {
                d++;
                p = q.getLast();
            }
        }
        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            TreeNode l = new TreeNode(val), r = new TreeNode(val);
            l.left = cur.left;
            r.right = cur.right;
            cur.left = l;
            cur.right = r;
        }
        return root;
    }
}
