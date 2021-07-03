package temp;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileInputStream;


class Baekjoon_17143 {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("temp/baekjoon_17143.txt"));
        BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = bReader.readLine().split(" ");
        int R = Integer.parseInt(input[0]);
        int C = Integer.parseInt(input[1]);
        int M = Integer.parseInt(input[2]);
        for (int i=0; i<M; ++i) {
            String[] sangu = bReader.readLine().split(" ");
        } 
        long answer = 0;
        

        System.out.println(R);
      
    }
}