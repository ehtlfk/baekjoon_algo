#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<cmath> 
#include<algorithm>

using namespace std;

bool visited[51][51];
int dx[8] = {0,0,-1,1,1,-1,1,-1};
int dy[8] = {1,-1,0,0,1,-1,-1,1};
int mat[51][51];
int W,H,cnt;
void dfs(int x, int y){
	visited[x][y] = true;
	for(int k=0;k<8;k++) { 
		int nx = dx[k]+x;
		int ny = dy[k]+y;
		if(0<=nx && nx<H && 0<=ny && ny<W && mat[nx][ny]==1 && visited[nx][ny] == false) {
			dfs(nx,ny);	
		}
	}
}

int main(int argc, char** argv)
{


	ios_base::sync_with_stdio(false); cout.tie(NULL);cin.tie(NULL); // input ???????? ^^^^^^^^% 
	while (true){
		cin >> W >> H;
		cnt =0;
    	if (W == 0 and H ==0){
    		break;
		}
		for(int i=0;i<50;i++)
            for(int j=0;j<50;j++)
                visited[i][j]=false;
		for(int i=0;i<H;i++)
            for(int j=0;j<W;j++)
                cin >> mat[i][j];
		for(int i=0;i<H;i++)
        {
            for(int j=0;j<W;j++)
            {
                if(visited[i][j]==false&&mat[i][j]==1)
                {
                    dfs(i,j);
                    cnt++;
                }
            }
        }
		cout << cnt << "\n";
	}
		
	return 0;
}
