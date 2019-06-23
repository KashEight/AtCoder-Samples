#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, l, r;
    cin >> n >> m >> l >> r;
    for (int i = 0; i < m - 1; ++i) {
        int l_, r_;
        cin >> l_ >> r_;
        l = max(l, l_);
        r = min(r, r_);
    }
    if (r - l + 1 < 0) {
        cout << 0 << endl;
    } else {
        cout << r - l + 1 << endl;
    }
}