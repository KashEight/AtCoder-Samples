#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, p;
    string s;
    vector<tuple<string, int, int>> v;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> s >> p;
        v.push_back(make_tuple(s, -p ,i));
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); ++i) cout << get<2>(v.at(i)) + 1 << endl;
}