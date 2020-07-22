package com.leo.interview;

/**
 * 【第二题】数据存取 我们的程序运行过程中用到了一个数组a，数组元素是一个map/dict。 数组元素的“键”和“值”都是字符串类型。在不同的语言中，
 * 对应的类型是: PHP的array, Java的HashMap, C++的std::map, Objective-C的NSDictionary,
 * Swift的Dictionary, Python的dict, JavaScript的object, 等等 示例:
 * a[0]["key1"]="value1" a[0]["key2"]="value2" a[1]["keyA"]="valueA" ...
 * 为了方便保存和加载，我们使用了一个基于文本的存储结构，数组元素每行一个:
 * text="key1=value1;key2=value2\nkeyA=valueA\n..." 要求:请实现一个“保存”函数、一个“加载”函数。
 * text=store(a); //把数组保存到一个文本字符串中 a=load(text); //把文本字符串中的内容读取为数组
 * 必须严格按照上述的“每行一个、key=value”的格式保存。
 */
public class Interview0422_6 {

    static final String CODE = "UTF-8";

    // public static void main(String[] args) {
    //     int arrSize = 2;
    //     int keyCount = 3;
    //     HashMap[] maps = new HashMap[arrSize];
    //     for (int i = 0; i < maps.length; i++) {
    //         maps[i] = new HashMap<String, String>();
    //     for (int j = 0; j < keyCount; j++) {
    //         maps[i].put("key=" + i + ";" + j, "值" + i + "=" + j);
    //     }
    // }
    // ng str = Store(maps);
    // em.out.println(str);
    // oad(str);
    // em.out.println(Store(maps));
    // 
 
    // ic String Store(Map<String, String>[] maps) {
    // StringBuilder out = new StringBuilder();
    // for (Map<String, String> m : maps) {
    //         for (Map.Entry<String, String> entry : m.entrySet()) {
    //             try {
    //                 out.append(URLEncoder.encode(entry.getKey(), CODE)).append("=");
    //             out.append(URLEncoder.encode(entry.getValue(), CODE)).append(";");
    //         } catch (java.io.UnsupportedEncodingException e) {
    //         e.printStackTrace();
    // }
    // 
    // nd("\n");
    // 
    // oString();
    // 
 
    // ashMap[] Load(String str) {
    // String[] lines = str.split("\n");
    // HashMap<String, String>[] out = new HashMap[lines.length];
    //     for (int i = 0; i < lines.length; i++) {
    //         out[i] = new HashMap<>();
    //         String[] values = lines[i].split(";");
    //     for (String pair : values) {
    //         String[] p = pair.split("=");
    //         try {
    //         out[i].put(URLDecoder.decode(p[0], CODE), URLDecoder.decode(p[1], CODE));
    //     } catch (java.io.UnsupportedEncodingException e) {
    //         e.printStackTrace();
    // }
    // 
    // 
 
    // 
    // 
} 
  