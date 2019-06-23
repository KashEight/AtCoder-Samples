#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const ll MOD = 1000000007;

int calc_ways(int start, int end) {
    int way_abs = end - start;
    if (way_abs == 0 || way_abs == 1) return 1;
    int dp[way_abs + 10];
    dp[0] = 1;
    
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> a;
    for (int i = 0; i < M; ++i) cin >> a[i];
    ll ways = calc_ways(0, a[0] - 1);

}