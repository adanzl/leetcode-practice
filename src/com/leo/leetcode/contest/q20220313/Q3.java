package com.leo.leetcode.contest.q20220313;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 某公司计划推出一批投资项目。 product[i] = price 表示第 i 个理财项目的投资金额 price 。客户在按需投资时，需要遵循以下规则：
 * 1、客户在首次对项目 product[i] 投资时，需要投入金额 price
 * 2、对已完成首次投资的项目 product[i] 可继续追加投入，但追加投入的金额需小于上一次对该项目的投入(追加投入为大于 0 的整数)
 * 3、为控制市场稳定，每人交易次数不得大于 limit。(首次投资和追加投入均记作 1 次交易)
 * 若对所有理财项目中最多进行 limit 次交易，使得投入金额总和最大，请返回这个最大值的总和。
 * 注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
 * 提示：
 * 1、1 <= product.length <= 10^5
 * 2、1 <= product[i] <= 10^7
 * 3、1 <= limit <= 10^9
 * 链接：https://leetcode.cn/contest/cnunionpay-2022spring/problems/I4mOGz/
 */
public class Q3 {

    public static void main(String[] args) {
        // 834376211
        System.out.println(new Q3().maxInvestment(stringToIntegerArray("[43877,10848,10442,48132,83395,71523,60275,39527]"), 345056));
        // 26
        System.out.println(new Q3().maxInvestment(stringToIntegerArray("[4,5,3]"), 8));
        // 10
        System.out.println(new Q3().maxInvestment(stringToIntegerArray("[2,1,3]"), 20));
    }

    public int maxInvestment(int[] product, int limit) {
        int max = 0, MOD = 1_000_000_007;
        long ret = 0;
        for (int p : product) max = Math.max(max, p);
        int l = 1, r = max, price = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long sum = 0;
            for (int p : product) {
                if (p < mid) continue;
                sum += p - mid + 1;
                if (sum > limit) break;
            }
            if (sum > limit) {
                l = mid + 1;
                price = mid;
            } else {
                r = mid - 1;
            }
        }
        price++;
        int cnt = 0;
        for (int p : product) {
            if (p < price) continue;
            int n = p - price + 1;
            cnt += n;
            ret = (ret + (long) (p + price) * n / 2) % MOD;
        }
        ret = (ret + (long) (limit - cnt) * (price - 1)) % MOD;
        return (int) ret;
    }
}
