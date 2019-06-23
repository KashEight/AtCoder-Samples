#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const ll INF = 1LL << 60;

int main() {
    int N, L;
    cin >> N >> L;
    vector<int> v(N);
    for (int i = 0; i < N; ++i) v[i] = L + i;
    ll ans = INF;
    for (int i = 0; i < N; ++i) {
        if (abs(v[i]) < abs(ans)) ans = v[i];
    }
    cout << accumulate(v.begin(), v.end(), 0) - ans << endl;
}