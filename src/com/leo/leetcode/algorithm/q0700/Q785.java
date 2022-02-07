package com.leo.leetcode.algorithm.q0700;

import com.leo.utils.LCUtil;
import com.leo.utils.TestCase;

/**
 * 给定一个无向图graph，当这个图为二分图时返回true。
 * 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
 * graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。
 * 每个节点都是一个在0到graph.length-1之间的整数。
 * 这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。
 * 注意:
 * graph 的长度范围为 [1, 100]。
 * graph[i] 中的元素的范围为 [0, graph.length - 1]。
 * graph[i] 不会包含 i 或者有重复的值。
 * 图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
 * 链接：https://leetcode-cn.com/problems/is-graph-bipartite
 */
public class Q785 {
    public static void main(String[] args) {
        final TestCase tc1 = new TestCase("resources/Q785/Case88235646");
        System.out.println(new Q785().isBipartite(LCUtil.stringToInt2dArray(tc1.getData(0)))); // true
        System.out.println(new Q785().isBipartite(LCUtil.stringToInt2dArray("[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]"))); // false
        System.out.println(new Q785().isBipartite(LCUtil.stringToInt2dArray("[[1,3], [0,2], [1,3], [0,2]]"))); // true
        System.out.println(new Q785().isBipartite(LCUtil.stringToInt2dArray("[[1,2,3], [0,2], [0,1,3], [0,2]]"))); // false
        System.out.println(new Q785().isBipartite(LCUtil.stringToInt2dArray("[[1,2,3], [0,2], [0,1,3], [0,2]]"))); // false
    }

    public boolean isBipartite(int[][] graph) {
        int[] mark = new int[graph.length];
        mark[0] = 1;
        return fit(mark, graph, 0);
    }

    boolean fit(int[] mark, int[][] graph, int index) {
        for (int i = index; i < mark.length; i++) {
            int flag = mark[i];
            for (int v : graph[i]) {
                if (mark[v] == 0) {
                    mark[v] = flag == 1 ? 2 : 1;
                    if (fit(mark, graph, v)) return true;
                    mark[v] = flag == 1 ? 1 : 2;
                    if (fit(mark, graph, v)) return true;
                    mark[v] = 0;
                    return false;
                } else if (mark[v] == flag) {
                    return false;
                }
            }
        }
        return true;
    }
}
