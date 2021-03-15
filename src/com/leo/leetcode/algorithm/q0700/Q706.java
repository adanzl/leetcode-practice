package com.leo.leetcode.algorithm.q0700;

/**
 * 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
 * 实现 MyHashMap 类：
 * 1、MyHashMap() 用空映射初始化对象
 * 2、void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
 * 3、int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
 * 4、void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
 * <p>
 * 提示：
 * 1、0 <= key, value <= 10^6
 * 2、最多调用 104 次 put、get 和 remove 方法
 * <p>
 * 链接：https://leetcode-cn.com/problems/design-hashmap
 */
public class Q706 {

    public static void main(String[] args) {
        MyHashMap obj = new MyHashMap();
        obj.put(1, 1); // myHashMap 现在为 [[1,1]]
        obj.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
        // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
        System.out.println(obj.get(1));
        // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
        System.out.println(obj.get(3));
        obj.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
        // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
        System.out.println(obj.get(2));
        obj.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
        // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
        System.out.println(obj.get(2));
    }

    static class MyHashMap {

        int[][] map;
        int[] keys;

        /**
         * Initialize your data structure here.
         */
        public MyHashMap() {
            map = new int[1000000 / 32 + 1][];
            keys = new int[1000000 / 32 + 1];
        }

        /**
         * value will always be non-negative.
         */
        public void put(int key, int value) {
            int n = key >> 5, i = key & 0x1f;
            if (map[n] == null) map[n] = new int[32];
            map[n][i] = value;
            keys[n] |= 1 << i;
        }

        /**
         * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
         */
        public int get(int key) {
            int n = key >> 5, i = key & 0x1f;
            return (keys[n] & 1 << i) == 0 ? -1 : map[n][i];
        }

        /**
         * Removes the mapping of the specified value key if this map contains a mapping for the key
         */
        public void remove(int key) {
            int n = key >> 5, i = key & 0x1f;
            keys[n] &= ~(1 << i);
        }
    }
}
