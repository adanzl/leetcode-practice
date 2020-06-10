package com.leo.interview;

public class SingleInstance {

    static private volatile SingleInstance _instance;

    private final int value = 0;

    private SingleInstance() {
    }

    static public SingleInstance getInstance() {
        if (_instance == null) {
            synchronized (SingleInstance.class) {
                if (_instance == null) {
                    _instance = new SingleInstance();
                }
            }
        }
        return _instance;
    }

    public static void main(String[] args) {
        System.out.println(SingleInstance.getInstance().value);
    }
}
