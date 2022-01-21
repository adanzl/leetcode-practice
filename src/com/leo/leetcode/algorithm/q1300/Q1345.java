package com.leo.leetcode.algorithm.q1300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
 * 每一步，你可以从下标 i 跳到下标：
 * 1、i + 1 满足：i + 1 < arr.length
 * 2、i - 1 满足：i - 1 >= 0
 * 3、j 满足：arr[i] == arr[j] 且 i != j
 * 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
 * 注意：任何时候你都不能跳到数组外面。
 * <p>
 * 提示：
 * 1、1 <= arr.length <= 5 * 10^4
 * 2、-10^8 <= arr[i] <= 10^8
 * 链接：https://leetcode-cn.com/problems/jump-game-iv
 */

public class Q1345 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1345().minJumps(stringToIntegerArray("[100,-23,-23,404,100,23,23,23,3,404]")));
        // 0
        System.out.println(new Q1345().minJumps(stringToIntegerArray("[7]")));
        // 1
        System.out.println(new Q1345().minJumps(stringToIntegerArray("[7,6,9,6,9,6,9,7]")));
        // 2
        System.out.println(new Q1345().minJumps(stringToIntegerArray("[6,1,9]")));
        // 3
        System.out.println(new Q1345().minJumps(stringToIntegerArray("[11,22,7,7,7,7,7,7,7,22,13]")));
        // 3
        System.out.println(new Q1345().minJumps(stringToIntegerArray("[100,-23,-23,404,100,23,23,23,3,404]")));
    }

    public int minJumps(int[] arr) {
        if (arr.length < 2) return 0;
        boolean[] visited = new boolean[arr.length];
        int step = 0;
        Map<Integer, List<Integer>> vMap = new HashMap<>();
        Queue<Integer> q = new ArrayDeque<>();
        q.add(0);
        visited[0] = true;
        for (int i = 0; i < arr.length; i++) {
            vMap.putIfAbsent(arr[i], new ArrayList<>());
            vMap.get(arr[i]).add(i);
        }
        while (step < arr.length) {
            int size = q.size();
            for (int j = 0; j < size && !q.isEmpty(); j++) {
                int idx = q.poll();
                if (idx == arr.length - 1) return step;
                List<Integer> nextList = vMap.getOrDefault(arr[idx], new ArrayList<>());
                if (idx > 0) nextList.add(idx - 1);
                if (idx < arr.length - 1) nextList.add(idx + 1);
                for (int v : nextList) {
                    if (!visited[v]) {
                        q.add(v);
                        visited[v] = true;
                    }
                }
                vMap.remove(arr[idx]);
            }
            step++;
        }
        return -1;
    }
}
