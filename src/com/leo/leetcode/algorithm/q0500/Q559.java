package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.Node;

import static com.leo.utils.LCUtil.stringToNodeTree;

/**
 * 给定一个 N 叉树，找到其最大深度。
 * 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
 * N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
 * 提示：
 * 1、树的深度不会超过 1000 。
 * 2、树的节点数目位于 [0, 10^4] 之间。
 * 链接：https://leetcode.cn/problems/maximum-depth-of-n-ary-tree
 */
public class Q559 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q559().maxDepth(stringToNodeTree("[1,null,3,2,4,null,5,6]")));
        // 5
        System.out.println(new Q559().maxDepth(stringToNodeTree("[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]")));
    }

    public int maxDepth(Node root) {
        return maxDepth(root, 0);
    }

    int maxDepth(Node root, int depth) {
        if (root == null) return depth;
        if (root.children == null || root.children.size() == 0) return depth + 1;
        int max = depth;
        for (Node child : root.children) {
            max = Math.max(max, maxDepth(child, depth + 1));
        }
        return max;
    }
}
