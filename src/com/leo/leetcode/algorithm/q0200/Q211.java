package com.leo.leetcode.algorithm.q0200;

/**
 * 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
 * <p>
 * 实现词典类 WordDictionary ：
 * 1、WordDictionary() 初始化词典对象
 * 2、void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
 * 3、bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回 false 。
 * 4、word 中可能包含一些 '.' ，每个. 都可以表示任何一个字母。
 * <p>
 * 提示：
 * 1、1 <= word.length <= 500
 * 2、addWord 中的 word 由小写英文字母组成
 * 3、search 中的 word 由 '.' 或小写英文字母组成
 * 4、最多调用 50000 次 addWord 和 search
 * <p>
 * 链接：https://leetcode-cn.com/problems/design-add-and-search-words-data-structure
 */
public class Q211 {

    public static void main(String[] args) {
        WordDictionary obj = new WordDictionary();
        obj.addWord("bad");
        obj.addWord("dad");
        obj.addWord("mad");
        // true
        System.out.println(obj.search("ma."));
        // true
        System.out.println(obj.search("bad"));
        // false
        System.out.println(obj.search("pad"));
        // true
        System.out.println(obj.search(".ad"));
        // true
        System.out.println(obj.search("b.."));
    }

    static class WordDictionary {

        static class TNode {
            char c;
            boolean bEnd = false;

            TNode(char c) {
                this.c = c;
                this.sub = new TNode[26];
            }

            TNode[] sub;
        }

        TNode root;

        public WordDictionary() {
            root = new TNode(' ');
        }

        public void addWord(String word) {
            TNode p = root;
            for (char c : word.toCharArray()) {
                int idx = c - 'a';
                if (p.sub[idx] == null) p.sub[idx] = new TNode(c);
                p = p.sub[idx];
            }
            p.bEnd = true;
        }

        public boolean search(String word) {
            return search(word.toCharArray(), 0, root);
        }

        boolean search(char[] str, int offset, TNode tRoot) {
            if (tRoot == null) return false;
            if (offset == str.length) return tRoot.bEnd;
            char c = str[offset];
            if (c == '.') {
                for (TNode subNode : tRoot.sub) {
                    if (search(str, offset + 1, subNode)) return true;
                }
            } else {
                return search(str, offset + 1, tRoot.sub[c - 'a']);
            }
            return false;
        }
    }

}
