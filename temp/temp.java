import java.util.Arrays;

class Solution {
    public int solution(int[] prices, int[] discounts) {
        int answer = 0;
        Arrays.sort(prices);
        Arrays.sort(discounts);
        int pl = prices.length-1;
        int dl = discounts.length-1;
        for (int i=0;i<prices.length;i++){
            if (dl-i <0) {
                answer += prices[pl-i];
            } else answer+= (prices[pl-i]*(100-discounts[dl-i])/100);
        }
        
        return answer;
    }
}