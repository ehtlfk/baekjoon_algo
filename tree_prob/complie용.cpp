#include<iostream>
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

	}
}





int main(int argc, char** argv)
{
//    ios_base::sync_with_stdio(false); cout.tie(NULL);cin.tie(NULL);
//	freopen("test.txt", "r", stdin);

	freopen("baekjoon_11437.txt", "r", stdin);	
	int N, M;
	cin >> N;
    
	for(int i=0; i<N-1; ++i){
		int a, b;
		cin >> a >> b;
		vec[a].push_back(b);
		vec[b].push_back(a);
	}
	bfs(N);

	
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
	    while (depth[n1]!=depth[n2]){
		    if(depth[n1] > depth[n2]){
			    swap(n1,n2);
		     }
		diff = depth[n2] - depth[n1];
		k = int(log2(diff));
		n2 = parent[n2][k];
	    }
	    if (n1 == n2) {
		    cout <<  n1 << '\n';
	    }
	    else{
	    	
	    	while(n1!=n2){
                int flag = 1;
	    		k = int(log2(depth[n1]));
			    for(int i=0;i<k+1;i++){
				    if ( parent[n1][i] == parent[n2][i]){
					    n1 = parent[n1][i-1];
					    n2 = parent[n2][i-1];
                        flag = 0;
					    break;
                    flag = i;
				}
                if(flag){
                    n1 = parent[n1][flag];
					n2 = parent[n2][flag];
                }

			} 
		    
		}
		cout << n1 << '\n';
	}
}
	return 0;
}
