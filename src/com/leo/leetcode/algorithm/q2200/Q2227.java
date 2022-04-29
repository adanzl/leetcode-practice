package com.leo.leetcode.algorithm.q2200;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToCharArray;
import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给你一个字符数组 keys ，由若干 互不相同 的字符组成。还有一个字符串数组 values ，内含若干长度为 2 的字符串。
 * 另给你一个字符串数组 dictionary ，包含解密后所有允许的原字符串。请你设计并实现一个支持加密及解密下标从 0 开始字符串的数据结构。
 * 字符串 加密 按下述步骤进行：
 * 对字符串中的每个字符 c ，先从 keys 中找出满足 keys[i] == c 的下标 i 。
 * 在字符串中，用 values[i] 替换字符 c 。
 * 字符串 解密 按下述步骤进行：
 * 1、将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 s ，找出满足 values[i] == s 的一个下标 i 。如果存在多个有效的 i ，从中选择 任意 一个。这意味着一个字符串解密可能得到多个解密字符串。
 * 2、在字符串中，用 keys[i] 替换 s 。
 * 实现 Encrypter 类：
 * 1、Encrypter(char[] keys, String[] values, String[] dictionary) 用 keys、values 和 dictionary 初始化 Encrypter 类。
 * 2、String encrypt(String word1) 按上述加密过程完成对 word1 的加密，并返回加密后的字符串。
 * 3、int decrypt(String word2) 统计并返回可以由 word2 解密得到且出现在 dictionary 中的字符串数目。
 * 提示：
 * 1、1 <= keys.length == values.length <= 26
 * 2、values[i].length == 2
 * 3、1 <= dictionary.length <= 100
 * 4、1 <= dictionary[i].length <= 100
 * 5、所有 keys[i] 和 dictionary[i] 互不相同
 * 6、1 <= word1.length <= 2000
 * 7、1 <= word2.length <= 200
 * 8、所有 word1[i] 都出现在 keys 中
 * 9、word2.length 是偶数
 * 10、keys、values[i]、dictionary[i]、word1 和 word2 只含小写英文字母
 * 11、至多调用 encrypt 和 decrypt 总计 200 次
 * 链接：https://leetcode-cn.com/problems/encrypt-and-decrypt-strings
 */
public class Q2227 {

    public static void main(String[] args) {
        Encrypter encrypter = new Encrypter(
                stringToCharArray("[\"a\",\"b\",\"c\",\"z\"]"),
                stringToStringArray("[\"aa\",\"bb\",\"cc\",\"zz\"]"),
                stringToStringArray("[\"aa\",\"aaa\",\"aaaa\",\"aaaaa\",\"aaaaaaa\"]"));
        System.out.println(encrypter.decrypt("aa")); // 0
        System.out.println(encrypter.decrypt("aaaa")); // 1
        System.out.println(encrypter.decrypt("aaaa")); // 1
        System.out.println(encrypter.decrypt("aaaaaaaa")); // 1
        System.out.println(encrypter.decrypt("aaaaaaaaaaaaaa")); // 1
        System.out.println(encrypter.decrypt("aefagafvabfgshdthn")); // 0
        System.out.println("==================================");
        Encrypter e1 = new Encrypter(
                stringToCharArray("['a', 'b', 'c', 'd']"),
                stringToStringArray("[\"ei\", \"zf\", \"ei\", \"am\"]"),
                stringToStringArray("[\"abcd\", \"acbd\", \"adbc\", \"badc\", \"dacb\", \"cadb\", \"cbda\", \"abad\"]"));
        System.out.println(e1.encrypt("abcd")); // 返回 "eizfeiam"。
        // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为 "am"。
        System.out.println(e1.decrypt("eizfeiam")); // return 2.

    }

    static class Encrypter {
        Map<Character, String> charMap = new HashMap<>();
        Map<String, List<Character>> codeMap = new HashMap<>();
        Map<String, Integer> dict = new HashMap<>();

        public Encrypter(char[] keys, String[] values, String[] dictionary) {
            for (int i = 0; i < keys.length; i++) {
                charMap.put(keys[i], values[i]);
                codeMap.putIfAbsent(values[i], new ArrayList<>());
                codeMap.get(values[i]).add(keys[i]);
            }
            for (String dic : dictionary) {
                String key = this.encrypt(dic);
                dict.put(key, dict.getOrDefault(key, 0) + 1);
            }
        }

        public String encrypt(String word1) {
            StringBuilder sb = new StringBuilder();
            char[] str = word1.toCharArray();
            for (char c : str) sb.append(charMap.get(c));
            return sb.toString();
        }

        public int decrypt(String word2) {
            return dict.getOrDefault(word2, 0);
        }
    }
}
