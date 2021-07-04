package temp;
//백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 
//그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 
//그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 
//택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 
//연료는 한 칸 이동할 때마다 1만큼 소모된다. 
//한 승객을 목적지로 성공적으로 이동시키면, 
//그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 
//이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. 
//승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
//그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 
//모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.
// 출발지는 다르지만 도착지가 같을 수도 있는건가?

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileInputStream;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class Baekjoon_19238 {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("temp/baekjoon_19238.txt"));

        BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));

        String[] input = bReader.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int F = Integer.parseInt(input[2]);

        int[][] map = new int[N][N];
        for (int i=0; i<N; ++i) {
            StringTokenizer st = new StringTokenizer(bReader.readLine()," ");
            for (int j=0; j<N; ++j){
                map[i][j] = Integer.parseInt(st.nextToken());
            }   
        }
        
        
        String[] startP = bReader.readLine().split(" ");
        int[] start = new int[2];
        start[0] = Integer.parseInt(startP[0])-1;
        start[1] = Integer.parseInt(startP[1])-1;

        int[][] arr = new int[M][4];
        for (int i=0; i<M; ++i) {
            StringTokenizer st = new StringTokenizer(bReader.readLine()," ");
            for (int j=0; j<4; ++j){
                arr[i][j] = Integer.parseInt(st.nextToken())-1;
            }
            map[arr[i][0]][arr[i][1]] = i+2;
            // map[arr[i][2]][arr[i][3]] = -(i+2);   
        }
        
        int[] ret;
        int fx,fy;
        while (M>0) {
            ret = bfs(start, map, arr,-1,-1,F);
            if (ret[0]!=-1) {
                F -= ret[0];
                start[0] = ret[1];
                start[1] = ret[2];
                fx = arr[ret[3]-2][2];
                fy = arr[ret[3]-2][3];
                ret = bfs(start, map, arr, fx,fy,F);
                if (ret[0]!=-1){
                    start[0] = ret[1];
                    start[1] = ret[2];
                    F += ret[0];
                    M--;
                } else break;
            } else break;
        }
        if (M == 0 ){
            System.out.println(F);
        } else System.out.println(-1);
    }

    public static int[] bfs(int[] start, int[][] map, int[][] arr, int fx, int fy, int F) {
        Queue<int[]> q = new LinkedList<>();
        int x,y,nx,ny;
        int[] tmp;
        int[] ret = new int[4];
        int[] dx = {-1,0,0,1};
        int[] dy = {0,-1,1,0};

        int[][] v = new int[map.length][map.length];
        q.add(start);

        while (!q.isEmpty()) {
            tmp = q.poll();
            x = tmp[0];
            y = tmp[1];
            if (fx == -1 && map[x][y] > 1 ) {
                if (F < v[x][y]){
                    ret[0] = -1;
                    return ret;
                }
                ret[0]=v[x][y];
                ret[1] = x;
                ret[2] = y;
                ret[3] = map[x][y];
                map[x][y] = 0;
                return ret;
            }
            else if ( x==fx && y == fy) {
                if (F < v[x][y]){
                    ret[0] = -1;
                    return ret;
                }
                ret[0]=v[x][y];
                ret[1] = x;
                ret[2] = y;
                return ret;
            }

            for (int k=0; k<4;k++){
                nx = x + dx[k];
                ny = y + dy[k];
                if (0<=nx && nx<map.length && 0<=ny && ny<map.length && map[nx][ny]!=1 && v[nx][ny]==0) {
                    int[] nxy = new int[2];
                    nxy[0] = nx;
                    nxy[1] = ny;
                    q.add(nxy);
                    v[nx][ny] = v[x][y]+1;
                    if (fx == -1 && map[nx][ny] > 1 ) {
                        if (F < v[nx][ny]){
                            ret[0] = -1;
                            return ret;
                        }
                        ret[0]=v[nx][ny];
                        ret[1] = nx;
                        ret[2] = ny;
                        ret[3] = map[nx][ny];
                        map[nx][ny] = 0;
                        return ret;
                    }
                    else if ( nx==fx && ny == fy) {
                        if (F < v[nx][ny]){
                            ret[0] = -1;
                            return ret;
                        }
                        ret[0]=v[nx][ny];
                        ret[1] = nx;
                        ret[2] = ny;
                        return ret;
                    }
                }
            }
        }
        ret[0] = -1;
        return ret;
    }
}
