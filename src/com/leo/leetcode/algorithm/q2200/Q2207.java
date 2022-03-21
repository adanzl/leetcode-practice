package com.leo.leetcode.algorithm.q2200;

/**
 * 给你一个下标从 0 开始的字符串 text 和另一个下标从 0 开始且长度为 2 的字符串 pattern ，两者都只包含小写英文字母。
 * 你可以在 text 中任意位置插入 一个 字符，这个插入的字符必须是 pattern[0] 或者 pattern[1] 。注意，这个字符可以插入在 text 开头或者结尾的位置。
 * 请你返回插入一个字符后，text 中最多包含多少个等于 pattern 的 子序列 。
 * 子序列 指的是将一个字符串删除若干个字符后（也可以不删除），剩余字符保持原本顺序得到的字符串。
 * 提示：
 * 1、1 <= text.length <= 10^5
 * 2、pattern.length == 2
 * 3、text 和 pattern 都只包含小写英文字母。
 * 链接：https://leetcode-cn.com/problems/maximize-number-of-subsequences-in-a-string
 */
public class Q2207 {

    public static void main(String[] args) {
        // 496
        System.out.println(new Q2207().maximumSubsequenceCount("vnedkpkkyxelxqptfwuzcjhqmwagvrglkeivowvbjdoyydnjrqrqejoyptzoklaxcjxbrrfmpdxckfjzahparhpanwqfjrpbslsyiwbldnpjqishlsuagevjmiyktgofvnyncizswldwnngnkifmaxbmospdeslxirofgqouaapfgltgqxdhurxljcepdpndqqgfwkfiqrwuwxfamciyweehktaegynfumwnhrgrhcluenpnoieqdivznrjljcotysnlylyswvdlkgsvrotavnkifwmnvgagjykxgwaimavqsxuitknmbxppgzfwtjdvegapcplreokicxcsbdrsyfpustpxxssnouifkypwqrywprjlyddrggkcglbgcrbihgpxxosmejchmzkydhquevpschkpyulqxgduqkqgwnsowxrmgqbmltrltzqmmpjilpfxocflpkwithsjlljxdygfvstvwqsyxlkknmgpppupgjvfgmxnwmvrfuwcrsadomyddazlonjyjdeswwznkaeaasyvurpgyvjsiltiykwquesfjmuswjlrphsdthmuqkrhynmqnfqdlwnwesdmiiqvcpingbcgcsvqmsmskesrajqwmgtdoktreqssutpudfykriqhblntfabspbeddpdkownehqszbmddizdgtqmobirwbopmoqzwydnpqnvkwadajbecmajilzkfwjnpfyamudpppuxhlcngkign"
                , "rr"));
        // 3
        System.out.println(new Q2207().maximumSubsequenceCount("fwymvreuftzgrcrxczjacqovduqaiigy", "yy"));
        // 1
        System.out.println(new Q2207().maximumSubsequenceCount("fwymvreuftzgrcrxczjacqovduqaiig", "yy"));
        // 4
        System.out.println(new Q2207().maximumSubsequenceCount("abdcdbc", "ac"));
        // 6
        System.out.println(new Q2207().maximumSubsequenceCount("aabb", "ab"));
    }

    public long maximumSubsequenceCount(String text, String pattern) {
        char c1 = pattern.charAt(0), c2 = pattern.charAt(1);
        int count0 = 0, count1 = 0;
        long ret = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == c1) count0++;
            if (text.charAt(i) == c2) {
                count1++;
                ret += count0;
            }
        }
        return (c1 == c2 ? 0 : Math.max(count0, count1)) + ret;
    }
}
