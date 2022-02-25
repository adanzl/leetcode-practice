package com.leo.leetcode.algorithm.q1600;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有一条双向道路。
 * 两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。
 * 整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。
 * 给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 。
 * 提示：
 * 1、2 <= n <= 100
 * 2、0 <= roads.length <= n * (n - 1) / 2
 * 3、roads[i].length == 2
 * 4、0 <= ai, bi <= n-1
 * 5、ai != bi
 * 6、每对城市之间 最多只有一条 道路相连
 * 链接：https://leetcode-cn.com/problems/maximal-network-rank
 */
public class Q1615 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q1615().maximalNetworkRank(8, stringToInt2dArray("[[0,1],[0,3],[0,2],[1,2],[1,4],[2,4],[3,4]]")));
        // 4
        System.out.println(new Q1615().maximalNetworkRank(4, stringToInt2dArray("[[0,1],[0,3],[1,2],[1,3]]")));
        // 5
        System.out.println(new Q1615().maximalNetworkRank(5, stringToInt2dArray("[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]")));
        // 5
        System.out.println(new Q1615().maximalNetworkRank(8, stringToInt2dArray("[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]")));
    }

    public int maximalNetworkRank(int n, int[][] roads) {
        List<int[]> counts = new ArrayList<>();
        boolean[][] map = new boolean[n][n];
        int ret = 0;
        for (int i = 0; i < n; i++) counts.add(new int[]{i, 0});
        for (int[] road : roads) {
            counts.get(road[0])[1]++;
            counts.get(road[1])[1]++;
            map[road[0]][road[1]] = true;
            map[road[1]][road[0]] = true;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int[] p0 = counts.get(i), p1 = counts.get(j);
                ret = Math.max(ret, p0[1] + p1[1] - (map[p0[0]][p1[0]] ? 1 : 0));
            }
        }
        return ret;
    }
}
