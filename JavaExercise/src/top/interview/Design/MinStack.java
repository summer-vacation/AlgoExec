package top.interview.Design;

import java.util.ArrayList;
import java.util.LinkedList;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/98/design/562/
 * 实现栈
 */
public class MinStack {

    /** initialize your data structure here. */
    private ArrayList<Integer> stack;
    private int min;
    private LinkedList<Integer> sorted_stack;
    public MinStack() {
        stack = new ArrayList<>();
        min = Integer.MIN_VALUE;
    }

    public void push(int x) {
        stack.add(x);
        min(x);
    }

    public void pop(){
        stack.remove(stack.size() - 1);
        // 刚好删除的是min
    }

    public int top(){
        return stack.get(stack.size() - 1);
    }

    public void min(int x){
        if (min > x) {
            min = x;
        }
    }

    public int getMin() {
        // todo:保存有序状态，直接取最小值
        int min = Integer.MAX_VALUE;
        for(Integer n : stack){
            min = Math.min(min, n);
        }
        return min;
    }

    public static void main(String[] args) {
        try {
            MinStack obj = new MinStack();
            obj.push(3);
            obj.pop();
            int param_3 = obj.top();
            int param_4 = obj.getMin();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
