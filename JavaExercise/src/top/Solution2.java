package top;


public class Solution2 {
    public static int solution(int n) {
        int least = getLeastCase(n);
        int most = getMostCase(n);

        return least - most;
    }

    // 斐波那契数列前 x 项和小于等于n， 求x
    public static int getLeastCase(int n) {
        if(n==0)return 0;
        if(n==1)return 1;
        if(n==2)return 2;

        int[] v = new int [n+1];
        v[0] = 0;
        v[1] = 1;

        for (int i = 2; i <= n; i++) {
            v[i] = v[i - 1] + v[i - 2];
        }

        int index = 0;
        int sum = 0;
        while (true) {
            sum += v[index];
            if (sum > n) {
                return index - 1;
            }
            index++;
        }
    }

    // 等比数列前 x 项和小于等于n， 求x
    // S(x) = pow(2, x) -1
    public static int getMostCase(int n) {
        if (n <= 0) {
            return 0;
        }
        double x = Math.log(n + 1)/Math.log(2);
        return (int)x;
    }

    public static void main(String[] args) {
        System.out.println(Solution2.solution(1002));
    }
}
