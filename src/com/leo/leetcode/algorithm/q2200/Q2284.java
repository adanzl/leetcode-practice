package com.leo.leetcode.algorithm.q2200;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * 给你一个聊天记录，共包含 n 条信息。给你两个字符串数组 messages 和 senders ，其中 messages[i] 是 senders[i] 发出的一条 信息 。
 * 一条 信息 是若干用单个空格连接的 单词 ，信息开头和结尾不会有多余空格。发件人的 单词计数 是这个发件人总共发出的 单词数 。注意，一个发件人可能会发出多于一条信息。
 * 请你返回发出单词数 最多 的发件人名字。如果有多个发件人发出最多单词数，请你返回 字典序 最大的名字。
 * 注意：
 * 1、字典序里，大写字母小于小写字母。
 * 2、"Alice" 和 "alice" 是不同的名字。
 * 提示：
 * 1、n == messages.length == senders.length
 * 2、1 <= n <= 104
 * 3、1 <= messages[i].length <= 100
 * 4、1 <= senders[i].length <= 10
 * 5、messages[i] 包含大写字母、小写字母和 ' ' 。
 * 6、messages[i] 中所有单词都由 单个空格 隔开。
 * 7、messages[i] 不包含前导和后缀空格。
 * 8、senders[i] 只包含大写英文字母和小写英文字母。
 * 链接：https://leetcode.cn/problems/sender-with-largest-word-count
 */
public class Q2284 {
    public static void main(String[] args) {
        // "Alice"
        System.out.println(new Q2284().largestWordCount(new String[]{"Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"}, new String[]{"Alice", "userTwo", "userThree", "Alice"}));
        // "Charlie"
        System.out.println(new Q2284().largestWordCount(new String[]{"How is leetcode for everyone", "Leetcode is useful for practice"}, new String[]{"Bob", "Charlie"}));
    }

    public String largestWordCount(String[] messages, String[] senders) {
        PriorityQueue<Object[]> pq = new PriorityQueue<>((o1, o2) -> {
            if ((int) o1[0] != (int) o2[0]) return (int) o2[0] - (int) o1[0];
            return ((String) o2[1]).compareTo((String) o1[1]);
        });
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < messages.length; i++) {
            map.putIfAbsent(senders[i], 0);
            int len = messages[i].split(" ").length;
            map.put(senders[i], map.get(senders[i]) + len);
        }
        for (String key : map.keySet()) {
            pq.add(new Object[]{map.get(key), key});
        }
        if (pq.isEmpty()) return "";
        return pq.poll()[1].toString();
    }
}
