// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.io.FileInputStream;
// import java.util.List;
// import java.util.Collections;
// import java.util.Arrays;

// public class SWEXPERT_1859 {
//     public static void main(String args[]) throws Exception {
//         System.setIn(new FileInputStream("SWEXPERT/SWEXPERT_1859.txt"));

//         BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));
//         int T;
//         T = Integer.parseInt(bReader.readLine());

//         for (int test_case = 1; test_case <= T; test_case++) {
//             int N = Integer.parseInt(bReader.readLine());
//             String[] input = bReader.readLine().split(" ");
//             int answer = money(-1, N, 0, 0, 0, input);
//             System.out.println("#" + test_case + " " + answer);
//         }
//     }

//     public static int money(int k, int N, int tot, int cnt, int tmp, String[] input) {
//         if (k == N - 1) {
//             tot += Integer.parseInt(input[k]) * cnt - tmp;
//             return tot;
//         } else {
//             k += 1;
//             int change = tot + Integer.parseInt(input[k]) * cnt - tmp;
//             // List<Integer> numbers = List.of(money(k, N, tot, cnt, tmp, input),
//             // money(k, N, tot, cnt + 1, tmp + Integer.parseInt(input[k]), input),
//             // money(k, N, change, 0, 0, input), money(k, N, change, 1,
//             // Integer.parseInt(input[k]), input));
//             int[] numbers = { money(k, N, tot, cnt, tmp, input),
//                     money(k, N, tot, cnt + 1, tmp + Integer.parseInt(input[k]), input),
//                     money(k, N, change, 0, 0, input), money(k, N, change, 1, Integer.parseInt(input[k]), input) };
//             // return numbers.isEmpty() ? -1 : Collections.max(numbers);
//             Arrays.sort(numbers);
//             return numbers[numbers.length - 1];
//         }

//     }
// }

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileInputStream;

class Solution {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("SWEXPERT/SWEXPERT_1859.txt"));
        BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));
        int T;
        T = Integer.parseInt(bReader.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = Integer.parseInt(bReader.readLine());
            String[] input = bReader.readLine().split(" ");
            long answer = 0;
            int mx = Integer.parseInt(input[input.length - 1]);
            for (int i = input.length - 1; i > 0; i--) {
                if (Integer.parseInt(input[i - 1]) > mx) {
                    mx = Integer.parseInt(input[i - 1]);
                } else {
                    answer += (mx - Integer.parseInt(input[i - 1]));
                }
            }
            System.out.println("#" + test_case + " " + answer);
        }
    }
}