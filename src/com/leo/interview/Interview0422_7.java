package com.leo.interview;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

/**
 * 【第三题】路径规划
 * 假设现在有一个有向无环图，每个节点上都带有正数权重。我们希望找到一条最优路径，使得这个路径上经过的节点的权重之和最大。
 * 输入:n个节点，m个路径，起点
 * 输出:最优路径的权重值之和
 * 举例:
 * 3个节点:
 * A 1
 * B 2
 * C 2
 * 3条路径:
 * A->B
 * B->C
 * A->C
 * 起点:
 * A
 * 输出:5 (最优路径是 A->B->C ， 权重之和是 1+2+2=5)
 * • 附加问题:我们要求的输入是有向无环图，但是没人知道实际使用的时
 * 候会有什么数据输入进来，如何避免输入了带环路的图导致的死循环呢?
 */
public class Interview0422_7 {

    public static void main(String[] args) {
        Node A = new Node(1);
        Node B = new Node(2);
        Node C = new Node(2);
        Node D = new Node(5);
        A.next.add(B);
        B.next.add(C);
        A.next.add(C);
        A.next.add(D);
        D.next.add(A);
        System.out.println(new Interview0422_7().findMaxPath(A)); // 5
    }

    int max = 0;
    HashSet<Node> visited = new HashSet<>();

    int findMaxPath(Node head) {
        findPath(head, 0);
        return this.max;
    }

    void findPath(Node node, int path) {
        this.max = Math.max(this.max, path + node.val);
        this.visited.add(node);
        for (Node next : node.next) {
            if (this.visited.contains(next)) continue;
            findPath(next, path + node.val);
        }
        this.visited.remove(node);
    }

    static class Node {
        List<Node> next = new ArrayList<>();
        int val;

        Node(int val) {
            this.val = val;
        }
    }
}
