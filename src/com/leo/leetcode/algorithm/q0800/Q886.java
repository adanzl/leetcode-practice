package com.leo.leetcode.algorithm.q0800;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
 * 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和 bi的人归入同一组。
 * 当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
 * 提示：
 * 1、1 <= n <= 2000
 * 2、0 <= dislikes.length <= 10^4
 * 3、dislikes[i].length == 2
 * 4、1 <= dislikes[i][j] <= n
 * 5、ai < bi
 * 6、dislikes 中每一组都 不同
 * 链接：https://leetcode-cn.com/problems/possible-bipartition
 */
public class Q886 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q886().possibleBiPartition(4, stringToInt2dArray("[[1,2],[1,3],[2,4]]")));
        // false
        System.out.println(new Q886().possibleBiPartition(3, stringToInt2dArray("[[1,2],[1,3],[2,3]]")));
        // false
        System.out.println(new Q886().possibleBiPartition(5, stringToInt2dArray("[[1,2],[2,3],[3,4],[4,5],[1,5]]")));
    }

    int[] groups;

    public boolean possibleBiPartition(int n, int[][] dislikes) {
        groups = new int[n];
        List<List<Integer>> nextList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            groups[i] = -1;
            nextList.add(new ArrayList<>());
        }
        for (int[] dislike : dislikes) {
            nextList.get(dislike[0] - 1).add(dislike[1] - 1);
            nextList.get(dislike[1] - 1).add(dislike[0] - 1);
        }
        for (int i = 0; i < n; i++) {
            if (groups[i] == -1 && conflict(nextList, i, 0))
                return false;
        }
        return true;
    }

    boolean conflict(List<List<Integer>> nextList, int idx, int group) {
        if (groups[idx] != -1) return groups[idx] != group;
        groups[idx] = group;
        List<Integer> nextArr = nextList.get(idx);
        for (int next : nextArr) {
            if (conflict(nextList, next, group == 0 ? 1 : 0))
                return true;
        }
        return false;
    }
}
