package com.leo.leetcode.algorithm.q6000;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 n 个节点的 无向图 ，节点编号为 0 到 n - 1 。
 * 给你一个下标从 0 开始的整数数组 scores ，其中 scores[i] 是第 i 个节点的分数。
 * 同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 之间有一条 无向 边。
 * 一个合法的节点序列如果满足以下条件，我们称它是 合法的 ：
 * 1、序列中每 相邻 节点之间有边相连。
 * 2、序列中没有节点出现超过一次。
 * 节点序列的分数定义为序列中节点分数之 和 。
 * 请你返回一个长度为 4 的合法节点序列的最大分数。如果不存在这样的序列，请你返回 -1 。
 * 提示：
 * 1、n == scores.length
 * 2、4 <= n <= 5 * 10^4
 * 3、1 <= scores[i] <= 10^8
 * 4、0 <= edges.length <= 5 * 10^4
 * 5、edges[i].length == 2
 * 6、0 <= ai, bi <= n - 1
 * 7、ai != bi
 * 8、不会有重边。
 * 链接：https://leetcode-cn.com/problems/maximum-score-of-a-node-sequence
 */
public class Q2242 {

    public static void main(String[] args) {
        // 83
        System.out.println(new Q2242().maximumScore(stringToIntegerArray("[16,21,22,2,24,21,12,17,2,24]")
                , stringToInt2dArray("[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,0]]")));
        // 24
        System.out.println(new Q2242().maximumScore(stringToIntegerArray("[5,2,9,8,4]"), stringToInt2dArray("[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]")));
        // -1
        System.out.println(new Q2242().maximumScore(stringToIntegerArray("[9,20,6,4,11,12]"), stringToInt2dArray("[[0,3],[5,3],[2,4],[1,3]]")));
    }

    public int maximumScore(int[] scores, int[][] edges) {
        int max = -1;
        List<List<Integer>> nextList = new ArrayList<>();
        for (int i = 0; i < scores.length; i++) nextList.add(new ArrayList<>());
        for (int[] edge : edges) {
            nextList.get(edge[0]).add(edge[1]);
            nextList.get(edge[1]).add(edge[0]);
        }
        // 关键性的去掉了多余的节点
        for (int i = 0; i < scores.length; i++) {
            List<Integer> nList = nextList.get(i);
            if (nList.size() > 3) {
                nList.sort((a, b) -> (scores[b] - scores[a]));
                nextList.set(i, new ArrayList<>(nList.subList(0, 3)));
            }
        }
        for (int[] edge : edges) {
            int score = scores[edge[0]] + scores[edge[1]];
            for (int nodeLeft : nextList.get(edge[0])) {
                if (nodeLeft == edge[1]) continue;
                for (int nodeRight : nextList.get(edge[1])) {
                    if (nodeRight == edge[0] || nodeRight == nodeLeft) continue;
                    int newScore = score + scores[nodeLeft] + scores[nodeRight];
                    max = Math.max(max, newScore);
                }
            }
        }
        return max;
    }

}
