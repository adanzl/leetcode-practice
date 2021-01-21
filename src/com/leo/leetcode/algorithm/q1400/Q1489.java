package com.leo.leetcode.algorithm.q1400;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，
 * 其中 edges[i] = [from_i, to_i, weight_i] 表示在 from_i 和 to_i 节点之间有一条带权无向边。
 * 最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。
 * 请你找到给定图中最小生成树的所有关键边和伪关键边。
 * 如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。
 * 伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
 * 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。
 * 提示：
 * 1、2 <= n <= 100
 * 2、1 <= edges.length <= min(200, n * (n - 1) / 2)
 * 3、edges[i].length == 3
 * 4、0 <= from_i < to_i < n
 * 5、1 <= weight_i <= 1000
 * 6、所有 (from_i, to_i) 数对都是互不相同的。
 * <p>
 * 链接：https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
 */
public class Q1489 {

    public static void main(String[] args) {
        // [[0,2,3,5],[1,4]]
        System.out.println(new Q1489().findCriticalAndPseudoCriticalEdges(6, stringToInt2dArray("[[0,1,2],[0,2,5],[2,3,5],[1,4,4],[2,5,5],[4,5,2]]")));
        // [[3],[0,1,2,4,5,6]]
        System.out.println(new Q1489().findCriticalAndPseudoCriticalEdges(6, stringToInt2dArray("[[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]")));
        // [[0,1],[2,3,4,5]]
        System.out.println(new Q1489().findCriticalAndPseudoCriticalEdges(5, stringToInt2dArray("[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]")));
        // [[],[0,1,2,3]]
        System.out.println(new Q1489().findCriticalAndPseudoCriticalEdges(4, stringToInt2dArray("[[0,1,1],[1,2,1],[2,3,1],[0,3,1]]")));
    }

    int[] parent;
    int[] edgeMask;
    int nGroup;

    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        List<Integer> keyEdges = new ArrayList<>(), notKeyEdges = new ArrayList<>();
        List<List<Integer>> ret = new ArrayList<>(2);
        ret.add(keyEdges);
        ret.add(notKeyEdges);
        int[][] eData = new int[edges.length][4];
        for (int i = 0; i < edges.length; i++) {
            eData[i][0] = edges[i][0];
            eData[i][1] = edges[i][1];
            eData[i][2] = edges[i][2];
            eData[i][3] = i;
        }
        Arrays.sort(eData, Comparator.comparingInt(o -> o[2]));
        parent = new int[n];
        edgeMask = new int[eData.length];
        reset();
        int weight = buildTree(eData);
        for (int i = 0; i < edgeMask.length; i++) {
            reset();
            edgeMask[i] = 2;
            int nWeight = buildTree(eData);
            if (nWeight > weight || nWeight < 0) {
                keyEdges.add(eData[i][3]);
            } else if (weight == nWeight) {
                reset();
                nWeight = eData[i][2];
                merge(eData[i][0], eData[i][1]);
                nWeight += buildTree(eData);
                if (nWeight == weight) notKeyEdges.add(eData[i][3]);
            }
        }
        return ret;
    }

    void reset() {
        for (int i = 0; i < parent.length; i++) parent[i] = i;
        Arrays.fill(edgeMask, 0);
        nGroup = parent.length;
    }

    int buildTree(int[][] edges) {
        int weight = 0;
        for (int i = 0; i < edges.length; i++) {
            if (edgeMask[i] != 0) continue;
            int[] edge = edges[i];
            if (find(edge[0]) != find(edge[1])) {
                weight += edge[2];
                merge(edge[0], edge[1]);
            }
            edgeMask[i] = 1;
        }
        return nGroup == 1 ? weight : -1;
    }

    void merge(int i_0, int i_1) {
        int r_0 = find(i_0), r_1 = find(i_1);
        if (r_0 != r_1) {
            parent[r_1] = r_0;
            --nGroup;
        }
    }

    int find(int x) {
        return parent[x] == x ? parent[x] : (parent[x] = find(parent[x]));
    }
}
