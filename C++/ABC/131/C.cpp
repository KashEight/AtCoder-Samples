#include <bits/stdc++.h>

using namespace std;

using ll = long long;

ll gcd(ll a, ll b) {
    if (a % b == 0) return b;

    gcd(b, a % b);
}

int main() {
    ll A, B, C, D;
    cin >> A >> B >> C >> D;
    ll ab_abs = B - A  + 1;
    ll c_count = A % C == 0 ? abs(B / C) - abs(A / C) + 1 : abs(B / C) - abs(A / C);
    ll d_count = A % D == 0 ? abs(B / D) - abs(A / D) + 1 : abs(B / D) - abs(A / D);
    ll gcd_of_cd = gcd(C, D);
    ll cd = gcd_of_cd * (C / gcd_of_cd) * (D / gcd_of_cd);
    ll cd_count = A % cd == 0 ? abs(B / cd) - abs(A / cd) + 1 : abs(B / cd) - abs(A / cd);
    ab_abs -= c_count + d_count - cd_count;
    cout << ab_abs << endl;
}