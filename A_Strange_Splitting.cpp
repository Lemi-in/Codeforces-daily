#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

void color(int t, vector<pair<int, vector<int>>> &tc) {
    for (int i = 0; i < t; ++i) {
        int n = tc[i].first;
        vector<int> a = tc[i].second;
        unordered_set<int> u(a.begin(), a.end());

        if (u.size() <= 1) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
            string c(n, 'R');
            c[1] = 'B';
            cout << c << endl;
        }
    }
}

int main() {
    int t;
    cin >> t;
    vector<pair<int, vector<int>>> tc(t);
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int j = 0; j < n; ++j) {
            cin >> a[j];
        }
        tc[i] = make_pair(n, a);
    }
    color(t, tc);
return 0;
}