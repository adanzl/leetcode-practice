package com.leo.leetcode.algorithm.q0100;

import java.util.HashMap;
import java.util.Map;

public class Q146 {
    public void TestOJ() {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.get(1));       // 返回  1
        cache.put(3, 3);    // 该操作会使得密钥 2 作废
        System.out.println(cache.get(2));       // 返回 -1 (未找到)
        cache.put(4, 4);    // 该操作会使得密钥 1 作废
        System.out.println(cache.get(1));       // 返回 -1 (未找到)
        System.out.println(cache.get(3));       // 返回  3
        System.out.println(cache.get(4));       // 返回  4
    }

    static class LRUCache {

        Map<Integer, DNode> map;
        DNode head;
        DNode tail;
        final int capacity;

        public LRUCache(int capacity) {
            this.map = new HashMap<>();
            this.capacity = capacity;
        }

        public int get(int key) {
            if (!map.containsKey(key)) {
                return -1;
            }
            DNode node = map.get(key);
            updateNode(node);
            return node.v;
        }

        public void put(int key, int value) {
            if (map.containsKey(key)) {
                DNode n = map.get(key);
                n.v = value;
                updateNode(n);
            } else {
                DNode n = new DNode(key, value);
                if (map.size() == capacity) {
                    map.remove(tail.k);
                    removeNode(tail);
                }
                map.put(key, n);
                updateNode(n);
            }
        }

        void updateNode(DNode node) {
            if (node == head) return;
            removeNode(node);

            node.next = head;
            if (head != null) head.pre = node;
            node.pre = null;
            if (head == null) tail = node;
            head = node;
        }

        void removeNode(DNode node) {
            if (node == null) return;
            DNode preNode = node.pre, nextNode = node.next;
            if (preNode != null) preNode.next = nextNode;
            if (nextNode != null) nextNode.pre = preNode;
            if (node == tail) tail = node.pre;
        }

        static class DNode {
            int k;
            int v;
            DNode pre;
            DNode next;

            DNode(int k, int v) {
                this.k = k;
                this.v = v;
            }
        }
    }


//    class LRUCache extends LinkedHashMap<Integer, Integer> {
//        private int capacity;
//
//        public LRUCache(int capacity) {
//            super(capacity, 0.75F, true);
//            this.capacity = capacity;
//        }
//
//        public int get(int key) {
//            return super.getOrDefault(key, -1);
//        }
//
//        public void put(int key, int value) {
//            super.put(key, value);
//        }
//
//        @Override
//        protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
//            return size() > capacity;
//        }
//    }
}



