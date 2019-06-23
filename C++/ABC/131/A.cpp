#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    bool flag = false;
    for (int i = 1; i < 4; ++i) {
        if (s[i - 1] == s[i]) flag = true;
    }
    if (!flag) cout << "Good" << endl;
    else cout << "Bad" << endl;
}