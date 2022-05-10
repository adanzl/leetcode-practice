package com.leo.leetcode.lcp;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：
 * 1、有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
 * 2、每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
 * 3、每轮信息必须需要传递给另一个人，且信息可重复经过同一个人
 * 给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。返回信息从小 A (编号 0 ) 经过 k 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。
 * 限制：
 * 1、2 <= n <= 10
 * 2、1 <= k <= 5
 * 3、1 <= relation.length <= 90, 且 relation[i].length == 2
 * 4、0 <= relation[i][0],relation[i][1] < n 且 relation[i][0] != relation[i][1]
 * 链接：https://leetcode.cn/problems/chuan-di-xin-xi
 */
public class LCP07 {

    public static void main(String[] args) {
        // 0
        System.out.println(new LCP07().numWays(3, stringToInt2dArray("[[0,2],[2,1]]"), 2));
        // 3
        System.out.println(new LCP07().numWays(5, stringToInt2dArray("[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]"), 3));
    }

    public int numWays(int n, int[][] relation, int k) {
        int ret = 0;
        List<List<Integer>> nextList = new ArrayList<>();
        for (int i = 0; i < n; i++) nextList.add(new ArrayList<>());
        for (int[] r : relation) nextList.get(r[0]).add(r[1]);
        Queue<Integer> q = new ArrayDeque<>();
        q.add(0);
        while (!q.isEmpty() && k-- > 0) {
            int size = q.size();
            for (int i = 0; i < size && !q.isEmpty(); i++) {
                q.addAll(nextList.get(q.poll()));
            }
        }
        for (int p : q) if (p == n - 1) ret++;
        return ret;
    }
}
