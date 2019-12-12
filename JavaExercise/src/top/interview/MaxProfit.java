package top.interview;

/***
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/572/
 *
 * 找到最佳买卖股票的十几人，只允许交易一次
 */
public class MaxProfit {
    public MaxProfit(){

    }
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0){
            return 0;
        } else{
            int maxProfit = 0;
            int min = prices[0];
            int n = prices.length;
            for (int i = 1; i < n; i++){
                maxProfit = Math.max(maxProfit, prices[i] - min);
                if (prices[i] < min){
                    min = prices[i];
                }
            }
            return maxProfit;
        }
    }

    public static void main(String[] args) {
        int[] inout = new int[]{7,1,5,3,6,4};
        System.out.println(new MaxProfit().maxProfit(inout));
    }
}
