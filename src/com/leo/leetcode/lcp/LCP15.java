package com.leo.leetcode.lcp;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，其中散布着 N 个推销点，编号 0 到 N-1，不存在三点共线的情况。
 * 每两点之间有一条直线相连。游戏没有规定起点和终点，但限定了每次转角的方向。
 * 首先，小王需要先选择两个点分别作为起点和终点，然后从起点开始访问剩余 N-2 个点恰好一次并回到终点。
 * 访问的顺序需要满足一串给定的长度为 N-2 由 L 和 R 组成的字符串 direction，表示从起点出发之后在每个顶点上转角的方向。
 * 根据这个提示，小王希望你能够帮她找到一个可行的遍历顺序，输出顺序下标（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。
 * 限制：
 * 1、3 <= points.length <= 1000 且 points[i].length == 2
 * 2、1 <= points[i][0],points[i][1] <= 10000
 * 3、direction.length == points.length - 2
 * 4、direction 只包含 "L","R"
 * 链接：https://leetcode.cn/problems/you-le-yuan-de-mi-gong
 */
public class LCP15 {

    public static void main(String[] args) {
        // [0,3,1,2]
        System.out.println(Arrays.toString(new LCP15().visitOrder(stringToInt2dArray("[[1,3],[2,4],[3,3],[2,1]]"), "LR")));
        // [0,2,1,3]
        System.out.println(Arrays.toString(new LCP15().visitOrder(stringToInt2dArray("[[1,1],[1,4],[3,2],[2,1]]"), "LL")));
    }

    int[][][] vectors;

    public int[] visitOrder(int[][] points, String direction) {
        int N = points.length;
        vectors = new int[N][N][2];
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                vectors[i][j] = new int[]{points[j][0] - points[i][0], points[j][1] - points[i][1]};
                vectors[j][i] = new int[]{-vectors[i][j][0], -vectors[i][j][1]};
            }
        }
        int[] res = new int[N];
        func(new boolean[N], direction.toCharArray(), res, 0);
        return res;
    }

    boolean func(boolean[] visited, char[] dirs, int[] res, int idx) {
        if (idx == res.length) return true;
        for (int i = 0; i < visited.length; i++) {
            if (visited[i]) continue;
            if (idx > 1) {
                int[] vector1 = vectors[res[idx - 2]][res[idx - 1]], vector2 = vectors[res[idx - 1]][i];
                // v < 0 vector2 在 vector1 的右边
                int v = vector1[0] * vector2[1] - vector1[1] * vector2[0];
                if ((dirs[idx - 2] == 'L' && v <= 0) || (dirs[idx - 2] == 'R' && v >= 0)) continue;
            }
            visited[i] = true;
            res[idx] = i;
            if (func(visited, dirs, res, idx + 1)) return true;
            visited[i] = false;
        }
        return false;
    }
}
