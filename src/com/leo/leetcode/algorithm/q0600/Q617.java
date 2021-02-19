package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;
import static com.leo.utils.LCUtil.treeNodeToString;


/**
 * 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
 * 你需要将他们合并为一个新的二叉树。
 * 合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
 * 注意: 合并必须从两个树的根节点开始。
 * <p>
 * 链接：https://leetcode-cn.com/problems/merge-two-binary-trees
 */
public class Q617 {
    public static void main(String[] args) {
        // [3, 4, 5, 5, 4, null, 7, null, null, null, null, null, null]
        System.out.println(treeNodeToString(new Q617().mergeTrees(
                stringToTreeNode("[1,3,2,5]"),
                stringToTreeNode("[2,1,3,null,4,null,7]")))
        );
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
