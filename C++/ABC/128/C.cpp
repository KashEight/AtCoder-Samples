#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> s(M);
    vector<int> p(M);
    for (int i = 0; i < M; ++i) {
        int k;
        cin >> k;
        s[i].resize(k);
        for (int j = 0; j < k; ++j) cin >> s[i][j];
    }
    for (int i = 0; i < M; ++i) cin >> p[i];

    int ans = 0;

    for (int bit = 0; bit < (1 << M); ++bit) {
        bool flag = true;
        for (int i = 0; i < M; ++i) {
            int c = 0;
            for (int id : s[i]) {
                if (bit & (1 << (id - 1))) ++c;
            }
            if (c % 2 != p[i]) flag = false;
        }
        if (flag) ++ans;
    }
    cout << ans << endl;
}