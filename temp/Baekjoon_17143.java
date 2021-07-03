package temp;
// bufferedReader가 scanner보다 빠르지만, type을 바꿔줘야하는 번거로움 존재
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileInputStream;
import java.util.StringTokenizer;
import java.util.Arrays;

class Baekjoon_17143 {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("temp/baekjoon_17143.txt"));
        BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = bReader.readLine().split(" ");
        int R = Integer.parseInt(input[0]);
        int C = Integer.parseInt(input[1]);
        int M = Integer.parseInt(input[2]);

        int[][] arr = new int[M][5];
        for (int i=0; i<M; ++i) {
            StringTokenizer st = new StringTokenizer(bReader.readLine()," ");
            for (int j=0; j<5; ++j){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }   
        } 
        long answer = 0;
        

        System.out.println(Arrays.toString(arr[0]));
      
    }
}