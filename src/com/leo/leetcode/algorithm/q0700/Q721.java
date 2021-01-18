package com.leo.leetcode.algorithm.q0700;

import java.util.*;

import static com.leo.utils.LCUtil.stringToListListString;

/**
 * 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，
 * 其中第一个元素 accounts[i][0] 是 名称(name)，其余元素是 emails 表示该账户的邮箱地址。
 * 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。
 * 请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。
 * 一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
 * 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。
 * 账户本身可以以任意顺序返回。
 * <p>
 * 链接：https://leetcode-cn.com/problems/accounts-merge
 */
public class Q721 {
    public static void main(String[] args) {
        // [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
        System.out.println(new Q721().accountsMerge(stringToListListString("[[\"John\", \"johnsmith@mail.com\", \"john00@mail.com\"], [\"John\", \"johnnybravo@mail.com\"], [\"John\", \"johnsmith@mail.com\", \"john_newyork@mail.com\"], [\"Mary\", \"mary@mail.com\"]]")));
    }

    int[] parent;
    Map<String, Integer> keyIndex = new HashMap<>();

    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        List<List<String>> ret = new ArrayList<>();
        parent = new int[accounts.size()];
        for (int i = 0; i < accounts.size(); i++) {
            parent[i] = i;
            List<String> data = accounts.get(i);
            for (int j = 1; j < data.size(); j++) {
                String key = data.get(j);
                if (keyIndex.containsKey(key)) merge(keyIndex.get(key), i);
                else keyIndex.put(key, i);
            }
        }
        HashMap<Integer, List<String>> map = new HashMap<>();
        for (Map.Entry<String, Integer> entry : keyIndex.entrySet()) {
            int root = find(entry.getValue());
            String email = entry.getKey();
            if (!map.containsKey(root)) {
                List<String> list = new ArrayList<>();
                list.add("");
                map.put(root, list);
                ret.add(list);
            }
            map.get(root).add(email);
        }
        for (List<String> l : ret) {
            Collections.sort(l);
            int ki = keyIndex.get(l.get(1));
            l.set(0, accounts.get(ki).get(0));
        }
        return ret;
    }

    void merge(int index_0, int index_1) {
        int r_0 = find(index_0), r_1 = find(index_1);
        if (r_0 != r_1) parent[r_1] = r_0;
    }

    int find(int index) {
        if (parent[index] != index) parent[index] = find(parent[index]);
        return parent[index];
    }
}
