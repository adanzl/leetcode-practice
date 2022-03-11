package com.leo.leetcode.algorithm.q0700;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;
import static com.leo.utils.LCUtil.treeNodeToString;

/**
 * 给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。
 * 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
 * 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
 * 提示：
 * 1、树中的节点数将在 [0, 10^4]的范围内。
 * 2、-10^8 <= Node.val <= 10^8
 * 3、所有值 Node.val 是 独一无二 的。
 * 4、-10^8 <= val <= 10^8
 * 5、保证 val 在原始BST中不存在。
 * 链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
 */
public class Q701 {

    public static void main(String[] args) {
        // [4,2,7,1,3,5]
        System.out.println(treeNodeToString(new Q701().insertIntoBST(stringToTreeNode("[4,2,7,1,3]"), 5)));
        // [40,20,60,10,30,50,70,null,null,25]
        System.out.println(treeNodeToString(new Q701().insertIntoBST(stringToTreeNode("[40,20,60,10,30,50,70]"), 25)));
        // [4,2,7,1,3,5]
        System.out.println(treeNodeToString(new Q701().insertIntoBST(stringToTreeNode("[4,2,7,1,3,null,null,null,null,null,null]"), 5)));
    }

    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (null == root) return new TreeNode(val);
        if (val > root.val) root.right = insertIntoBST(root.right, val);
        else if (val < root.val) root.left = insertIntoBST(root.left, val);
        return root;
    }

}
