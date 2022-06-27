package com.leo.leetcode.algorithm.q6000;

import com.leo.utils.TestCase;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 存在一棵无向连通树，树中有编号从 0 到 n - 1 的 n 个节点， 以及 n - 1 条边。
 * 给你一个下标从 0 开始的整数数组 nums ，长度为 n ，其中 nums[i] 表示第 i 个节点的值。另给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中存在一条位于节点 ai 和 bi 之间的边。
 * 删除树中两条 不同 的边以形成三个连通组件。对于一种删除边方案，定义如下步骤以计算其分数：
 * 1、分别获取三个组件 每个 组件中所有节点值的异或值。
 * 2、最大 异或值和 最小 异或值的 差值 就是这一种删除边方案的分数。
 * 例如，三个组件的节点值分别是：[4,5,7]、[1,9] 和 [3,3,3] 。三个异或值分别是 4 ^ 5 ^ 7 = 6、1 ^ 9 = 8 和 3 ^ 3 ^ 3 = 3 。最大异或值是 8 ，最小异或值是 3 ，分数是 8 - 3 = 5 。
 * 返回在给定树上执行任意删除边方案可能的 最小 分数。
 * 提示：
 * 1、n1 == nums.length
 * 2、3 <= n <= 1000
 * 3、1 <= nums[i] <= 108
 * 4、edges.length == n - 1
 * 5、edges[i].length == 2
 * 6、0 <= ai, bi < n
 * 7、ai != bi
 * 8、edges 表示一棵有效的树
 * 链接：https://leetcode.cn/problems/minimum-score-after-removals-on-a-tree
 */
public class Q2322 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2322().minimumScore(stringToIntegerArray("[8,9,18,8,26,30,10]"), stringToInt2dArray("[[5,1],[4,1],[1,3],[3,6],[0,6],[0,2]] ")));
        // 1
        System.out.println(new Q2322().minimumScore(stringToIntegerArray("[15,15,16,25,28,27,27,15,3,15,17,13,20]"), stringToInt2dArray("[[9,3],[3,6],[8,9],[8,7],[11,3],[1,8],[12,8],[10,9],[4,3],[2,11],[5,12],[0,1]]")));
        // 173292
        TestCase tc = new TestCase("resources/Case001.txt");
        System.out.println(new Q2322().minimumScore(stringToIntegerArray(tc.getData(0)), stringToInt2dArray(tc.getData(1))));
        // 9
        System.out.println(new Q2322().minimumScore(stringToIntegerArray("[1,5,5,4,11]"), stringToInt2dArray("[[0,1],[1,2],[1,3],[3,4]]")));
        // 0
        System.out.println(new Q2322().minimumScore(stringToIntegerArray("[5,5,2,4,4,2]"), stringToInt2dArray("[[0,1],[1,2],[5,2],[4,3],[1,3]]")));

    }

    int minScore = Integer.MAX_VALUE;
    int order = 0;
    int[] xorValues;
    int[] parents;
    int[] in, out; // 使用dfs访问顺序判定子树的结构

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        xorValues = new int[n];
        parents = new int[n];
        in = new int[n];
        out = new int[n];
        List<List<Integer>> nextList = new ArrayList<>();
        for (int i = 0; i < n; i++) nextList.add(new ArrayList<>());
        for (int i = 0; i < n; i++) parents[i] = i;
        for (int[] edge : edges) {
            nextList.get(edge[0]).add(edge[1]);
            nextList.get(edge[1]).add(edge[0]);
        }
        System.arraycopy(nums, 0, xorValues, 0, n);
        dfs(nextList, 0, 0, 0);
        for (int i = 0; i < edges.length; i++) {
            for (int j = i + 1; j < edges.length; j++) {
                int[] edge1, edge2;
                if (Math.min(in[edges[i][0]], in[edges[i][1]]) < Math.min(in[edges[j][0]], in[edges[j][1]])) {
                    edge1 = edges[i];
                    edge2 = edges[j];
                } else {
                    edge1 = edges[j];
                    edge2 = edges[i];
                }
                int parent1, parent2, child1, child2;
                if (parents[edge1[0]] == edge1[1]) {
                    parent1 = edge1[1];
                    child1 = edge1[0];
                } else {
                    parent1 = edge1[0];
                    child1 = edge1[1];
                }
                if (parents[edge2[0]] == edge2[1]) {
                    parent2 = edge2[1];
                    child2 = edge2[0];
                } else {
                    parent2 = edge2[0];
                    child2 = edge2[1];
                }
                parents[child1] = child1;
                int xor2 = xorValues[child1];
                int xor1 = xorValues[0] ^ xor2;
                int xor3 = xorValues[child2];
                if (in[parent2] >= in[child1] && out[parent2] <= out[child1]) {
                    // 在子树上分割 xor2
                    xor2 ^= xor3;
                } else {
                    // 在父树上分割 xor1
                    xor1 ^= xor3;
                }
                int maxXor = Math.max(xor1, Math.max(xor2, xor3));
                int minXor = Math.min(xor1, Math.min(xor2, xor3));
                parents[child1] = parent1;
                minScore = Math.min(minScore, maxXor - minXor);
            }
        }
        return minScore;
    }

    int dfs(List<List<Integer>> nextList, int idx, int depth, int pre) {
        in[idx] = order++;
        for (int next : nextList.get(idx)) {
            if (next == pre) continue;
            xorValues[idx] ^= dfs(nextList, next, depth + 1, idx);
        }
        parents[idx] = pre;
        out[idx] = order;
        return xorValues[idx];
    }


}
