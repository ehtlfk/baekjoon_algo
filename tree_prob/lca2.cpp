/////////////////////////////////////////////////////////////////////////////////////////////
// �⺻ �����ڵ�� ���� �����ص� ���� �����ϴ�. ��, ����� ���� ����
// �Ʒ� ǥ�� ����� ���� �ʿ�� �����ϼ���.
// ǥ�� �Է� ����
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int ���� 1�� �Է¹޴� ����
// cin >> b >> c;                       // float ���� 2�� �Է¹޴� ���� 
// cin >> d >> e >> f;                  // double ���� 3�� �Է¹޴� ����
// cin >> g;                            // char ���� 1�� �Է¹޴� ����
// cin >> var;                          // ���ڿ� 1�� �Է¹޴� ����
// cin >> AB;                           // long long ���� 1�� �Է¹޴� ����
/////////////////////////////////////////////////////////////////////////////////////////////
// ǥ�� ��� ����
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int ���� 1�� ����ϴ� ����
// cout << b << " " << c;               // float ���� 2�� ����ϴ� ����
// cout << d << " " << e << " " << f;   // double ���� 3�� ����ϴ� ����
// cout << g;                           // char ���� 1�� ����ϴ� ����
// cout << var;                         // ���ڿ� 1�� ����ϴ� ����
// cout << AB;                          // long long ���� 1�� ����ϴ� ����
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
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}
