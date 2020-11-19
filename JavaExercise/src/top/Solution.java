package top;

import java.util.*;

public class Solution {
    public static int Travel(int start, int end) {
        ArrayList<Integer> uset = new ArrayList<>();
        ArrayList<Integer[]> v = new ArrayList<>();

        uset.add(start);
        v.add(new Integer[]{start / 8, start % 8});

        int level = 0;
        while (!v.isEmpty()) {
            ArrayList<Integer[]> t = new ArrayList<>();
            for (Integer[] integers : v) {
                if (integers[0] * 8 + integers[1] == end) {
                    return level;
                }
                if (!uset.contains(integers[0] * 8 + integers[1])) {
                    uset.add(integers[0] * 8 + integers[1]);
                }
                if (integers[0] - 2 >= 0 &&
                        integers[1] - 1 >= 0 &&
                        !uset.contains((integers[0] - 2) * 8 + integers[1] - 1)){
                    t.add(new Integer[]{integers[0] - 2, integers[1] - 1});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] - 2) * 8 + integers[1] - 1);
                    }
                }
                if (integers[0] - 2 >= 0 && integers[1] + 1 <= 7 && !uset.contains((integers[0] - 2) * 8 + integers[1] + 1)) {
                    t.add(new Integer[]{integers[0] - 2, integers[1] + 1});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] - 2) * 8 + integers[1] + 1);
                    }
                }
                if (integers[0] - 1 >= 0 && integers[1] - 2 >= 0 && !uset.contains((integers[0] - 1) * 8 + integers[1] - 2)) {
                    t.add(new Integer[]{integers[0] - 1, integers[1] - 2});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] - 1) * 8 + integers[1] - 2);
                    }
                }
                if (integers[0] - 1 >= 0 && integers[1] + 2 <= 7 && !uset.contains((integers[0] - 1) * 8 + integers[1] + 2)) {
                    t.add(new Integer[]{integers[0] - 1, integers[1] + 2});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] - 1) * 8 + integers[1] + 2);
                    }
                }
                if (integers[0] + 1 <= 7 && integers[1] + 2 <= 7 && !uset.contains((integers[0] + 1) * 8 + integers[1] + 2)) {
                    t.add(new Integer[]{integers[0] + 1, integers[1] + 2});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] + 1) * 8 + integers[1] + 2);
                    }
                }
                if (integers[0] + 1 <= 7 && integers[1] - 2 >= 0 && !uset.contains((integers[0] + 1) * 8 + integers[1] - 2)) {
                    t.add(new Integer[]{integers[0] + 1, integers[1] - 2});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] + 1) * 8 + integers[1] - 2);
                    }
                }
                if (integers[0] + 2 <= 7 && integers[1] + 1 <= 7 && !uset.contains((integers[0] + 2) * 8 + integers[1] + 1)) {
                    t.add(new Integer[]{integers[0] + 2, integers[1] + 1});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] + 2) * 8 + integers[1] + 1);
                    }
                }
                if (integers[0] + 2 <= 7 && integers[1] - 1 >= 0 && !uset.contains((integers[0] + 2) * 8 + integers[1] - 1)) {
                    t.add(new Integer[]{integers[0] + 2, integers[1] - 1});
                    if (!uset.contains((integers[0] - 2) * 8 + integers[1] - 1)) {
                        uset.add((integers[0] + 2) * 8 + integers[1] - 1);
                    }
                }
            }
            v = t;
            level++;
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(Solution.Travel(0, 1));
        System.out.println(Solution.Travel(19, 36));
    }
}
