package top.interview.Design;

import java.util.Stack;

public class MinStack_01 {
    Stack<Integer> stack;
    Stack<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack_01() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int x) {
        stack.push(x);

        if(minStack.empty()){
            minStack.push(x);
        }else{
            int val = minStack.peek();
            if(x <= val) minStack.push(x);
            else minStack.push(val);
        }
    }

    public void pop() {
        stack.pop();
        minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}
