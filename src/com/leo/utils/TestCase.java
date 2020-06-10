package com.leo.utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class TestCase {

    private final List<String> data = new ArrayList<>();

    public TestCase(String path) {
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(path));
            System.out.println("Reading the file using readLine() method: ");
            String contentLine;
            while ((contentLine = br.readLine()) != null) {
                data.add(contentLine);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (br != null) {
                    br.close();
                }
            } catch (IOException e) {
                System.out.println("Error in closing the BufferedReader");
            }
        }
    }

    public String getData(int lenNum) {
        if (lenNum > data.size()) {
            System.out.println("No data for num: " + lenNum);
            return "";
        }
        return this.data.get(lenNum);
    }
}

