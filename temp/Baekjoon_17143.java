package temp;
// bufferedReader가 scanner보다 빠르지만, type을 바꿔줘야하는 번거로움 존재
// 상어 위치정보 1234 : 상하우좌
// 같은 크기 상어 없음
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

        int[][] map = new int[R][C];
        for (int i=0; i<arr.length; ++i) {
            map[arr[i][0]-1][arr[i][1]-1] = i+1; // 0번 상어는 안됨, s:속도, d:방향, z:크기
            // 벽꿍하면 뒤로 돌아감, 마지막 위치가 벽 앞일 경우 방향을 반대로 해서 속도만큼 이동
        }

        for (int p=0; p<C; ++p) {
            for (int r=0; r<R; ++r) {
                int sangu = map[p][r]-1;
                if (sangu!=-1) {
                    answer+=arr[sangu][4];
                    map[p][r] = 0;
                    arr[sangu] = null;
                }
            }
            // 상어 이동
            for (int j = 0; j<arr.length;++j) {
                if (arr[j] != null) {
                    int s = arr[j][2];
                    int d = arr[j][3];
                    while (0<=arr[j][0] && arr[j][0]<R && 0<= arr[j][1] && arr[j][1]<C){
                        switch (d) {
                            case 1: 
                                arr[j][0]-=s%(2*R-2);
                                if (arr[j][0]<0){
                                    d = 2;
                                    s = arr[j][0]*-1;
                                }
                                break;
                            case 2:
                                arr[j][0]+=s%(2*R-2);
                                if (arr[j][0]>=R) {
                                    d = 1;
                                }
                                break;
                        }
                    }
                    
                }
            }
        }

        
        

        System.out.println(Arrays.toString(arr[0]));
      
    }
}