package com.leo.interview;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class QHW {
    // 1970-1-1 1970-1-3 1970-1-5
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {
            String line = in.nextLine();
            try {
                SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
                Date start = sdf.parse(line);
                if (!sdf.format(start).equals(line)) {
                    System.out.println("Invalid input");
                    continue;
                }
                long time = (start.getTime() - sdf.parse("1970-1-1").getTime()) / (1000 * 24 * 60 * 60);
                long p = time % 5;
                if (p < 3) {
                    System.out.println("He is working");
                } else {
                    System.out.println("He is having a rest");
                }

            } catch (ParseException e) {
                System.out.println("Invalid input");
            }
        }
        in.close();
    }

}
