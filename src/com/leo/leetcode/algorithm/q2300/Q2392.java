package com.leo.leetcode.algorithm.q2300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 正 整数 k ，同时给你：
 * 1、一个大小为 n 的二维整数数组 rowConditions ，其中 rowConditions[i] = [above_i, below_i] 和
 * 2、一个大小为 m 的二维整数数组 colConditions ，其中 colConditions[i] = [left_i, right_i] 。
 * 两个数组里的整数都是 1 到 k 之间的数字。
 * 你需要构造一个 k x k 的矩阵，1 到 k 每个数字需要 恰好出现一次 。剩余的数字都是 0 。
 * 矩阵还需要满足以下条件：
 * 1、对于所有 0 到 n - 1 之间的下标 i ，数字 above_i 所在的 行 必须在数字 below_i 所在行的上面。
 * 2、对于所有 0 到 m - 1 之间的下标 i ，数字 left_i 所在的 列 必须在数字 right_i 所在列的左边。
 * 返回满足上述要求的 任意 矩阵。如果不存在答案，返回一个空的矩阵。
 * 提示：
 * 1、2 <= k <= 400
 * 2、1 <= rowConditions.length, colConditions.length <= 104
 * 3、rowConditions[i].length == colConditions[i].length == 2
 * 4、1 <= above_i, below_i, left_i, right_i <= k
 * 5、above_i != below_i
 * 6、left_i != right_i
 * 链接：https://leetcode.cn/problems/build-a-matrix-with-conditions
 */
public class Q2392 {

    public static void main(String[] args) {
        //
        System.out.println(Arrays.deepToString(new Q2392().buildMatrix(8, stringToInt2dArray("[[1,2],[7,3],[4,3],[5,8],[7,8],[8,2],[5,8],[3,2],[1,3],[7,6],[4,3],[7,4],[4,8],[7,3],[7,5]]"), stringToInt2dArray("[[5,7],[2,7],[4,3],[6,7],[4,3],[2,3],[6,2]]"))));
        // [[3,0,0],[0,0,1],[0,2,0]] || [[0, 0, 1], [3, 0, 0], [0, 2, 0]]
        System.out.println(Arrays.deepToString(new Q2392().buildMatrix(3, stringToInt2dArray("[[1,2],[3,2]]"), stringToInt2dArray("[[2,1],[3,2]]"))));
        // []
        System.out.println(Arrays.deepToString(new Q2392().buildMatrix(3, stringToInt2dArray("[[1,2],[2,3],[3,1],[2,3]]"), stringToInt2dArray("[[2,1]]"))));
    }

    public int[][] buildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        List<Integer> rOrder = getOrder(k, rowConditions), cOrder = getOrder(k, colConditions);
        if (rOrder.size() < k || cOrder.size() < k) return new int[][]{};
        int[][] ans = new int[k][k];
        int[] iRow = new int[k];
        for (int i = 0; i < k; i++) iRow[rOrder.get(i)] = i;
        for (int i = 0; i < k; i++) {
            int num = cOrder.get(i);
            ans[iRow[num]][i] = num + 1;
        }
        return ans;
    }

    // 拓扑序列
    List<Integer> getOrder(int n, int[][] conditions) {
        List<List<Integer>> nextList = new ArrayList<>();
        List<Integer> ret = new ArrayList<>();
        int[] nPre = new int[n];
        for (int i = 0; i < n; i++) nextList.add(new ArrayList<>());
        for (int[] condition : conditions) {
            int x = condition[0] - 1, y = condition[1] - 1; // 此处调整下标 0-1
            nextList.get(x).add(y);
            nPre[y]++;
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (nPre[i] == 0) q.add(i);
        while (!q.isEmpty()) {
            int cur = q.poll();
            ret.add(cur);
            for (int next : nextList.get(cur)) {
                --nPre[next];
                if (nPre[next] == 0) q.add(next);
            }
        }
        return ret;
    }
}
