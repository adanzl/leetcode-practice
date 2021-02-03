package com.leo.leetcode.algorithm.q0100;

public class Q190 {

    public static void main(String[] args) {
        // 00111001011110000010100101000000
        System.out.println(Integer.toBinaryString(new Q190().reverseBits(Integer.valueOf("00000010100101000001111010011100", 2))));
        // 10111111111111111111111111111111
//        System.out.println(Integer.toBinaryString(new Q190().reverseBits(Integer.valueOf("11111111111111111111111111111101", 2))));
    }

    public int reverseBits(int n) {
        int ret = 0, c = 30, sign = n < 0? 1: 0;
        while(c-- >= 0) {
            ret = (ret | (n & 1)) << 1;
            if(n!=0)n >>= 1;
        }
        return ret + sign;
    }
}
