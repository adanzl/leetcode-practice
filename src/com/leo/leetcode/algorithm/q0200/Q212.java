package com.leo.leetcode.algorithm.q0200;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToChar2dArray;
import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
 * 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
 * 同一个单元格内的字母在一个单词中不允许被重复使用。
 * 提示：
 * 1、m == board.length
 * 2、n == board[i].length
 * 3、1 <= m, n <= 12
 * 4、board[i][j] 是一个小写英文字母
 * 5、1 <= words.length <= 3 * 10^4
 * 6、1 <= words[i].length <= 10
 * 7、words[i] 由小写英文字母组成
 * 8、words 中的所有字符串互不相同
 * 链接：https://leetcode-cn.com/problems/word-search-ii
 */
public class Q212 {

    public static void main(String[] args) {
        // ["eat","oath"]
        System.out.println(new Q212().findWords(
                stringToChar2dArray("[[\"o\",\"a\",\"a\",\"n\"],[\"e\",\"t\",\"a\",\"e\"],[\"i\",\"h\",\"k\",\"r\"],[\"i\",\"f\",\"l\",\"v\"]]")
                , stringToStringArray("[\"oath\",\"pea\",\"eat\",\"rain\"]")));
        // []
        System.out.println(new Q212().findWords(
                stringToChar2dArray("[[\"a\",\"b\"],[\"c\",\"d\"]]")
                , stringToStringArray("[\"abcb\"]")));
    }

    public List<String> findWords(char[][] board, String[] words) {
        List<String> ret = new ArrayList<>();
        for (String word : words) addDict(word);
        main:
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                walk(board, i, j, root, ret);
                if (words.length == ret.size()) break main;
            }
        }
        return ret;
    }

    void walk(char[][] board, int x, int y, TireNode tNode, List<String> out) {
        if (x < 0 || x > board.length - 1 || y < 0 || y > board[0].length - 1 || board[x][y] == ' ') return;
        char c = board[x][y];
        TireNode node = tNode.sub[c - 'a'];
        if (node == null) return;
        if (node.str != null) {
            out.add(node.str);
            node.str = null;
        }
        board[x][y] = ' ';
        walk(board, x + 1, y, node, out);
        walk(board, x - 1, y, node, out);
        walk(board, x, y + 1, node, out);
        walk(board, x, y - 1, node, out);
        board[x][y] = c;
    }

    TireNode root = new TireNode(' ');

    void addDict(String word) {
        TireNode p = root;
        for (int i = 0; i < word.length(); i++) {
            int ic = word.charAt(i) - 'a';
            if (p.sub[ic] == null) p.sub[ic] = new TireNode(word.charAt(i));
            p = p.sub[ic];
        }
        p.str = word;
    }

    static class TireNode {
        TireNode(char c) {
            this.c = c;
        }

        char c;
        String str;
        TireNode[] sub = new TireNode[26];
    }
}
