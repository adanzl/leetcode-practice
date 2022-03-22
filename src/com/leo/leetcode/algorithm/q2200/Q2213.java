package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的字符串 s 。另给你一个下标从 0 开始、长度为 k 的字符串 queryCharacters ，
 * 一个下标从 0 开始、长度也是 k 的整数 下标 数组 queryIndices ，这两个都用来描述 k 个查询。
 * 第 i 个查询会将 s 中位于下标 queryIndices[i] 的字符更新为 queryCharacters[i] 。
 * 返回一个长度为 k 的数组 lengths ，其中 lengths[i] 是在执行第 i 个查询 之后 s 中仅由 单个字符重复 组成的 最长子字符串 的 长度 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 由小写英文字母组成
 * 3、k == queryCharacters.length == queryIndices.length
 * 4、1 <= k <= 10^5
 * 5、queryCharacters 由小写英文字母组成
 * 6、0 <= queryIndices[i] < s.length
 * 链接：https://leetcode-cn.com/problems/longest-substring-of-one-repeating-character
 */
public class Q2213 {

    public static void main(String[] args) {
        // [3,3,4]
        System.out.println(Arrays.toString(new Q2213().longestRepeating("babacc", "bcb", stringToIntegerArray("[1,3,3]"))));
        // [2,3]
        System.out.println(Arrays.toString(new Q2213().longestRepeating("abyzz", "aa", stringToIntegerArray("[2,1]"))));
    }

    Node[] treeArr;
    char[] str;

    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        int[] ret = new int[queryIndices.length];
        treeArr = new Node[s.length() << 2]; // l-r-v
        str = s.toCharArray();
        this.buildTree(treeArr, 0, 0, s.length() - 1);
        for (int i = 0; i < queryIndices.length; i++) {
            char c = queryCharacters.charAt(i);
            if (str[queryIndices[i]] != c) {
                str[queryIndices[i]] = c;
                updateNode(0, queryIndices[i]);
            }
            ret[i] = treeArr[0].max;
        }
        return ret;
    }

    Node buildTree(Node[] treeArr, int root, int l, int r) {
        int mid = (l + r) >> 1, sl = (root << 1) + 1, sr = sl + 1;
        Node pNode = treeArr[root] = new Node(l, r);
        if (l == r) return pNode;
        Node lNode = buildTree(treeArr, sl, l, mid);
        Node rNode = buildTree(treeArr, sr, mid + 1, r);
        merge(pNode, lNode, rNode);
        return pNode;
    }

    void merge(Node pNode, Node lNode, Node rNode) {
        pNode.max = Math.max(lNode.max, rNode.max);
        if (str[lNode.r] == str[rNode.l]) {
            if (lNode.cPre == lNode.r - lNode.l + 1) pNode.cPre = lNode.cPre + rNode.cPre;
            else pNode.cPre = lNode.cPre;
            if (rNode.cSuf == rNode.r - rNode.l + 1) pNode.cSuf = lNode.cSuf + rNode.cSuf;
            else pNode.cSuf = rNode.cSuf;
            pNode.max = Math.max(pNode.max, lNode.cSuf + rNode.cPre);
        } else {
            pNode.cPre = lNode.cPre;
            pNode.cSuf = rNode.cSuf;
        }
    }

    void updateNode(int root, int idx) {
        Node pNode = treeArr[root];
        if (pNode.l == pNode.r || pNode.l > idx || pNode.r < idx) return;
        int sl = (root << 1) + 1, sr = sl + 1;
        updateNode(sl, idx);
        updateNode(sr, idx);
        merge(pNode, treeArr[sl], treeArr[sr]);
    }

    static class Node {
        int l, r, cPre = 1, cSuf = 1, max = 1;

        public Node(int l, int r) {
            this.l = l;
            this.r = r;
        }
    }
}
