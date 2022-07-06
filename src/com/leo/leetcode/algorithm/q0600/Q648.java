package com.leo.leetcode.algorithm.q0600;

import java.util.List;

import static com.leo.utils.LCUtil.stringToStringList;

/**
 * 在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
 * 例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
 * 现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。
 * 你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
 * 你需要输出替换之后的句子。
 * 提示：
 * 1、1 <= dictionary.length <= 1000
 * 2、1 <= dictionary[i].length <= 100
 * 3、dictionary[i] 仅由小写字母组成。
 * 4、1 <= sentence.length <= 10^6
 * 5、sentence 仅由小写字母和空格组成。
 * 6、sentence 中单词的总量在范围 [1, 1000] 内。
 * 7、sentence 中每个单词的长度在范围 [1, 1000] 内。
 * 8、sentence 中单词之间由一个空格隔开。
 * 9、sentence 没有前导或尾随空格。
 * 链接：https://leetcode.cn/problems/replace-words
 */
public class Q648 {

    public static void main(String[] args) {
        // "the cat was rat by the bat"
        System.out.println(new Q648().replaceWords(stringToStringList("[\"cat\",\"bat\",\"rat\"]"), "the cattle was rattled by the battery"));
        // "a a b c"
        System.out.println(new Q648().replaceWords(stringToStringList("[\"a\",\"b\",\"c\"]"), "aadsfasf absbs bbab cadsfafs"));
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        String[] strs = sentence.split(" ");
        StringBuilder ret = new StringBuilder();
        dictionary.sort((a, b) -> b.length() - a.length());
        for (String str : strs) {
            for (String dic : dictionary) {
                if (str.startsWith(dic)) {
                    str = dic;
                }
            }
            ret.append(str).append(" ");
        }
        return ret.substring(0, ret.length() - 1);
    }
}
