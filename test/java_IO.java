package test;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
    public static void main(String args[]) throws Exception {
   
    BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));

    String[] input = bReader.readLine().split(" ");
    int A = Integer.parseInt(input[0]);
    int B = Integer.parseInt(input[1]);

    System.out.println((A+B));

    }
}