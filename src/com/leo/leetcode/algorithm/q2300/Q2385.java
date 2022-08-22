package com.leo.leetcode.algorithm.q2300;

import com.leo.utils.TreeNode;

import java.util.*;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。
 * 每分钟，如果节点满足以下全部条件，就会被感染：
 * 1、节点此前还没有感染。
 * 2、节点与一个已感染节点相邻。
 * 返回感染整棵树需要的分钟数。
 * 提示：
 * 1、树中节点的数目在范围 [1, 10^5] 内
 * 2、1 <= Node.val <= 10^5
 * 3、每个节点的值 互不相同
 * 4、树中必定存在值为 start 的节点
 * 链接：https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected
 */
public class Q2385 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2385().amountOfTime(stringToTreeNode("[1,5,3,null,4,10,6,9,2]"), 3));
        // 0
        System.out.println(new Q2385().amountOfTime(stringToTreeNode("[1]"), 1));
    }

    public int amountOfTime(TreeNode root, int start) {
        Map<Integer, List<Integer>> nextMap = new HashMap<>();
        walk(root, nextMap);
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        visited.add(start);
        int ans = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int cur = q.poll();
                List<Integer> nextList = nextMap.get(cur);
                for (int next : nextList) {
                    if (visited.contains(next)) continue;
                    visited.add(next);
                    q.offer(next);
                }
            }
            ans++;
        }
        return ans - 1;
    }

    void walk(TreeNode root, Map<Integer, List<Integer>> map) {
        map.putIfAbsent(root.val, new ArrayList<>());
        if (root.left != null) {
            map.putIfAbsent(root.left.val, new ArrayList<>());
            map.get(root.val).add(root.left.val);
            map.get(root.left.val).add(root.val);
            walk(root.left, map);
        }
        if (root.right != null) {
            map.putIfAbsent(root.right.val, new ArrayList<>());
            map.get(root.val).add(root.right.val);
            map.get(root.right.val).add(root.val);
            walk(root.right, map);
        }
    }
}
