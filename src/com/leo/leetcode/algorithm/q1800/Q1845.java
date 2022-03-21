package com.leo.leetcode.algorithm.q1800;

import java.util.PriorityQueue;

/**
 * 请你设计一个管理 n 个座位预约的系统，座位编号从 1 到 n 。
 * 请你实现 SeatManager 类：
 * 1、SeatManager(int n) 初始化一个 SeatManager 对象，它管理从 1 到 n 编号的 n 个座位。所有座位初始都是可预约的。
 * 2、int reserve() 返回可以预约座位的 最小编号 ，此座位变为不可预约。
 * 3、void unreserve(int seatNumber) 将给定编号 seatNumber 对应的座位变成可以预约。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= seatNumber <= n
 * 3、每一次对 reserve 的调用，题目保证至少存在一个可以预约的座位。
 * 4、每一次对 unreserve 的调用，题目保证 seatNumber 在调用函数前都是被预约状态。
 * 5、对 reserve 和 unreserve 的调用 总共 不超过 10^5 次。
 * 链接：https://leetcode-cn.com/problems/seat-reservation-manager
 */
public class Q1845 {

    public static void main(String[] args) {
        SeatManager seatManager = new SeatManager(5); // 初始化 SeatManager ，有 5 个座位。
        System.out.println(seatManager.reserve());    // 所有座位都可以预约，所以返回最小编号的座位，也就是 1 。
        System.out.println(seatManager.reserve());    // 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
        seatManager.unreserve(2); // 将座位 2 变为可以预约，现在可预约的座位为 [2,3,4,5] 。
        System.out.println(seatManager.reserve());    // 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
        System.out.println(seatManager.reserve());    // 可以预约的座位为 [3,4,5] ，返回最小编号的座位，也就是 3 。
        System.out.println(seatManager.reserve());    // 可以预约的座位为 [4,5] ，返回最小编号的座位，也就是 4 。
        System.out.println(seatManager.reserve());    // 唯一可以预约的是座位 5 ，所以返回 5 。
        seatManager.unreserve(5); // 将座位 5 变为可以预约，现在可预约的座位为 [5] 。
    }

    static class SeatManager {
        private PriorityQueue<Integer> q;

        public SeatManager(int n) {
            q = new PriorityQueue<>();
            for (int i = 0; i < n; i++) q.offer(i + 1);
        }

        public int reserve() {
            return q.isEmpty() ? -1 : q.poll();
        }

        public void unreserve(int seatNumber) {
            q.offer(seatNumber);
        }
    }
}
