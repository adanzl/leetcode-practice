package com.leo.leetcode.lcp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 又到了一年一度的春游时间，小吴计划去游乐场游玩 1 天，游乐场总共有 N 个游乐项目，编号从 0 到 N-1。
 * 小吴给每个游乐项目定义了一个非负整数值 value[i] 表示自己的喜爱值。
 * 两个游乐项目之间会有双向路径相连，整个游乐场总共有 M 条双向路径，保存在二维数组 edges中。 小吴计划选择一个游乐项目 A 作为这一天游玩的重点项目。
 * 上午小吴准备游玩重点项目 A 以及与项目 A 相邻的两个项目 B、C （项目A、B与C要求是不同的项目，且项目B与项目C要求相邻），并返回 A ，即存在一条 A-B-C-A 的路径。
 * 下午，小吴决定再游玩重点项目 A以及与A相邻的两个项目 B'、C'，（项目A、B'与C'要求是不同的项目，且项目B'与项目C'要求相邻），并返回 A ，即存在一条 A-B'-C'-A 的路径。
 * 下午游玩项目 B'、C' 可与上午游玩项目B、C存在重复项目。 小吴希望提前安排好游玩路径，使得喜爱值之和最大。
 * 请你返回满足游玩路径选取条件的最大喜爱值之和，如果没有这样的路径，返回 0。 注意：一天中重复游玩同一个项目并不能重复增加喜爱值了。
 * 例如：上下午游玩路径分别是 A-B-C-A与A-C-D-A 那么只能获得 value[A] + value[B] + value[C] + value[D] 的总和。
 * 限制：
 * 1、3 <= value.length <= 10000
 * 2、1 <= edges.length <= 10000
 * 3、0 <= edges[i][0],edges[i][1] < value.length
 * 4、0 <= value[i] <= 10000
 * 5、edges中没有重复的边
 * 6、edges[i][0] != edges[i][1]
 * 链接：https://leetcode.cn/problems/you-le-yuan-de-you-lan-ji-hua
 */
public class LCP16 {

    public static void main(String[] args) {
        // 6
        System.out.println(new LCP16().maxWeight(stringToInt2dArray("[[0,1],[1,2],[0,2]]"), stringToIntegerArray("[1,2,3]")));
        // 0
        System.out.println(new LCP16().maxWeight(stringToInt2dArray("[[0,2],[2,1]]"), stringToIntegerArray("[1,2,5]")));
        // 39
        System.out.println(new LCP16().maxWeight(stringToInt2dArray("[[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]]"), stringToIntegerArray("[7,8,6,8,9,7]")));
    }

    // https://leetcode.cn/problems/you-le-yuan-de-you-lan-ji-hua/solution/tu-jie-si-lu-xiang-xi-zheng-ming-by-newhar/
    public int maxWeight(int[][] edges, int[] value) {
        int N = value.length, M = edges.length;
        int[] cntArr = new int[N];

        // 对边按权值和排序，以便之后对每个点，直接获得按权值和排序的边
        Arrays.sort(edges, (o1, o2) -> value[o1[0]] + value[o1[1]] - value[o2[0]] - value[o2[1]]);
        // 统计各个点的度数（出边数量）
        for (int[] edge : edges) {
            ++cntArr[edge[0]];
            ++cntArr[edge[1]];
        }
        // 将无向图重建为有向图
        List<List<int[]>> G = new ArrayList<>(N);
        for (int i = 0; i < N; i++) G.add(new ArrayList<>());
        for (int i = 0; i < M; ++i) {
            if (cntArr[edges[i][0]] < cntArr[edges[i][1]] || (cntArr[edges[i][0]] == cntArr[edges[i][1]] && edges[i][0] < edges[i][1]))
                G.get(edges[i][0]).add(new int[]{edges[i][1], i});
            else
                G.get(edges[i][1]).add(new int[]{edges[i][0], i});
        }

        // 求所有的三元环，并按边归类
        List<List<Integer>> nodes = new ArrayList<>();
        int[] vis = new int[N], ids = new int[N];
        for (int i = 0; i < M; i++) nodes.add(new ArrayList<>());
        Arrays.fill(vis, 0xff);
        for (int i = 0; i < M; ++i) {
            for (int[] ne : G.get(edges[i][0])) {
                vis[ne[0]] = i;
                ids[ne[0]] = ne[1];
            }
            for (int[] ne : G.get(edges[i][1])) {
                if (vis[ne[0]] == i) {
                    nodes.get(ne[1]).add(edges[i][0]);
                    nodes.get(ids[ne[0]]).add(edges[i][1]);
                    nodes.get(i).add(ne[0]);
                }
            }
        }
        // 将三元环按顶点归类，每个顶点自动获得按权值和排序的边
        List<List<Integer>> C = new ArrayList<>();
        for (int i = 0; i < N; i++) C.add(new ArrayList<>());
        for (int i = 0; i < M; ++i)
            for (int n : nodes.get(i)) C.get(n).add(i);
        // 求出结果
        int res = 0;
        for (int i = 0; i < N; ++i) {
            int bound = C.get(i).size() - 1;
            for (int a = 0; a < Math.min(3, C.get(i).size()) && bound >= a; ++a) {
                for (int b = a; b <= bound; ++b) {
                    int cur = value[i] + value[edges[C.get(i).get(a)][0]] + value[edges[C.get(i).get(a)][1]], cnt = 0;
                    if (edges[C.get(i).get(b)][0] != edges[C.get(i).get(a)][0] && edges[C.get(i).get(b)][0] != edges[C.get(i).get(a)][1]) {
                        cur += value[edges[C.get(i).get(b)][0]];
                        ++cnt;
                    }
                    if (edges[C.get(i).get(b)][1] != edges[C.get(i).get(a)][0] && edges[C.get(i).get(b)][1] != edges[C.get(i).get(a)][1]) {
                        cur += value[edges[C.get(i).get(b)][1]];
                        ++cnt;
                    }
                    res = Math.max(res, cur);
                    if (cnt == 2) {
                        bound = b - 1;
                        break;
                    }
                }
            }
        }
        return res;
    }
}
