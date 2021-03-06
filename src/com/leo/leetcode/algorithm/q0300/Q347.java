package com.leo.leetcode.algorithm.q0300;

import com.leo.utils.LCUtil;

import java.util.*;

public class Q347 {

    public static void main(String[] args) {
        new Q347().TestOJ();
    }

    public void TestOJ() {
        System.out.println(topKFrequent(LCUtil.stringToIntegerArray("[1,1,1,2,2,3]"), 2)); // [1,2]
        System.out.println(topKFrequent(LCUtil.stringToIntegerArray("[1,1,1,2,2,3,3]"), 2)); // [1,2]
        System.out.println(topKFrequent(LCUtil.stringToIntegerArray("[1]"), 1)); // [1]
    }

    public List<Integer> topKFrequent(int[] nums, int k) {
        // build hash map : character and how often it appears
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        // init heap 'the less frequent element first'
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.comparingInt(count::get));

        // keep k top frequent elements in the heap
        for (int n : count.keySet()) {
            heap.add(n);
            if (heap.size() > k)
                heap.poll();
        }

        // build output list
        List<Integer> top_k = new LinkedList<>();
        while (!heap.isEmpty())
            top_k.add(heap.poll());
        Collections.reverse(top_k);
        return top_k;
    }
}
