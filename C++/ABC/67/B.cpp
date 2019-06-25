#include <bits/stdc++.h>

using namespace std;

int main() {
	int N, K;
  	cin >> N >> K;
  	vector<int> l(N);
  	for (int i = 0; i < N; ++i) cin >> l[i];
  	sort(l.begin(), l.end());
    cout << accumulate(l.end() - K, l.end(), 0) << endl;
}