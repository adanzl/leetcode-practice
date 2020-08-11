package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonArray;
import com.eclipsesource.json.JsonValue;

/**
 * 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
 * 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
 * class Node {
 *     public int val;
 *     public List<Node> neighbors;
 * }
 * 测试用例格式：
 * 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。
 * 该图在测试用例中使用邻接列表表示。
 * 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
 * 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。+
 * 提示：
 *  节点数不超过 100 。
 *  每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
 *  无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
 *  由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
 *  图是连通图，你可以从给定节点访问到所有节点。
 * 链接：https://leetcode-cn.com/problems/clone-graph
 */
public class Q133 {

    public static void main(String[] args) {
        System.out.println(nodeToString(new Q133().cloneGraph(string2GraphTreeNode("[[2,4],[1,3],[2,4],[1,3]]"))));
        System.out.println(nodeToString(new Q133().cloneGraph(string2GraphTreeNode("[[]]"))));
        System.out.println(nodeToString(new Q133().cloneGraph(string2GraphTreeNode("[]"))));
        System.out.println(nodeToString(new Q133().cloneGraph(string2GraphTreeNode("[[2],[1]]"))));
    }

    static Node string2GraphTreeNode(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        if (jsonArray.isEmpty()) return null;
        Node[] nodes = new Node[jsonArray.size()];
        for (int i = 0; i < jsonArray.size(); i++) {
            nodes[i] = new Node(i + 1);
        }
        for (int i = 0; i < jsonArray.size(); i++) {
            for (JsonValue jd : jsonArray.get(i).asArray()) {
                nodes[i].neighbors.add(nodes[jd.asInt() - 1]);
            }
        }
        return nodes[0];
    }

    static String nodeToString(Node root) {
        if (root == null) return "[]";
        Node[] mark = new Node[101];
        StringBuilder output = new StringBuilder();
        Queue<Node> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        int count = 0;
        while (!nodeQueue.isEmpty()) {
            Node node = nodeQueue.remove();
            if (mark[node.val] != null) continue;
            count++;
            mark[node.val] = node;
            for (Node n : node.neighbors) {
                nodeQueue.add(n);
            }
        }
        for (int i = 0; i < count; i++) {
            StringBuilder frag = new StringBuilder();
            if (mark[i + 1].neighbors.isEmpty()) {
                output.append("[], ");
                continue;
            }
            for (Node node : mark[i + 1].neighbors) {
                frag.append(node.val).append(", ");
            }
            output.append("[" + frag.substring(0, frag.length() - 2) + "], ");
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }

    Node[] maps = new Node[101];

    boolean[] marks = new boolean[101];

    int[] deeps = new int[101];

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        return walk(node, 1);
    }

    Node walk(Node node, int deep) {
        if (marks[node.val]) return null;
        Node root = getNode(node, deep);
        for (Node n : node.neighbors) {
            Node ret = getNode(n, deep + 1);
            root.neighbors.add(ret);
        }
        for (Node n : node.neighbors) {
            if (deeps[n.val] > deep) {
                walk(n, deep + 1);
            }
        }
        marks[node.val] = true;
        return root;
    }

    Node getNode(Node node, int deep) {
        if (maps[node.val] == null) {
            maps[node.val] = new Node(node.val, new ArrayList<>(node.neighbors.size()));
            deeps[node.val] = deep;
        }
        return maps[node.val];
    }

    static class Node {

        public int val;

        public List<Node> neighbors;

        public Node() {
            val = 0;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val, ArrayList<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }
}