package com.leo.leetcode.algorithm.q1000;

import java.util.PriorityQueue;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 有一堆石头，每块石头的重量都是正整数。
 * 每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
 * 如果 x == y，那么两块石头都会被完全粉碎；
 * 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
 * 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
 * <p>
 * 链接：https://leetcode-cn.com/problems/last-stone-weight
 */

public class Q1046 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q1046().lastStoneWeight(stringToIntegerArray("[2,7,4,1,8,1]")));
    }

    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int stone : stones) {
            pq.offer(stone);
        }

        while (pq.size() > 1) {
            int a = pq.poll(), b = pq.poll();
            if (a > b) pq.offer(a - b);
        }
        return pq.isEmpty() ? 0 : pq.poll();
    }
}
