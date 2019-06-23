#include <bits/stdc++.h>

using namespace std;

int main() {
    int r, d, x;
    vector<int> v;
    cin >> r >> d >> x;
    v.push_back(r * x - d);
    for (int i = 1; i < 10; ++i) v.push_back(r * v.at(i - 1) - d);
    for (int i = 0; i < v.size(); ++i) cout << v.at(i) << endl;
}