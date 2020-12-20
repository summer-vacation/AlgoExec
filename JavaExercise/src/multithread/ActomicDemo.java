package multithread;

import java.util.concurrent.atomic.AtomicIntegerArray;

class AtomicDemo {

    private int[] value = new int[]{0, 1, 2};
    private AtomicIntegerArray mAtomicIntegerArray = new AtomicIntegerArray(value);

    private void doAdd() {
        for (int i = 0; i < 5; i++) {
            int value = mAtomicIntegerArray.addAndGet(0, 1);
            System.out.println(Thread.currentThread().getName() + "--->" + value);
        }
    }

    public static void main(String[] args) {
        AtomicDemo demo = new AtomicDemo();
        new Thread(demo::doAdd, "线程1").start();
        new Thread(demo::doAdd, "线程2").start();
    }
}
