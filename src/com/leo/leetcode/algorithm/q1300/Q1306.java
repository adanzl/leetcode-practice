package com.leo.leetcode.algorithm.q1300;

import java.util.ArrayDeque;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。
 * 请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。
 * 注意，不管是什么情况下，你都无法跳到数组之外。
 * 提示：
 * 1、1 <= arr.length <= 5 * 10^4
 * 2、0 <= arr[i] < arr.length
 * 3、0 <= start < arr.length
 * 链接：https://leetcode-cn.com/problems/jump-game-iii
 */
public class Q1306 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q1306().canReach(stringToIntegerArray("[4,2,3,0,3,1,2]"), 5));
        // true
        System.out.println(new Q1306().canReach(stringToIntegerArray("[0,1]"), 1));
        // true
        System.out.println(new Q1306().canReach(stringToIntegerArray("[4,2,3,0,3,1,2]"), 0));
        // false
        System.out.println(new Q1306().canReach(stringToIntegerArray("[3,0,2,1,2]"), 2));
        // true
        System.out.println(new Q1306().canReach(stringToIntegerArray("[0]"), 0));
        // false
        System.out.println(new Q1306().canReach(stringToIntegerArray("[]"), 0));
    }

    // bfs
    public boolean canReach(int[] arr, int start) {
        if (arr.length == 0) return false;
        int[] sign = new int[]{-1, 1};
        boolean[] visited = new boolean[arr.length];
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int idx = q.poll(), step = arr[idx];
                if (step == 0) return true;
                for (int s : sign) {
                    int next = idx + step * s;
                    if (next < 0 || next >= arr.length || visited[next]) continue;
                    visited[next] = true;
                    q.add(next);
                }
            }
        }
        return false;
    }
}
