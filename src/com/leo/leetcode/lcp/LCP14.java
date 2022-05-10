package com.leo.leetcode.lcp;

import com.leo.utils.TestCase;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。
 * 为了减少他的工作量，请求出最少可以切成多少个子数组。
 * 限制：
 * 1、1 <= nums.length <= 10^5
 * 2、2 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/qie-fen-shu-zu
 */
public class LCP14 {

    public static void main(String[] args) {
        // 2
        System.out.println(new LCP14().splitArray(stringToIntegerArray("[2,3,3,2,3,3]")));
        // 147
        System.out.println(new LCP14().splitArray(stringToIntegerArray((new TestCase("resources/LCP14/Case001.txt")).getData(0))));
        // 63
        System.out.println(new LCP14().splitArray(stringToIntegerArray("[292493,243391,6997,303689,65617,102503,243203,1571,29723,60637,92431,299447,42473,220931,12413,74177,185959,236063,27691,258611,12253,118589,122201,163027,175013,136261,254389,362581,444937,572963,391873,643373,681011,328621,359767,597209,734897,476347,617537,330839,505027,800731,629929,765353,502651,687019,434191,472159,529157,631679,343963,740671,634577,866009,857321,850189,864757,807607,847937,878797,873421,837601,830143,812341,847237,814061,872353,816091,867619,854303,856393,819239,819317,866573,864223,824591,854617,834623,869467,847009,840943,859783,855119,849301,835207,829643,873419,842339,849649,812939,851267,822739,850189,857167,885233,981091,925153,919381,904357,926131]")));
        // 4
        System.out.println(new LCP14().splitArray(stringToIntegerArray("[2,3,5,7]")));
    }

    // 质因数分解
    public int splitArray(int[] nums) {
        Map<Integer, Integer> primeMap = new HashMap<>();
        int N = 1_000_010;
        int[] primes = new int[N]; // 最大的质因数
        // 欧拉筛法 找出素数
//        List<Integer> primeList = new ArrayList<>();
//        boolean[] isNp = new boolean[N];
//        for (int i = 2; i < N; i++) {
//            if (!isNp[i]) {
//                primeList.add(i);
//                primes[i] = i;
//            }
//            for (int p : primeList) {
//                if (p * i >= N) break;
//                isNp[p * i] = true;
//                primes[p * i] = Math.max(p, primes[i]);
//                if (i % p == 0) break;
//            }
//        }
        // 埃拉托色尼筛选法，预处理每个数的最大质因子
        for (int i = 2; i < N; i++) {
            if (primes[i] == 0) {
                for (int j = i; j < N; j += i) primes[j] = i;
            }
        }
        int ret = 0;
        for (int num : nums) {
            int cur = ret + 1;
            while (num > 1) {
                int prime = primes[num];
                primeMap.put(prime, Math.min(ret + 1, primeMap.getOrDefault(prime, ret + 1)));
                cur = Math.min(cur, primeMap.get(prime));
                num /= prime;
            }
            ret = cur;
        }
        return ret;
    }

}
