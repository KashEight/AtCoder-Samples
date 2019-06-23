#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    int total_min = 1000000;
    cin >> N;
    vector<int> W(N);
    for (int i = 0; i < N; ++i) cin >> W[i];
    for (int i = 1; i <= N; ++i) {
        for (int j = 0; j < N; ++j) {
            int under_sum, top_sum;
            under_sum = accumulate(W.begin(), W.begin() + j + 1, 0);
            top_sum = accumulate(W.begin() + j + 1, W.end(), 0);
            int total = abs(under_sum - top_sum);
            if (total_min > total) total_min = total;
        }
    }
    cout << total_min << endl;
}