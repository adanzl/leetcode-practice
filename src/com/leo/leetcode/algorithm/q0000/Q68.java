package com.leo.leetcode.algorithm.q0000;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
 * 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
 * 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
 * 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
 * 说明:
 * 单词是指由非空格字符组成的字符序列。
 * 每个单词的长度大于 0，小于等于 maxWidth。
 * 输入单词数组 words 至少包含一个单词。
 * 链接：https://leetcode-cn.com/problems/text-justification
 */
public class Q68 {

    public static void main(String[] args) {
        System.out.println(new Q68().fullJustify(new String[]{"What", "must", "be", "acknowledgment", "shall", "be"}, 16));
        System.out.println(new Q68().fullJustify(new String[]{"ask", "not", "what are"}, 16));
        // ["This    is    an", "example  of text", "justification.  "]
        System.out.println(new Q68().fullJustify(new String[]{"This", "is", "an", "example", "of", "text", "justification."}, 16));
        System.out.println(new Q68().fullJustify(new String[]{"This", "is", "an", "example", "of", "text", "justification...", "GO"}, 16));
        System.out.println(new Q68().fullJustify(new String[]{""}, 1));
        // ["What   must   be", "acknowledgment  ", "shall be        "]
        System.out.println(new Q68().fullJustify(new String[]{"What", "must", "be", "acknowledgment", "shall", "be"}, 16));
        // ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  " ]
        System.out.println(new Q68().fullJustify(new String[]{"Science", "is", "what", "we", "understand", "well"
                , "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"}, 20));
    }

    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> out = new ArrayList<>();
        int count = 0, len = 0, offset = 0;
        for (int i = 0; i < words.length; ) {
            if (len + words[i].length() <= maxWidth) {
                len += words[i].length() + 1;
                i++;
                count++;
            } else {
                if (count != 1) len--;
                char[] line = new char[maxWidth];
                int iLine = 0;
                int cPadding = count == 1 ? 1 : (count - 1);
                int padding = (maxWidth - len) / cPadding;
                int ext = maxWidth - len - cPadding * padding;
                padding++;
                for (int j = 0; j < count; j++) {
                    String word = words[offset + j];
                    for (int k = 0; k < word.length(); k++) line[iLine++] = word.charAt(k);
                    if (cPadding-- > 0) for (int k = 0; k < padding; k++) line[iLine++] = ' ';
                    if (ext-- > 0) line[iLine++] = ' ';
                }
                out.add(new String(line));
                offset += count;
                count = 0;
                len = 0;
            }
        }
        if (count != 0) {
            char[] line = new char[maxWidth];
            int iLine = 0;
            for (int j = 0; j < count; j++) {
                String word = words[offset + j];
                for (int k = 0; k < word.length(); k++) line[iLine++] = word.charAt(k);
                if (iLine < maxWidth) line[iLine++] = ' ';
            }
            Arrays.fill(line, iLine, line.length, ' ');
            out.add(new String(line));
        }
        return out;
    }
}
