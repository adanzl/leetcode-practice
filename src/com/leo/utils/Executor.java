package com.leo.utils;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonArray;
import com.eclipsesource.json.JsonValue;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.*;

public class Executor {

    final private Class<?> cl;

    public Executor(Class<?> cl) {
        this.cl = cl;
    }


    public void execute(String methodExp, String paramString) {
        String[] methods = stringToStringArray(methodExp);
        JsonArray paramArray = Json.parse(paramString).asArray();
        Class<?> classObj = null;
        for (Class<?> innerClazz : cl.getDeclaredClasses()) {
            String cName = innerClazz.getName();
            if (cName.substring(cName.lastIndexOf("$") + 1).equals(methods[0])) {
                classObj = innerClazz;
                break;
            }
        }
        if (null == classObj) {
            System.out.println("No class:" + methods[0]);
            return;
        }
        List<Object> ret = new ArrayList<>();
        Object obj = null;
        for (Constructor<?> c : classObj.getDeclaredConstructors()) {
            int pCount = c.getParameterCount();
            JsonArray cParamArray = paramArray.get(0).asArray();
            if (pCount != cParamArray.size()) continue;
            try {
                Object[] params = buildParams(c.getParameterTypes(), cParamArray);
                c.setAccessible(true);
                obj = c.newInstance(params);
                ret.add(null);
                break;
            } catch (Exception ignored) {
            }
        }
        if (null == obj) {
            System.out.println("Create Instance failed:" + methods[0]);
            return;
        }
        for (int i = 1; i < methods.length; i++) {
            JsonValue param = paramArray.get(i);
            String func = methods[i];
            for (Method method : classObj.getDeclaredMethods()) {
                if (method.getName().equals(func)) {
                    try {
                        Object[] params = buildParams(method.getParameterTypes(), param.asArray());
                        method.setAccessible(true);
                        Class<?> returnType = method.getReturnType();
                        Object result = method.invoke(obj, params);
                        if (returnType == int[].class) ret.add(Arrays.toString((int[]) result));
                        else if (returnType == double[].class) ret.add(Arrays.toString((double[]) result));
                        else if (returnType == String[].class) ret.add(Arrays.toString((String[]) result));
                        else if (returnType == boolean[].class) ret.add(Arrays.toString((boolean[]) result));
                        else if (returnType == TreeNode.class) ret.add(treeNodeToString((TreeNode) result));
                        else if (returnType == ListNode.class) ret.add(listNodeToString((ListNode) result));
                        else if (returnType != void.class) ret.add(result);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    break;
                }
            }
        }
        System.out.println(ret);
    }

    private Object[] buildParams(Class<?>[] types, JsonArray paramArray) {
        Object[] params = new Object[types.length];
        for (int i = 0; i < params.length; i++) {
            Class<?> pType = types[i];
            if (pType == String.class) params[i] = paramArray.get(i).asString();
            if (pType == Integer.class || pType == int.class) params[i] = paramArray.get(i).asInt();
            if (pType == Double.class || pType == double.class) params[i] = paramArray.get(i).asDouble();
            if (pType == Boolean.class || pType == boolean.class) params[i] = paramArray.get(i).asBoolean();
            if (pType == TreeNode.class) params[i] = stringToTreeNode(paramArray.get(i).toString());
            if (pType == ListNode.class) params[i] = stringToListNode(paramArray.get(i).toString());
        }
        return params;
    }

}
