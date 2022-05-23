package com.leo.leetcode.algorithm.q0600;

import java.util.HashMap;
import java.util.Map;

/**
 * 设计一个 map ，满足以下几点:
 * 1、字符串表示键，整数表示值
 * 2、返回具有前缀等于给定字符串的键的值的总和
 * 实现一个 MapSum 类：
 * 1、MapSum() 初始化 MapSum 对象
 * 2、void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对 key-value 将被替代成新的键值对。
 * 3、int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
 * 提示：
 * 1、1 <= key.length, prefix.length <= 50
 * 2、key 和 prefix 仅由小写英文字母组成
 * 3、1 <= val <= 1000
 * 4、最多调用 50 次 insert 和 sum
 * 链接：https://leetcode.cn/problems/map-sum-pairs
 */
public class Q677 {

    public static void main(String[] args) {
        MapSum mapSum;
        mapSum = new MapSum();
        mapSum.insert("apple", 3);
        System.out.println(mapSum.sum("apple"));  // 3
        mapSum.insert("app", 2);
        System.out.println(mapSum.sum("ap")); // 5
        mapSum.insert("apple", 3);
        System.out.println(mapSum.sum("apple")); // 5
        System.out.println("===========================");
        mapSum = new MapSum();
        mapSum.insert("apple", 3);
        System.out.println(mapSum.sum("ap"));           // 返回 3 (apple = 3)
        mapSum.insert("app", 2);
        System.out.println(mapSum.sum("ap"));           // 返回 5 (apple + app = 3 + 2 = 5)
        System.out.println("===========================");
    }

    static class MapSum {
        Node head = new Node('\0');
        Map<String, Integer> preKeys = new HashMap<>();

        public void insert(String key, int val) {
            char[] str = key.toCharArray();
            if (preKeys.containsKey(key)) addValue(str, -preKeys.get(key));
            addValue(str, val);
            preKeys.put(key, val);
        }

        void addValue(char[] str, int val) {
            Node cur = head;
            for (char c : str) {
                int idx = c - 'a';
                cur.val += val;
                if (cur.children[idx] == null) cur.children[idx] = new Node(0);
                cur = cur.children[idx];
            }
            cur.val += val;
        }

        public int sum(String prefix) {
            char[] str = prefix.toCharArray();
            Node cur = head;
            for (char c : str) {
                int idx = c - 'a';
                if (cur.children[idx] == null) cur.children[idx] = new Node(0);
                cur = cur.children[idx];
            }
            return cur.val;
        }

        static class Node {
            int val;
            Node[] children = new Node[26];

            public Node(int val) {
                this.val = val;
            }
        }
    }
}
