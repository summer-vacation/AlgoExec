public class test extends abstracttets implements interfacetest{

    public static void main(String[] args) {
        System.out.println("5" + 3);
        System.out.println(("5" + 3).getClass().toString());
        new test().open();
        new test().test1();
        test2();
    }

    @Override
    public boolean open() {
        System.out.println(new test().a);
        return false;
    }

    @Override
    int test1() {
        System.out.println(new test().aa);
        return 0;
    }
}
