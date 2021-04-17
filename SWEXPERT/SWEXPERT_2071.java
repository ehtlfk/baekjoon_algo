import java.util.Scanner;
import java.io.FileInputStream;

public class SWEXPERT_2071 {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("SWEXPERT/SWEXPERT_2071.txt"));
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            double sum = 0;
            for (int i = 0; i < 10; i++) {
                int a = sc.nextInt();
                sum += a;
            }
            System.out.println("#" + test_case + " " + String.format("%.0f", sum / 10));
        }
        sc.close();
    }
}
// sample code
// import java.io.BufferedReader;
// import java.io.InputStreamReader;

// class Solution {
// public static void main(String args[]) throws Exception {
// new Solution().run();
// }

// public void run() throws Exception {
// BufferedReader bReader = new BufferedReader(new
// InputStreamReader(System.in));

// int tCase = Integer.parseInt(bReader.readLine());
// for (int i = 0; i < tCase; i++) {
// int sum = 0, avg;
// String[] input;
// input = bReader.readLine().split(" ");

// for (String value : input) {
// int v = Integer.parseInt(value);
// sum += v;
// }

// avg = (sum%10 > 4)? sum/10+1:sum/10; //?? 왜 4로 나눔? 아 반올림...

// System.out.println("#" + (i + 1) + " " + avg);
// }
// }
// }

// 아니 속도가 2배 이상 빠르네...