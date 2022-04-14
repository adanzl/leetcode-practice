package com.leo.leetcode.algorithm.q1500;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。
 * 在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1 。
 * 给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的 1 。
 * 返回存在长度 恰好 为 m 的 一组 1 的最后步骤。如果不存在这样的步骤，请返回 -1 。
 * 提示：
 * 1、n == arr.length
 * 2、1 <= n <= 10^5
 * 3、1 <= arr[i] <= n
 * 4、arr 中的所有整数 互不相同
 * 5、1 <= m <= arr.length
 * 链接：https://leetcode-cn.com/problems/find-latest-group-of-size-m
 */
public class Q1562 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q1562().findLatestStep(stringToIntegerArray("[4,3,2,1]"), 1));
        // 4
        System.out.println(new Q1562().findLatestStep(stringToIntegerArray("[3,5,1,2,4]"), 1));
        // 1
        System.out.println(new Q1562().findLatestStep(stringToIntegerArray("[1]"), 1));
        // -1
        System.out.println(new Q1562().findLatestStep(stringToIntegerArray("[3,1,5,4,2]"), 2));
        // 5
        System.out.println(new Q1562().findLatestStep(stringToIntegerArray("[3,1,5,4,2]"), 5));
        // 2
        System.out.println(new Q1562().findLatestStep(stringToIntegerArray("[2,1]"), 2));
    }

    public int findLatestStep(int[] arr, int m) {
        int n = arr.length, ret = -1;
        int[] parent = new int[n], len = new int[n];
        Set<Integer> set = new HashSet<>();
        for (int num : arr) parent[num - 1] = num - 1;
        for (int i = 0; i < n; i++) {
            len[arr[i] - 1] = 1;
            if (len[arr[i] - 1] == m) set.add(arr[i] - 1);
            if (arr[i] > 1 && len[arr[i] - 2] > 0) merge(parent, len, set, arr[i] - 1, arr[i] - 2, m);
            if (arr[i] < n && len[arr[i]] > 0) merge(parent, len, set, arr[i] - 1, arr[i], m);
            if (!set.isEmpty()) ret = i + 1;
        }
        return ret;
    }

    int find(int[] parent, int x) {
        return parent[x] == x ? x : (parent[x] = find(parent, parent[x]));
    }

    void merge(int[] parent, int[] len, Set<Integer> set, int x0, int x1, int m) {
        int p0 = find(parent, x0), p1 = find(parent, x1);
        if (len[p1] == m) set.remove(p1);
        if (len[p0] == m) set.remove(p0);
        if (p0 != p1) {
            parent[p0] = p1;
            len[p1] += len[p0];
        }
        if (len[p1] == m) set.add(p1);
    }
}
