package com.leo.leetcode.algorithm.q2000;

import com.leo.utils.TestCase;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 城市用一个 双向连通 图表示，图中有 n 个节点，从 1 到 n 编号（包含 1 和 n）。
 * 图中的边用一个二维整数数组 edges 表示，其中每个 edges[i] = [ui, vi] 表示一条节点 ui 和节点 vi 之间的双向连通边。
 * 每组节点对由 最多一条 边连通，顶点不存在连接到自身的边。穿过任意一条边的时间是 time 分钟。
 * 每个节点都有一个交通信号灯，每 change 分钟改变一次，从绿色变成红色，再由红色变成绿色，循环往复。所有信号灯都 同时 改变。
 * 你可以在 任何时候 进入某个节点，但是 只能 在节点 信号灯是绿色时 才能离开。如果信号灯是  绿色 ，你 不能 在节点等待，必须离开。
 * 第二小的值 是 严格大于 最小值的所有值中最小的值。
 * 例如，[2, 3, 4] 中第二小的值是 3 ，而 [2, 2, 4] 中第二小的值是 4 。
 * 给你 n、edges、time 和 change ，返回从节点 1 到节点 n 需要的 第二短时间 。
 * 注意：
 * 1、你可以 任意次 穿过任意顶点，包括 1 和 n 。
 * 2、你可以假设在 启程时 ，所有信号灯刚刚变成 绿色 。
 * 提示：
 * 1、2 <= n <= 10^4
 * 2、n - 1 <= edges.length <= min(2 * 10^4, n * (n - 1) / 2)
 * 3、edges[i].length == 2
 * 4、1 <= ui, vi <= n
 * 5、ui != vi
 * 6、不含重复边
 * 7、每个节点都可以从其他节点直接或者间接到达
 * 8、1 <= time, change <= 10^3
 * <p>
 * 链接：https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination
 */

public class Q2045 {
    public static void main(String[] args) {
        TestCase tc;
        // 19983000
        tc = new TestCase("resources/Q2045/Case003.txt");
        System.out.println(new Q2045().secondMinimum(
                Integer.parseInt(tc.getData(0)),
                stringToInt2dArray(tc.getData(1)),
                Integer.parseInt(tc.getData(2)),
                Integer.parseInt(tc.getData(3))));
        // 12829
        tc = new TestCase("resources/Q2045/Case002.txt");
        System.out.println(new Q2045().secondMinimum(
                Integer.parseInt(tc.getData(0)),
                stringToInt2dArray(tc.getData(1)),
                Integer.parseInt(tc.getData(2)),
                Integer.parseInt(tc.getData(3))));
        // 15
        System.out.println(new Q2045().secondMinimum(4, stringToInt2dArray("[[1,2],[1,3],[2,4],[3,4]]"), 3, 2));
        // 11
        System.out.println(new Q2045().secondMinimum(2, stringToInt2dArray("[[1,2]]"), 3, 2));
        // 13
        System.out.println(new Q2045().secondMinimum(5, stringToInt2dArray("[[1,2],[1,3],[1,4],[3,4],[4,5]]"), 3, 5));
        // 3142
        tc = new TestCase("resources/Q2045/Case001.txt");
        System.out.println(new Q2045().secondMinimum(
                Integer.parseInt(tc.getData(0)),
                stringToInt2dArray(tc.getData(1)),
                Integer.parseInt(tc.getData(2)),
                Integer.parseInt(tc.getData(3))));

    }

    public int secondMinimum(int n, int[][] edges, int time, int change) {
        int ret = 0, first_ret = -1;
        List<List<Integer>> list = new ArrayList<>(n);
        int[] visited = new int[n];
        for (int i = 0; i < n; i++) list.add(new ArrayList<>());
        for (int[] p : edges) {
            list.get(p[0] - 1).add(p[1] - 1);
            list.get(p[1] - 1).add(p[0] - 1);
        }
        Queue<Integer> q = new ArrayDeque<>();
        q.add(0);
        while (!q.isEmpty()) {
            int size = q.size();
            Set<Integer> nextSet = new HashSet<>();
            for (int i = 0; i < size && !q.isEmpty(); i++) {
                int p = q.poll();
                if (p == n - 1) {
                    if (first_ret > 0 && first_ret != ret) return ret;
                    else first_ret = ret;
                }
                ++visited[p];
                List<Integer> next = list.get(p);
                for (int ni : next) {
                    if (visited[ni] >= 2) continue;
                    nextSet.add(ni);
                }
            }
            q.addAll(nextSet);
            int c = ret / change;
            if (c % 2 == 1) ret = change * (c + 1);
            ret += time;
        }
        return -1;
    }
}
