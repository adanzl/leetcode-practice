package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.TreeNode;

import java.util.*;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
 * 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
 * 提示:
 * 1、节点数在 [1, 10^4] 范围内
 * 2、-10^5 <= Node.val <= 10^5
 * 链接：https://leetcode.cn/problems/most-frequent-subtree-sum
 */
public class Q508 {

    public static void main(String[] args) {
        // [2]
        System.out.println(Arrays.toString(new Q508().findFrequentTreeSum(stringToTreeNode("[5,2,-5]"))));
        // [2,-3,4]
        System.out.println(Arrays.toString(new Q508().findFrequentTreeSum(stringToTreeNode("[5,2,-3]"))));
    }

    Map<Integer, Integer> cMap = new HashMap<>();

    public int[] findFrequentTreeSum(TreeNode root) {
        dfs(root);
        List<int[]> list = new ArrayList<>(cMap.size()), ret = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : cMap.entrySet()) {
            list.add(new int[]{entry.getKey(), entry.getValue()});
        }
        list.sort((a, b) -> b[1] - a[1]);
        for (int i = 0; i < list.size(); i++) {
            if (i > 0 && list.get(i)[1] != list.get(i - 1)[1]) break;
            ret.add(list.get(i));
        }
        return Arrays.stream(ret.toArray(new int[0][])).mapToInt(a -> a[0]).toArray();
    }

    int dfs(TreeNode root) {
        if (null == root) return 0;
        int ret = root.val + dfs(root.left) + dfs(root.right);
        cMap.put(ret, cMap.getOrDefault(ret, 0) + 1);
        return ret;
    }

}
