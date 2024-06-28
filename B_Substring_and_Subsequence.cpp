#include <iostream>
#include <string>
#include <math.h>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        string a, b;
        cin >> a >> b;
        int ans = a.length() + b.length();
        for (int st = 0; st < b.length(); st++) {
            int ptr = st;
            for (int i = 0; i < a.length(); i++) {
                if (ptr < b.length() && a[i] == b[ptr]) {
                    ptr++;
                }
            }
            if
             (ans < a.length() + b.length() - ptr + st) {
                ans = a.length() + b.length() - ptr + st;
            }
            else {
                ans = ans;
                };

        }
        cout << ans << endl;
    }
    return 0;
}