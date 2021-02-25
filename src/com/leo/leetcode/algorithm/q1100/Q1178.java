package com.leo.leetcode.algorithm.q1100;

import static com.leo.utils.LCUtil.stringToStringArray;

import java.util.*;

/**
 * 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
 * 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
 * 1、单词 word 中包含谜面 puzzle 的第一个字母。
 * 2、单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
 * <p>
 * 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；
 * 而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
 * 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。
 * <p>
 * 提示：
 * 1、1 <= words.length <= 10^5
 * 2、4 <= words[i].length <= 50
 * 3、1 <= puzzles.length <= 10^4
 * 4、puzzles[i].length == 7
 * 5、words[i][j], puzzles[i][j] 都是小写英文字母。
 * 6、每个 puzzles[i] 所包含的字符都不重复。
 * <p>
 * 链接：https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle
 */
public class Q1178 {

    public static void main(String[] args) {
        // [1,1,3,2,4,0]
        System.out.println(new Q1178().findNumOfValidWords(
                stringToStringArray("[\"aaaa\",\"asas\",\"able\",\"ability\",\"actt\",\"actor\",\"access\"]"),
                stringToStringArray("[\"aboveyz\",\"abrodyz\",\"abslute\",\"absoryz\",\"actresz\",\"gaswxyz\"]"))
        );
    }

    public List<Integer> findNumOfValidWords(String[] words, String[] puzzles) {
        List<Integer> ret = new ArrayList<>(puzzles.length);
        Map<Integer, Integer> wDict = new HashMap<>();
        for (String word : words) {
            int sign = 0;
            for (int i = 0; i < word.length(); i++) sign |= 1 << (word.charAt(i) - 'a');
            if (Integer.bitCount(sign) <= 7) wDict.put(sign, wDict.getOrDefault(sign, 0) + 1);
        }
        for (String puzzle : puzzles) {
            int sign = 0;
            // 此处要从1开始，后面首字母会被强制处理
            for (int i = 1; i < puzzle.length(); i++) sign |= 1 << (puzzle.charAt(i) - 'a');
            int ans = 0, subMask = sign;
            // 二进制枚举
            do {
                int s = subMask | (1 << (puzzle.charAt(0) - 'a'));
                if (wDict.containsKey(s)) ans += wDict.get(s);
                subMask = (subMask - 1) & sign;
            } while (subMask != sign);
            ret.add(ans);
        }
        return ret;
    }
}
