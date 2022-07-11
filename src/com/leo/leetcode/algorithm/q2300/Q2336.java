package com.leo.leetcode.algorithm.q2300;

import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

/**
 * 现有一个包含所有正整数的集合 [1, 2, 3, 4, 5, ...] 。
 * 实现 SmallestInfiniteSet 类：
 * 1、SmallestInfiniteSet() 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。
 * 2、int popSmallest() 移除 并返回该无限集中的最小整数。
 * 3、void addBack(int num) 如果正整数 num 不 存在于无限集中，则将一个 num 添加 到该无限集中。
 * 提示：
 * 1、1 <= num <= 1000
 * 2、最多调用 popSmallest 和 addBack 方法 共计 1000 次
 * 链接：https://leetcode.cn/problems/smallest-number-in-infinite-set
 */
public class Q2336 {

    public static void main(String[] args) {
        SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
        smallestInfiniteSet.addBack(2);    // 2 已经在集合中，所以不做任何变更。
        System.out.println(smallestInfiniteSet.popSmallest()); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
        System.out.println(smallestInfiniteSet.popSmallest()); // 返回 2 ，并将其从集合中移除。
        System.out.println(smallestInfiniteSet.popSmallest()); // 返回 3 ，并将其从集合中移除。
        smallestInfiniteSet.addBack(1);    // 将 1 添加到该集合中。
        System.out.println(smallestInfiniteSet.popSmallest()); // 返回 1 ，因为 1 在上一步中被添加到集合中，
        System.out.println(smallestInfiniteSet.popSmallest()); // 返回 4 ，并将其从集合中移除。
        System.out.println(smallestInfiniteSet.popSmallest()); // 返回 5 ，并将其从集合中移除。
    }

    static class SmallestInfiniteSet {
        int limit = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Set<Integer> set = new HashSet<>();

        public int popSmallest() {
            if (!pq.isEmpty()) {
                int ret = pq.poll();
                set.remove(ret);
                return ret;
            }
            return limit++;
        }

        public void addBack(int num) {
            if (num >= limit) return;
            if (!set.contains(num)) {
                pq.offer(num);
                set.add(num);
            }
        }
    }

}
