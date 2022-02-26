package com.leo.leetcode.algorithm.q1000;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。
 * 在每个花园中，你打算种下四种花之一。
 * 另外，所有花园 最多 有 3 条路径可以进入或离开.
 * 你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
 * 以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1、2、3、4 表示。保证存在答案。
 * 提示：
 * 1、1 <= n <= 10^4
 * 2、0 <= paths.length <= 2 * 10^4
 * 3、paths[i].length == 2
 * 4、1 <= xi, yi <= n
 * 5、xi != yi
 * 每个花园 最多 有 3 条路径可以进入或离开
 * 链接：https://leetcode-cn.com/problems/flower-planting-with-no-adjacent
 */
public class Q1042 {

    public static void main(String[] args) {
        // [1,2,3]
        System.out.println(Arrays.toString(new Q1042().gardenNoAdj(3, stringToInt2dArray("[[1,2],[2,3],[3,1]]"))));
        // [1,2,1,2]
        System.out.println(Arrays.toString(new Q1042().gardenNoAdj(4, stringToInt2dArray("[[1,2],[3,4]]"))));
        // [1,2,3,4]
        System.out.println(Arrays.toString(new Q1042().gardenNoAdj(4, stringToInt2dArray("[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]"))));
    }

    public int[] gardenNoAdj(int n, int[][] paths) {
        int[] ret = new int[n];
        List<List<Integer>> neighbors = new ArrayList<>(n);
        for (int i = 0; i < n; i++) neighbors.add(new ArrayList<>());
        for (int[] path : paths) {
            neighbors.get(path[0] - 1).add(path[1] - 1);
            neighbors.get(path[1] - 1).add(path[0] - 1);
        }
        List<Integer> colors = Arrays.asList(1, 2, 3, 4);
        for (int i = 0; i < n; i++) {
            Set<Integer> color = new HashSet<>(colors);
            List<Integer> neighbor = neighbors.get(i);
            for (int near : neighbor) color.remove(ret[near]);
            if (!color.isEmpty()) ret[i] = color.stream().findFirst().get();
        }
        return ret;
    }
}
