package com.leo.leetcode.algorithm.q0600;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerList;
import static com.leo.utils.LCUtil.stringToListListInt;

/**
 * 在 LeetCode 商店中， 有 n 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
 * 给你一个整数数组 price 表示物品价格，其中 price[i] 是第 i 件物品的价格。另有一个整数数组 needs 表示购物清单，其中 needs[i] 是需要购买第 i 件物品的数量。
 * 还有一个数组 special 表示大礼包，special[i] 的长度为 n + 1 ，其中 special[i][j] 表示第 i 个大礼包中内含第 j 件物品的数量，且 special[i][n] （也就是数组中的最后一个整数）为第 i 个大礼包的价格。
 * 返回 确切 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。
 * 提示：
 * 1、n == price.length
 * 2、n == needs.length
 * 3、1 <= n <= 6
 * 4、0 <= price[i] <= 10
 * 5、0 <= needs[i] <= 10
 * 6、1 <= special.length <= 100
 * 7、special[i].length == n + 1
 * 8、0 <= special[i][j] <= 50
 * 链接：https://leetcode.cn/problems/shopping-offers
 */
public class Q638 {

    public static void main(String[] args) {
        // 14
        System.out.println(new Q638().shoppingOffers(stringToIntegerList("[2,5]"), stringToListListInt("[[3,0,5],[1,2,10]]"), stringToIntegerList("[3,2]")));
        // 11
        System.out.println(new Q638().shoppingOffers(stringToIntegerList("[2,3,4]"), stringToListListInt("[[1,1,0,4],[2,2,1,9]]"), stringToIntegerList("[1,2,1]")));
    }

    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        int n = price.size();
        List<List<Integer>> sp = new ArrayList<>();
        for (List<Integer> s : special) {
            int sum = 0;
            for (int i = 0; i < n; i++) sum += s.get(i) * price.get(i);
            if (sum > s.get(n)) sp.add(s);
        }
        return dfs(price, sp, needs, new HashMap<>());
    }

    int dfs(List<Integer> price, List<List<Integer>> special, List<Integer> needs, Map<String, Integer> mMap) {
        StringBuilder sign = new StringBuilder();
        for (int n : needs) sign.append(n).append("_");
        String key = sign.toString();
        if (!mMap.containsKey(key)) {
            int min = 0x3f3f3f3f;
            out:
            for (List<Integer> sp : special) {
                List<Integer> newNeeds = new ArrayList<>();
                for (int i = 0; i < sp.size() - 1; i++) {
                    if (needs.get(i) < sp.get(i)) continue out;
                    newNeeds.add(needs.get(i) - sp.get(i));
                }
                min = Math.min(min, dfs(price, special, newNeeds, mMap) + sp.get(sp.size() - 1));
            }
            int sum = 0;
            for (int i = 0; i < needs.size(); i++) sum += price.get(i) * needs.get(i);
            min = Math.min(min, sum);
            mMap.put(key, min);
        }
        return mMap.get(key);
    }
}
