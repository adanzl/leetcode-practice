package com.leo.leetcode.algorithm.q0700;

/**
 * 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
 * 实现 MyHashSet 类：
 * 1、void add(key) 向哈希集合中插入值 key 。
 * 2、bool contains(key) 返回哈希集合中是否存在这个值 key 。
 * 3、void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
 * <p>
 * 提示：
 * 1、0 <= key <= 10^6
 * 2、最多调用 10^4 次 add、remove 和 contains 。
 * <p>
 * 进阶：你可以不使用内建的哈希集合库解决此问题吗？
 * <p>
 * 链接：https://leetcode-cn.com/problems/design-hashset
 */
public class Q705 {

    public static void main(String[] args) {
        MyHashSet obj = new MyHashSet();
        obj.add(1);      // set = [1]
        obj.add(2);      // set = [1, 2]
        obj.add(1000000);      // set = [1, 2]
        System.out.println(obj.contains(1000000)); // 返回 True
        System.out.println(obj.contains(1)); // 返回 True
        System.out.println(obj.contains(3)); // 返回 False ，（未找到）
        obj.add(2);      // set = [1, 2]
        System.out.println(obj.contains(2)); // 返回 True
        obj.remove(2);   // set = [1]
        System.out.println(obj.contains(2)); // 返回 False ，（已移除）
    }

    static class MyHashSet {

        int[] marks = new int[1000000 / 32 + 1];

        public MyHashSet() {

        }

        public void add(int key) {
            int n = key / 32, i = key % 32;
            marks[n] |= 1 << i;
        }

        public void remove(int key) {
            int n = key / 32, i = key % 32;
            marks[n] &= ~(1 << i);
        }

        /**
         * Returns true if this set contains the specified element
         */
        public boolean contains(int key) {
            int n = key / 32, i = key % 32;
            return (marks[n] & 1 << i) != 0;
        }
    }
}
