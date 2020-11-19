package top.interview.Trees;

public class test_stack {

    public int fun1(int x){
        return fun2(x);
    }

    public int fun2(int x){
        return x/0;
    }

    public static void main(String[] args) {
        new test_stack().fun1(10);
    }
}
