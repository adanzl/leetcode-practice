package com.leo.leetcode.algorithm.q0600;

import java.util.*;

import static com.leo.utils.LCUtil.stringToListListInt;

/**
 * 你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：
 * 1、0 表示障碍，无法触碰
 * 2.1 表示地面，可以行走
 * 3、比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
 * 每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
 * 你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。
 * 你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
 * 可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。
 * 提示：
 * 1、m == forest.length
 * 2、n == forest[i].length
 * 3、1 <= m, n <= 50
 * 4、0 <= forest[i][j] <= 10^9
 * 链接：https://leetcode.cn/problems/cut-off-trees-for-golf-event
 */
public class Q675 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q675().cutOffTree(stringToListListInt("[[2,3,4],[0,0,5],[8,7,6]]")));
        // -1
        System.out.println(new Q675().cutOffTree(stringToListListInt("[[1,2,3],[0,0,0],[7,6,5]]")));
        // 12
        System.out.println(new Q675().cutOffTree(stringToListListInt("[[8,2,3],[0,0,4],[7,6,5]]")));
        // 6
        System.out.println(new Q675().cutOffTree(stringToListListInt("[[1,2,3],[0,0,4],[7,6,5]]")));
    }

    public int cutOffTree(List<List<Integer>> forest) {
        int m = forest.size(), n = forest.get(0).size(), ret = 0, N = m * n;
        List<List<Integer>> nextVertex = new ArrayList<>();
        int[] preNode = new int[]{0, 0, 0};
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        for (int i = 0; i < N; i++) nextVertex.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int v = forest.get(i).get(j);
                if (v < 1) continue;
                if (v > 1) pq.offer(new int[]{v, i, j});
                if (i > 0 && forest.get(i - 1).get(j) > 0) {
                    nextVertex.get(i * n + j).add((i - 1) * n + j);
                    nextVertex.get((i - 1) * n + j).add(i * n + j);
                }
                if (j > 0 && forest.get(i).get(j - 1) > 0) {
                    nextVertex.get(i * n + j).add(i * n + j - 1);
                    nextVertex.get(i * n + j - 1).add(i * n + j);
                }
                if (i < m - 1 && forest.get(i + 1).get(j) > 0) {
                    nextVertex.get(i * n + j).add((i + 1) * n + j);
                    nextVertex.get((i + 1) * n + j).add(i * n + j);
                }
                if (j < n - 1 && forest.get(i).get(j + 1) > 0) {
                    nextVertex.get(i * n + j).add(i * n + j + 1);
                    nextVertex.get(i * n + j + 1).add(i * n + j);
                }
            }
        }

        while (!pq.isEmpty()) {
            int[] curNode = pq.poll();
            int src = preNode[1] * n + preNode[2], dst = curNode[1] * n + curNode[2];
            long dis = getDistance(src, dst, nextVertex);
            if (dis > N) return -1;
            ret += dis;
            preNode = curNode;
        }

        return ret;
    }

    int getDistance(int src, int dst, List<List<Integer>> nextVertex) {
        if (src == dst) return 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(src);
        boolean[] visited = new boolean[nextVertex.size()];
        int ret = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0 && !queue.isEmpty()) {
                int cur = queue.poll();
                for (int next : nextVertex.get(cur)) {
                    if (next == dst) return ret + 1;
                    if (visited[next]) continue;
                    visited[next] = true;
                    queue.offer(next);
                }
            }
            ret++;
        }
        return Integer.MAX_VALUE;
    }
}
