import java.util.Scanner;
import java.io.FileInputStream;

public class SWEXPERT_2072 {
    public static void main(String args[]) throws Exception {

        System.setIn(new FileInputStream("SWEXPERT/SWEXPERT_2072.txt"));
        // System.out.println("Working Directory = " + System.getProperty("user.dir"));
        // => working directory = algo_prob
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int[] arr = new int[10];
            for (int i = 0; i < arr.length; i++) {
                arr[i] = sc.nextInt();
            }
            int sum = 0;
            for (int j = 0; j < arr.length; j++) {
                if (arr[j] % 2 == 1) {
                    sum += arr[j];
                }
            }
            System.out.println("#" + test_case + " " + sum);
        }
        sc.close();
    }
}