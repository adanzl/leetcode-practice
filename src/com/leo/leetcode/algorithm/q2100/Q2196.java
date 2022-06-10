package com.leo.leetcode.algorithm.q2100;

import com.leo.utils.TreeNode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.treeNodeToString;

/**
 * 给你一个二维整数数组 descriptions ，其中 descriptions[i] = [parent_i, child_i,  isLeft_i] 表示 parent_i 是 child_i 在 二叉树 中的 父节点，
 * 二叉树中各节点的值 互不相同 。此外：
 * 1、如果  isLeft_i == 1 ，那么 child_i 就是 parent_i 的左子节点。
 * 2、如果  isLeft_i == 0 ，那么 child_i 就是 parent_i 的右子节点。
 * 请你根据 descriptions 的描述来构造二叉树并返回其 根节点 。
 * 测试用例会保证可以构造出 有效 的二叉树。
 * 提示：
 * 1、1 <= descriptions.length <= 10^4
 * 2、descriptions[i].length == 3
 * 3、1 <= parent_i, child_i <= 10^5
 * 4、0 <= isLeft_i <= 1
 * 5、descriptions 所描述的二叉树是一棵有效二叉树
 * 链接：https://leetcode.cn/problems/create-binary-tree-from-descriptions
 */
public class Q2196 {

    public static void main(String[] args) {
        // [50,20,80,15,17,19]
        System.out.println(treeNodeToString(new Q2196().createBinaryTree(stringToInt2dArray("[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]"))));
        // [1,2,null,null,3,4]
        System.out.println(treeNodeToString(new Q2196().createBinaryTree(stringToInt2dArray("[[1,2,1],[2,3,0],[3,4,1]]"))));
    }

    public TreeNode createBinaryTree(int[][] descriptions) {
        Set<Integer> set = new HashSet<>();
        Map<Integer, TreeNode> treeNodeMap = new HashMap<>();
        for (int[] desc : descriptions) {
            int parent = desc[0];
            int child = desc[1];
            set.add(parent);
            set.add(child);
            treeNodeMap.put(parent, new TreeNode(parent));
            treeNodeMap.put(child, new TreeNode(child));
        }
        for (int[] desc : descriptions) {
            int parent = desc[0];
            int child = desc[1];
            int isLeft = desc[2];
            set.remove(child);
            if (isLeft == 1) treeNodeMap.get(parent).left = treeNodeMap.get(child);
            else treeNodeMap.get(parent).right = treeNodeMap.get(child);
        }
        return treeNodeMap.get(set.iterator().next());
    }
}
