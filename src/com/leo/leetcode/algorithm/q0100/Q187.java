package com.leo.leetcode.algorithm.q0100;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。
 * 在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
 * 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
 * <p>
 * 提示：
 * 1、0 <= s.length <= 105
 * 2、s[i] 为 'A'、'C'、'G' 或 'T'
 * <p>
 * 链接：https://leetcode-cn.com/problems/repeated-dna-sequences
 */
public class Q187 {

    public static void main(String[] args) {
        // ["AAAAACCCCC","CCCCCAAAAA"]
        System.out.println(new Q187().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));
        // ["AAAAAAAAAA"]
        System.out.println(new Q187().findRepeatedDnaSequences("AAAAAAAAAAAAA"));
    }

    public List<String> findRepeatedDnaSequences(String s) {
        Map<Integer, Integer> m = new HashMap<>();
        List<String> ret = new ArrayList<>();
        int sign = 0;
        for (int i = 0; i < s.length(); i++) {
            int v = s.charAt(i) & 0x07;
            sign = 0x3fffffff & ((sign << 3) + v);
            if (i < 9) continue;
            int count = m.getOrDefault(sign, 0);
            if (count == 1) ret.add(s.substring(i - 9, i + 1));
            m.put(sign, count + 1);
        }
        return ret;
    }
}
