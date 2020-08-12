package com.leo.leetcode.algorithm;

import java.util.HashMap;
import java.util.Map;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonArray;
import com.eclipsesource.json.JsonValue;

/**
 * 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
 * 要求返回这个链表的 深拷贝。 
 * 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。
 * 每个节点用一个 [val, random_index] 表示：
 *  val：一个表示 Node.val 的整数。
 *  random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 * 提示：
 *   -10000 <= Node.val <= 10000
 *   Node.random 为空（null）或指向链表中的节点。
 *   节点数目不超过 1000 。
 * 链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
 */
public class Q138 {

    public static void main(String[] args) {
        System.out.println(node2String(new Q138().copyRandomList(string2NodeList("[[7,null],[13,0],[11,4],[10,2],[1,0]]"))));
        System.out.println(node2String(new Q138().copyRandomList(string2NodeList("[[1,1],[2,1]]"))));
        System.out.println(node2String(new Q138().copyRandomList(string2NodeList("[[3,null],[3,0],[3,null]]"))));
        System.out.println(node2String(new Q138().copyRandomList(string2NodeList("[]"))));
    }

    static Node string2NodeList(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        if (jsonArray.isEmpty()) return null;
        Node[] nodes = new Node[jsonArray.size()];
        for (int i = 0; i < jsonArray.size(); i++) {
            nodes[i] = new Node(jsonArray.get(i).asArray().get(0).asInt());
            if (i != 0) nodes[i - 1].next = nodes[i];
        }
        for (int i = 0; i < jsonArray.size(); i++) {
            JsonValue rKey = jsonArray.get(i).asArray().get(1);
            if (!rKey.isNull()) {
                nodes[i].random = nodes[rKey.asInt()];
            }
        }
        return nodes[0];
    }

    static String node2String(Node node) {
        if (node == null) return "[]";
        StringBuilder output = new StringBuilder();
        Map<Node, Integer> map = new HashMap<>();
        Node p = node;
        int index = 0;
        while (p != null) {
            map.put(p, index++);
            p = p.next;
        }
        p = node;
        while (p != null) {
            output.append("[").append(p.val).append(", ");
            if (p.random == null) output.append("null");
            else output.append(map.get(p.random));
            output.append("], ");
            p = p.next;
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    public Node copyRandomList(Node head) {
        if (head == null) return null;
        Map<Node, Node> map = new HashMap<>();
        Node p = head, pre = null;
        while (p != null) {
            Node n = new Node(p.val);
            map.put(p, n);
            if (pre != null) pre.next = n;
            pre = n;
            p = p.next;
        }
        p = head;
        while (p != null) {
            if (p.random != null) map.get(p).random = map.get(p.random);
            p = p.next;
        }
        return map.get(head);
    }

    static class Node {

        int val;

        Node next;

        Node random;

        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }
}