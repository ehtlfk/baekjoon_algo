/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int 변수 1개 입력받는 예제
// cin >> b >> c;                       // float 변수 2개 입력받는 예제 
// cin >> d >> e >> f;                  // double 변수 3개 입력받는 예제
// cin >> g;                            // char 변수 1개 입력받는 예제
// cin >> var;                          // 문자열 1개 입력받는 예제
// cin >> AB;                           // long long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int 변수 1개 출력하는 예제
// cout << b << " " << c;               // float 변수 2개 출력하는 예제
// cout << d << " " << e << " " << f;   // double 변수 3개 출력하는 예제
// cout << g;                           // char 변수 1개 출력하는 예제
// cout << var;                         // 문자열 1개 출력하는 예제
// cout << AB;                          // long long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////

#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<cmath> 
#include<algorithm>
#define MAX 100001
using namespace std;



vector<int> vec[MAX];
int parent[MAX];
int depth[MAX];
bool visited[MAX];

void bfs(int parentNode, int currentDepth){
	queue<int> q;
	q.push(parentNode);
	while(!q.empty()){
		int qs=q.size();
		while(qs--){
			int currentNode=q.front();
			depth[currentNode]=currentDepth;
			q.pop();
			for(int nextNode : vec[currentNode]){
				if(!depth[nextNode]){
					parent[nextNode]=currentNode;
					q.push(nextNode);
				}
			}
		}
		currentDepth++;
	}
}



int main(int argc, char** argv)
{
	freopen("baekjoon_11437.txt", "r", stdin);
	int N, M;
	int K;
	cin >> N;
    
	for(int i=0; i<N-1; ++i){
		int a, b;
		cin >> a >> b;
		vec[a].push_back(b);
		vec[b].push_back(a);
	}
	K= int(log2(N-1))+1;
	cout << K << endl;
//	bfs(N,K);
	for( int i=0; i<N+1;i++) {
		cout << parent[i] << endl;
	}
	cout << endl;
		for( int i=0; i<N+1;i++) {
		cout << depth[i] << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
