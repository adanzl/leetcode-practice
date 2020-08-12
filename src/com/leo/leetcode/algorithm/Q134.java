package com.leo.leetcode.algorithm;

/**
 * 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
 * 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
 * 你从其中的一个加油站出发，开始时油箱为空。
 * 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
 * 说明: 
 *  如果题目有解，该答案即为唯一答案。
 *  输入数组均为非空数组，且长度相同。
 *  输入数组中的元素均为非负数。
 * 链接：https://leetcode-cn.com/problems/gas-station
 */
public class Q134 {

    public static void main(String[] args) {
        System.out.println(new Q134().canCompleteCircuit(new int[] { 1, 2, 3, 4, 5 }, new int[] { 3, 4, 5, 1, 2 })); // 3
        System.out.println(new Q134().canCompleteCircuit(new int[] { 2, 3, 4 }, new int[] { 3, 4, 3 })); // -1
    }

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int maxOffset = 0;
        for (int start = 0; start < gas.length;) {
            if (gas[start] < cost[start]) {
                start++;
                continue;
            }
            int end = start, remain = 0;
            while (true) {
                remain += gas[end] - cost[end];
                if (remain < 0) break;
                end = (end + 1) % gas.length;
                maxOffset = Math.max(maxOffset, end);
                if (start == end) return start;
            }
            start = maxOffset + 1;
            maxOffset = Math.max(maxOffset, start);
        }
        return -1;
    }
}
