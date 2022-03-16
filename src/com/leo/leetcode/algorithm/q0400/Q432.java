package com.leo.leetcode.algorithm.q0400;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
 * 实现 AllOne 类：
 * 1、AllOne() 初始化数据结构的对象。
 * 2、inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
 * 3、dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
 * 4、getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
 * 5、getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
 * 提示：
 * 1、1 <= key.length <= 10
 * 2、key 由小写英文字母组成
 * 3、测试用例保证：在每次调用 dec 时，数据结构中总存在 key
 * 4、最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10^4 次
 * 链接：https://leetcode-cn.com/problems/all-oone-data-structure
 */
public class Q432 {

    public static void main(String[] args) {
        AllOne allOne = new AllOne();
        allOne.inc("hello");
        allOne.inc("world");
        allOne.inc("leet");
        allOne.inc("code");
        allOne.inc("ds");
        allOne.inc("leet");
        System.out.println(allOne.getMaxKey()); // leet
        allOne.inc("ds");
        allOne.dec("leet");
        System.out.println(allOne.getMaxKey()); // ds
        allOne.dec("ds");
        allOne.inc("hello");
        System.out.println(allOne.getMaxKey()); // hello
        allOne.inc("hello");
        allOne.inc("hello");
        allOne.dec("world");
        allOne.dec("leet");
        allOne.dec("code");
        allOne.dec("ds");
        System.out.println(allOne.getMaxKey()); // hello
        allOne.inc("new");
        allOne.inc("new");
        allOne.inc("new");
        allOne.inc("new");
        allOne.inc("new");
        allOne.inc("new");
        System.out.println(allOne.getMaxKey()); // new
        System.out.println(allOne.getMinKey()); // hello
        System.out.println("====================");
        allOne = new AllOne();
        allOne.inc("a");
        allOne.inc("b");
        allOne.inc("b");
        allOne.inc("c");
        allOne.inc("c");
        allOne.inc("c");
        allOne.dec("b");
        allOne.dec("b");
        System.out.println(allOne.getMinKey()); // a
        allOne.dec("a");
        System.out.println(allOne.getMaxKey()); // c
        System.out.println(allOne.getMinKey()); // c
        System.out.println("====================");
        allOne = new AllOne();
        allOne.inc("hello");
        allOne.inc("hello");
        System.out.println(allOne.getMaxKey()); // "hello"
        System.out.println(allOne.getMinKey()); // "hello"
        allOne.inc("leet");
        System.out.println(allOne.getMaxKey()); // "hello"
        System.out.println(allOne.getMinKey()); // "leet"
    }

    static class AllOne {

        public AllOne() {

        }

        Map<String, Integer> strCount = new HashMap<>();
        Map<Integer, CNode> countMap = new HashMap<>();
        CNode minNode;
        CNode maxNode;

        public void inc(String key) {
            int oCount = strCount.getOrDefault(key, 0), nCount = oCount + 1;
            CNode oldNode = countMap.get(oCount), newNode = countMap.get(nCount);
            if (null == newNode) {
                newNode = new CNode(nCount);
                countMap.put(nCount, newNode);
                if (null != oldNode) {
                    newNode.next = oldNode.next;
                    newNode.pre = oldNode;
                    if (oldNode.next != null) oldNode.next.pre = newNode;
                    oldNode.next = newNode;
                }
            }
            newNode.set.add(key);
            if (minNode == null) minNode = newNode;
            if (maxNode == null) maxNode = newNode;
            if (maxNode.count < newNode.count) {
                maxNode.next = newNode;
                newNode.pre = maxNode;
                maxNode = newNode;
            }
            if (minNode.count > newNode.count) {
                minNode.pre = newNode;
                newNode.next = minNode;
                minNode = newNode;
            }
            if (null != oldNode) {
                oldNode.set.remove(key);
                if (oldNode.set.isEmpty()) {
                    countMap.remove(oCount);
                    if (null != oldNode.pre) oldNode.pre.next = oldNode.next;
                    if (null != oldNode.next) oldNode.next.pre = oldNode.pre;
                    if (oldNode == maxNode) maxNode = oldNode.next;
                    if (oldNode == minNode) minNode = oldNode.next;
                }
            }
            strCount.put(key, nCount);
        }

        public void dec(String key) {
            int oCount = strCount.getOrDefault(key, 0), nCount = oCount - 1;
            if (oCount == 0) return;
            strCount.put(key, nCount);

            CNode oldNode = countMap.get(oCount), newNode = countMap.get(nCount);
            if (null == newNode && nCount != 0) {
                newNode = new CNode(nCount);
                countMap.put(nCount, newNode);
                if (null != oldNode) {
                    newNode.pre = oldNode.pre;
                    newNode.next = oldNode;
                    if (oldNode.pre != null) oldNode.pre.next = newNode;
                    oldNode.pre = newNode;
                }
            }
            if (null != newNode) newNode.set.add(key);
            if (minNode == null) minNode = newNode;
            if (maxNode == null) maxNode = newNode;
            if (newNode != null && maxNode.count < newNode.count) {
                maxNode.next = newNode;
                newNode.pre = maxNode;
                maxNode = newNode;
            }
            if (newNode != null && minNode.count > newNode.count) {
                minNode.pre = newNode;
                newNode.next = minNode;
                minNode = newNode;
            }
            if (null != oldNode) {
                oldNode.set.remove(key);
                if (oldNode.set.isEmpty()) {
                    countMap.remove(oCount);
                    if (null != oldNode.pre) oldNode.pre.next = oldNode.next;
                    if (null != oldNode.next) oldNode.next.pre = oldNode.pre;
                    if (oldNode == maxNode) maxNode = oldNode.next;
                    if (oldNode == minNode) {
                        if (null != newNode) minNode = newNode;
                        else minNode = oldNode.next;
                    }
                }
            }
            strCount.put(key, nCount);
        }

        public String getMaxKey() {
            if (null == maxNode) return "";
            return maxNode.set.iterator().next();
        }

        public String getMinKey() {
            if (null == minNode) return "";
            return minNode.set.iterator().next();
        }

        static class CNode {
            public int count;
            public CNode pre = null;
            public CNode next = null;
            Set<String> set = new HashSet<>();

            CNode(int c) {
                this.count = c;
            }
        }
    }
}
