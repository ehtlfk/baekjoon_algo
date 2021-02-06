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
int parent[MAX][17];

void bfs(int n){
	int k;
	queue<int> q;
	q.push(1);
	while(!q.empty()){
		// queue.pop�� return ���� ���� 
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
		if(depth[currentNode]){
			k = int(log2(depth[currentNode]));
			for(int j=1;j<k+1;j++){
				parent[currentNode][j] = parent[parent[currentNode][j-1]][j-1];
			}
		}
	}
}
int lca(int n1,int n2) {
	int d1, d2, diff, k, temp1, temp2;
	bool flag;
	d1 = depth[n1];
	d2 = depth[n2];
	while (d1!=d2){
		if(d1 > d2){
			swap(d1,d2);
			swap(n1,n2);
		}
		diff = d2 - d1;
		k = int(log2(diff));
		n2 = parent[n2][k];
		d2 = depth[n2];
	}
	if (n1 == n2) {
		return n1;
	}
	else{
		while(n1!=n2){
			k = int(log2(d1));
			flag = 1;
			for(int i=1;i<k+1;++i){
				temp1 = parent[n1][i];
				temp2 = parent[n2][i];
				if (temp1 == temp2){
					flag = 0;
					n1 = parent[n1][i-1];
					n2 = parent[n2][i-1];
					d1 = depth[n1];
					d2 = depth[n2];
					break;
				}
			}
			if(flag){
				n1 = parent[n1][k];
				n2 = parent[n2][k];
				d1 = depth[n1];
				d2 = depth[n2];
			}
		}
		return n1;
	}
	
}


int main(int argc, char** argv)
{
	freopen("test.txt", "r", stdin);
	int N, M;
	cin >> N;
    
	for(int i=0; i<N-1; ++i){
		int a, b;
		cin >> a >> b;
		vec[a].push_back(b);
		vec[b].push_back(a);
	}
	bfs(N);
	cin >> M;
	for (int j=0;j<M;++j){
		int n1, n2;
		cin >> n1 >> n2;
//		cout << lca(n1,n2) << endl;
	}
	return 0;
}
