package com.leo.leetcode.algorithm.q0400;

/**
 * 给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的 IP 地址，返回 "Neither" 。
 * 有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中 0 <= xi <= 255 且 xi 不能包含 前导零。
 * 例如: “192.168.1.1” 、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “192.168@1.1” 为无效IPv4地址。
 * 一个有效的IPv6地址 是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中:
 * 1、1 <= xi.length <= 4
 * 2、xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。
 * 3、在 xi 中允许前导零。
 * 例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7334" 是有效的 IPv6 地址，而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 是无效的 IPv6 地址。
 * 提示：queryIP 仅由英文字母，数字，字符 '.' 和 ':' 组成。
 * 链接：https://leetcode.cn/problems/validate-ip-address
 */
public class Q468 {

    public static void main(String[] args) {
        // "IPv4"
        System.out.println(new Q468().validIPAddress("172.16.254.1"));
        // "IPv6"
        System.out.println(new Q468().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"));
        // "Neither"
        System.out.println(new Q468().validIPAddress("256.256.256.256"));
    }

    public String validIPAddress(String IP) {
        String[] IP4Arr = IP.split("\\.", -1);
        if (IP4Arr.length == 4) return isIP4Arr(IP4Arr);
        String[] IP6Arr = IP.split(":", -1);
        if (IP6Arr.length == 8) return isIP6Arr(IP6Arr);
        return "Neither";
    }

    public String isIP4Arr(String[] IP4Arr) {
        for (String ip : IP4Arr) {
            if (ip.length() > 3 || ip.length() <= 0) return "Neither";
            for (int i = 0; i < ip.length(); ++i) {
                if (!Character.isDigit(ip.charAt(i))) return "Neither";
            }
            int num = Integer.parseInt(ip);
            if (num > 255 || String.valueOf(num).length() != ip.length()) return "Neither";
        }
        return "IPv4";
    }

    public String isIP6Arr(String[] IP6Arr) {
        for (String ip : IP6Arr) {
            if (ip.length() > 4 || ip.length() <= 0) return "Neither";
            for (int i = 0; i < ip.length(); ++i) {
                char c = ip.charAt(i);
                if (!Character.isDigit(c) && !('a' <= c && c <= 'f') && !('A' <= c && c <= 'F')) {
                    return "Neither";
                }
            }
        }
        return "IPv6";
    }
}
