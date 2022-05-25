package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.TestCase;

import java.util.*;

/**
 * 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：
 * 1、每对相邻的单词之间仅有单个字母不同。
 * 2、转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
 * 3、sk == endWord
 * 给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。
 * 请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。
 * 每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。
 * 提示：
 * 1、1 <= beginWord.length <= 5
 * 2、endWord.length == beginWord.length
 * 3、1 <= wordList.length <= 5000
 * 4、wordList[i].length == beginWord.length
 * 5、beginWord、endWord 和 wordList[i] 由小写英文字母组成
 * 6、beginWord != endWord
 * 7、wordList 中的所有单词 互不相同
 * 链接：https://leetcode.cn/problems/word-ladder-ii
 */
public class Q126 {
    
    public static void main(String[] args) {

        final TestCase tc1 = new TestCase("resources/algorithm/q0100/Q126/Case77003406");
        LCUtil.calcRun(() -> System.out.println(new Q126().findLadders(tc1.getData(0), tc1.getData(1), LCUtil.stringToStringList(tc1.getData(2)))));
        final TestCase tc2 = new TestCase("resources/algorithm/q0100/Q126/Case77014075");
        LCUtil.calcRun(() -> System.out.println(new Q126().findLadders(tc2.getData(0), tc2.getData(1), LCUtil.stringToStringList(tc2.getData(2)))));
        // ["hot", "dog"]
        LCUtil.calcRun(() -> System.out.println(new Q126().findLadders("hot", "dog", LCUtil.stringToStringList("[\"hot\",\"dog\"]"))));
        // [["hit","hot","lot","log","cog"],["hit","hot","dot","dog","cog"]]
        LCUtil.calcRun(() -> System.out.println(new Q126().findLadders("hit", "cog", LCUtil.stringToStringList("[\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]"))));
        // []
        LCUtil.calcRun(() -> System.out.println(new Q126().findLadders("hit", "cog", LCUtil.stringToStringList("[\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]"))));
    }

    private static final int INF = 1 << 20;

    //=================================================================================================================
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Map<String, Set<String>> nextMap = new HashMap<>();
        List<List<String>> out = new ArrayList<>();
        LinkedList<LinkedList<String>> tmp = new LinkedList<>();
        wordList.add(beginWord);
        for (int i = 0; i < wordList.size(); i++) {
            String str1 = wordList.get(i);
            Set<String> next1 = nextMap.computeIfAbsent(str1, (key) -> new HashSet<>());
            for (int j = i + 1; j < wordList.size(); j++) {
                String str2 = wordList.get(j);
                if (canEdit(str1, str2)) {
                    Set<String> next2 = nextMap.computeIfAbsent(str2, (key) -> new HashSet<>());
                    next1.add(str2);
                    next2.add(str1);
                }
            }
        }
        if (!nextMap.containsKey(endWord)) return out;
        LinkedList<String> ans = new LinkedList<>();
        ans.add(beginWord);
        tmp.add(ans);
        walk(out, tmp, nextMap, new HashMap<>(), endWord);
        return out;
    }

    private void walk(List<List<String>> out, LinkedList<LinkedList<String>> tempList, final Map<String, Set<String>> nextMap, Map<String, Integer> visited, final String endWord) {
        if (tempList.isEmpty()) return;
        boolean bFind = false;
        int c = tempList.size();
        while (c-- > 0) {
            LinkedList<String> answer = tempList.removeFirst();
            Set<String> nextSet = new HashSet<>(nextMap.get(answer.getLast()));
            if (nextSet.contains(endWord)) {
                answer.add(endWord);
                out.add(answer);
                bFind = true;
                continue;
            }
            for (String s : nextSet) {
                if (visited.getOrDefault(s, INF) >= answer.size() + 1) {
                    visited.put(s, answer.size() + 1);
                    LinkedList<String> nAnswer = new LinkedList<>(answer);
                    nAnswer.addLast(s);
                    tempList.add(nAnswer);
                }
            }
        }
        if (!bFind) walk(out, tempList, nextMap, visited, endWord);
    }

    private boolean canEdit(String str1, String str2) {
        if (str1 == null || str2 == null || str1.length() != str2.length()) return false;
        int cFind = 0, i = 0;
        while (i < str1.length()) {
            if (str1.charAt(i) != str2.charAt(i)) cFind++;
            if (cFind > 1) return false;
            i++;
        }
        return cFind == 1;
    }
}
