package com.leo.leetcode.lcof;

import java.util.Objects;
import java.util.PriorityQueue;

public class Q41 {

    public static void main(String[] args) {
        MedianFinder obj = new MedianFinder();
        obj.addNum(1);
        obj.addNum(2);
        System.out.println(obj.findMedian());
        obj.addNum(3);
        System.out.println(obj.findMedian());
    }


    static class MedianFinder {

        PriorityQueue<Integer> lo;
        PriorityQueue<Integer> hi;

        /**
         * initialize your data structure here.
         */
        public MedianFinder() {
            lo = new PriorityQueue<>();
            hi = new PriorityQueue<>((o1, o2) -> o2 - o1);
        }

        public void addNum(int num) {
            hi.offer(num);
            lo.offer(Objects.requireNonNull(hi.poll()));
            if ((lo.size() + hi.size()) % 2 == 0) {
                hi.offer(Objects.requireNonNull(lo.poll()));
            }
        }

        public double findMedian() {
            int count = lo.size() + hi.size();
            return count % 2 == 0 ? (hi.peek() + lo.peek()) / 2.0 : lo.peek();
        }
    }
}
