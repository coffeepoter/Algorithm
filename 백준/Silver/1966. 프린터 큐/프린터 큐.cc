#include <iostream>
#include <queue>

using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int test;
	cin >> test;
	while (test--) {
		int n, m;
		cin >> n >> m;
		queue<pair<int, int>> q;
		priority_queue<int> pq; 

		for (int i = 0; i < n; i++) {
			int imp;
			cin >> imp;
			q.push({imp, i}); 
			pq.push(imp);
		}
		int ans = 1;
		while(1) {
			int imp = q.front().first;
			int val = q.front().second;
			if (imp != pq.top()) {
				q.pop();
				q.push({imp, val});
			}
			else {
				if (val == m) break;
				else {
					q.pop();
					pq.pop();
					ans++;
				}
			}
		}
		cout << ans << '\n';
	}
	return 0;
}