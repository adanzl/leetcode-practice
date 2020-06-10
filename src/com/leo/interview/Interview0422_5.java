package com.leo.interview;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonArray;
import com.eclipsesource.json.JsonObject;
import com.eclipsesource.json.JsonValue;

import java.util.LinkedList;

/**
 * 【第一题】JSON格式转换 在某个特定应用场景中，我们有一个从JSON获取的内容，
 * 比如: * m = { "a": 1, "b": { "c": 2, "d": [3,4] } }
 * 现在需要把这个层级的结构做展开，只保留一层key/value结构。
 * 对于上述输入，需要得到的结构是: * o = {"a": 1, "b.c": 2, "b.d": [3,4] }
 * 也就是说，原来需要通过 m["b"]["c"] 访问的值，在展开后可以通过 o["b.c"] 访问。
 * 请实现这个“层级结构展开”的代码。
 * 输入:任意JSON(或者map/dict)
 * 输出:展开后的JSON(或者map/dict)
 */
public class Interview0422_5 {

    public static void main(String[] args) {
        System.out.println(ExpandJson(Json.parse("[{\"a\": 1}]")).toString()); // [{"a":1}]
        System.out.println(ExpandJson(Json.parse("{ \"a\": 1, \"b\": { \"c\": 2, \"d\": [3,4] } }").asObject()).toString()); // {"a":1,"b.c":2,"b.d":[3,4]}
        System.out.println(ExpandJson(Json.parse("[3,4]")).toString()); // [3,4]
        System.out.println(ExpandJson(Json.parse("3")).toString()); // 3
        System.out.println(ExpandJson(Json.parse("{ \"a\": 1, \"b\": [ {\"c\": {\"d\": 3}},4] }").asObject()).toString()); // {"a":1,"b":[{"c.d":3},4]}
    }

    static JsonValue ExpandJson(JsonValue json) {
        if (json == null) return null;
        if (json.isArray()) {
            return ExpandArray(json.asArray(), new LinkedList<>());
        } else if (json.isObject()) {
            return ExpandNode(new JsonObject(), json, new LinkedList<>());
        }

        return json;
    }

    static JsonValue ExpandNode(JsonValue out, JsonValue node, LinkedList<String> path) {
        if (node.isObject()) {
            node.asObject().forEach((member) -> {
                path.addLast(member.getName());
                if (out.isArray()) {
                    out.asArray().add(ExpandNode(new JsonObject(), member.getValue(), path));
                } else {
                    ExpandNode(out, member.getValue(), path);
                }
                path.removeLast();
            });
        } else {
            JsonValue value;
            if (node.isArray()) {
                value = ExpandArray(node.asArray(), new LinkedList<>());
            } else {
                value = node;
            }
            if (out.isArray()) {
                out.asArray().add(value);
            } else {
                StringBuilder key = new StringBuilder();
                for (String str : path) {
                    if (key.length() > 0) {
                        key.append(".");
                    }
                    key.append(str);
                }
                out.asObject().add(key.toString(), value);
            }
        }
        return out;
    }

    static JsonValue ExpandArray(JsonArray arr, LinkedList<String> path) {
        JsonArray out = new JsonArray();
        for (JsonValue jv : arr) {
            if (jv.isArray()) out.add(ExpandArray(jv.asArray(), path));
            else ExpandNode(out, jv, path);
        }
        return out;
    }
}
