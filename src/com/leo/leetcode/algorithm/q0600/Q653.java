package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.TreeNode;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
 * 提示:
 * 1、二叉树的节点个数的范围是  [1, 10^4].
 * 2、-10^4 <= Node.val <= 10^4
 * 3、root 为二叉搜索树
 * 4、-10^5 <= k <= 10^5
 * <p>
 * 链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
 */
public class Q653 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q653().findTarget(stringToTreeNode("[2,0,3,-4,1,null,null,-5]"), -9));
        // true
        System.out.println(new Q653().findTarget(stringToTreeNode("[2,0,3,-4,1]"), -1));
        // false
        System.out.println(new Q653().findTarget(stringToTreeNode("[1]"), 2));
        // true
        System.out.println(new Q653().findTarget(stringToTreeNode("[2,1,3]"), 3));
        // true
        System.out.println(new Q653().findTarget(stringToTreeNode("[5,3,6,2,4,null,7]"), 9));
        // false
        System.out.println(new Q653().findTarget(stringToTreeNode("[5,3,6,2,4,null,7]"), 28));
    }

    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> set = new HashSet<>();
        return find(root, k, set);
    }

    public boolean find(TreeNode root, int k, Set<Integer> set) {
        if (root == null) return false;
        if (set.contains(k - root.val)) return true;
        set.add(root.val);
        return find(root.left, k, set) || find(root.right, k, set);
    }
}
