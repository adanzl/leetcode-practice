package com.leo.leetcode.algorithm.q1500;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToListListInt;

/**
 * 给你一个 有向无环图 ， n 个节点编号为 0 到 n-1 ，以及一个边数组 edges ，
 * 其中 edges[i] = [from_i, to_i] 表示一条从点 from_i 到点 toi 的有向边。
 * 找到最小的点集使得从这些点出发能到达图中所有点。题目保证解存在且唯一。
 * 你可以以任意顺序返回这些节点编号。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、1 <= edges.length <= min(10^5, n * (n - 1) / 2)
 * 3、edges[i].length == 2
 * 4、0 <= from_i, to_i < n
 * 5、所有点对 (from_i, to_i) 互不相同。
 * 链接：https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes
 */
public class Q1557 {

    public static void main(String[] args) {
        // [0,3]
        System.out.println(new Q1557().findSmallestSetOfVertices(6, stringToListListInt("[[0,1],[0,2],[2,5],[3,4],[4,2]]")));
        // [0,2,3]
        System.out.println(new Q1557().findSmallestSetOfVertices(5, stringToListListInt("[[0,1],[2,1],[3,1],[1,4],[2,4]]")));
    }

    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        List<Integer> ret = new ArrayList<>();
        int[] inEdges = new int[n];
        for(List<Integer> edge: edges) {
            inEdges[edge.get(1)]++;
        }
        for(int i = 0; i < n; i++) {
            if (inEdges[i] == 0) ret.add(i);
        }

        return ret;
    }
}
