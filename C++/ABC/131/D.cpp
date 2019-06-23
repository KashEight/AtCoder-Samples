#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> works(N);
    for (int i = 0; i < N; ++i) cin >> works[i].second >> works[i].first;
    sort(works.begin(), works.end());
    ll time = 0;
    bool flag = false;
    for (int i = 0; i < N; ++i) {
        time += works[i].second;
        if (time > works[i].first) {
            flag = true;
            break;
        }
    }
    if (flag) cout << "No" << endl;
    else cout << "Yes" << endl;
}