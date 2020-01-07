package top.interview.Math;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/744/
 * hint中给的
 */
public class CountPrimes {
    public int countPrimes(int n) {
        boolean[] isPrime = new boolean[n];
        // 初始化
        for (int i = 2; i < n; i++) {
            isPrime[i] = true;
        }
        // Loop's ending condition is i * i < n instead of i < sqrt(n)
        // to avoid repeatedly calling an expensive function sqrt().
        // 所有 2、3、4、5、6、7、8、9、10……的倍数全都不是质数
        for (int i = 2; i * i < n; i++) {
            if (!isPrime[i]) continue;
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(new CountPrimes().countPrimes(1000));
    }
}
