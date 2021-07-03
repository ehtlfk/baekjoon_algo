package temp;
// bufferedReader가 scanner보다 빠르지만, type을 바꿔줘야하는 번거로움 존재
// 상어 위치정보 1234 : 상하우좌
// 같은 크기 상어 없음
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileInputStream;
import java.util.StringTokenizer;

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
                int num = Integer.parseInt(st.nextToken());
                if (j<2){
                    arr[i][j] = num-1;
                } else arr[i][j] = num;
            }   
        } 
        
        long answer = 0;

        int[][] map = new int[R][C];
        for (int i=0; i<arr.length; ++i) {
            map[arr[i][0]][arr[i][1]] = i+1; // 0번 상어는 안됨, s:속도, d:방향, z:크기
            // 벽꿍하면 뒤로 돌아감, 마지막 위치가 벽 앞일 경우 방향을 반대로 해서 속도만큼 이동
        }

        for (int p=0; p<C; ++p) {
            for (int r=0; r<R; ++r) {
                int sangu = map[r][p];
                if (sangu!=0) {
                    answer+=arr[sangu-1][4];
                    map[r][p] = 0;
                    arr[sangu-1] = null;
                    break; // 가장 땅에 가까운 친구
                }
            }
            // 상어 이동
            for (int j = 0; j<arr.length;++j) {
                if (arr[j] != null) {
                    map[arr[j][0]][arr[j][1]] = 0;
                    int s = arr[j][2];
                    int d = arr[j][3];
                    while (s > 0) {
                        switch (d) {
                            case 1:
                                arr[j][0]-=s%(2*R-2);                                
                                if (arr[j][0]<0) {
                                    d = 2;
                                    s = arr[j][0]*-1;
                                    arr[j][0] = 0;
                                } else s =0;
                                break;
                            case 2:
                                arr[j][0]+=s%(2*R-2);
                                if (arr[j][0]>=R) {
                                    d = 1;
                                    s = (arr[j][0]-R+1);
                                    arr[j][0] = R-1;
                                } else s = 0;
                                break;
                            case 3:
                                arr[j][1]+=s%(2*C-2);
                                if (arr[j][1]>=C) {
                                    d = 4;
                                    s = arr[j][1]-C+1;
                                    arr[j][1] = C-1;
                                } else s = 0;
                            case 4:
                                arr[j][1]-=s%(2*C-2);
                                if (arr[j][1]<0) {
                                    d = 3;
                                    s = arr[j][1]*-1;
                                    arr[j][1] = 0;
                                } else s = 0;
                        }
                    }
                    arr[j][3] = d;
                    int mx = map[arr[j][0]][arr[j][1]];
                    if ( mx == 0 ) {
                        map[arr[j][0]][arr[j][1]] = j+1;
                    } else if (mx-1 < j && arr[mx-1][4] < arr[j][4]) {
                        arr[mx-1] = null;
                        map[arr[j][0]][arr[j][1]] = j+1;
                    } else {
                        // 이미 이동이 끝난 상어가 있고 자기보다 크기가 크면 
                        arr[mx-1] = null;
                    }
                }
            }
        }
        System.out.println(answer);
      
    }
}