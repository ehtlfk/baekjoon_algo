#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<cmath> 
#include<algorithm>
#define MAX 100001
using namespace std;



vector<int> vec[MAX];
int depth[MAX];
bool visited[MAX];
int parent[MAX][18];

void bfs(int n){
	int k;
	queue<int> q;
	q.push(1);
	while(!q.empty()){
		int currentNode=q.front(); 
		visited[currentNode] = 1;
		q.pop();
		for(int nextNode : vec[currentNode]){
			if(!visited[nextNode]){
				parent[nextNode][0]=currentNode;
				q.push(nextNode);
				depth[nextNode] = depth[currentNode] + 1;
			}
		}
//		if(depth[currentNode]){
//			k = int(log2(depth[currentNode]));
//			for(int j=1;j<k+1;j++){
//				parent[currentNode][j] = parent[parent[currentNode][j-1]][j-1];
//			}
//		}
	}
}


void dfs(int parentNode, int currentDepth){
	depth[parentNode]=currentDepth;
	visited[parentNode] = 1;
	for(int nextNode : vec[parentNode]){
		if(!visited[nextNode]) {
			parent[nextNode][0]=parentNode;
			dfs(nextNode, currentDepth+1);	
		}
	}
}
int lca(int n1,int n2) {
	
	
}


int main(int argc, char** argv)
{
//	freopen("test.txt", "r", stdin);
	freopen("baekjoon_11437.txt", "r", stdin);
	ios_base::sync_with_stdio(false); cout.tie(NULL);cin.tie(NULL); // input �������� ^^^^^^^^% 
	int N, M;
	cin >> N;
    
	for(int i=0; i<N-1; ++i){
		int a, b;
		cin >> a >> b;
		vec[a].push_back(b);
		vec[b].push_back(a);
	}
	bfs(N);
//	dfs(1,0);
	
	for(int i=1;i<18;i++){
		for(int j=1;j<N+1;j++){
			parent[j][i] = parent[parent[j][i-1]][i-1];
		}
	}
	
	
	cin >> M;
	for (int j=0;j<M;++j){
		int n1, n2;
		cin >> n1 >> n2;
		int diff, k;
		if(depth[n1] > depth[n2]){
				swap(n1,n2);
		}
		diff = depth[n2] - depth[n1];
		int a=0;
		while (diff){
			if(diff%2) {
				n2 = parent[n2][a];
			}		
			a++;
			diff/=2;	
		}
		if (n1 == n2) {
			cout << n1 << '\n';
		}
		else{
			// 이 부분이 핵심 가장 중요; 위에서부터 내려와야 더빠름
			k = int(log2(depth[n1]));
			for(int i=k;i>-1;i--){
				if ( parent[n1][i] != parent[n2][i]){
					n1 = parent[n1][i];
					n2 = parent[n2][i];
				}
			}
			cout << parent[n1][0] << '\n';
		}	
	}
	
	return 0;
}
