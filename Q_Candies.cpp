/*------------------------------------------------------
    - Author: GM. Amro Sous
    - Date:   2023-06-29 15:03:33
-------------------------------------------------------*/

#include <bits/stdc++.h>
using namespace std; 

#define ll long long 
#define nl "\n"
#define FAST std::ios_base::sync_with_stdio(false), std::cin.tie(NULL)

int main() {

    FAST;

    int n; 
    cin >> n; 
    vector<int> a(n + 1); 
    a[0] = 0; 
    int x; 
    for (int i = 1; i <= n; i++)
    {
        cin >> x; 
        a[i] = a[i - 1] + x; 
    }
    int q, l, r, sum; 
    cin >> q; 
    for (int i = 0; i < q; i++)
    {
        cin >> l >> r; 
        sum = a[r] - a[l - 1];
        cout << sum / 10 << nl;
    }

    return 0;
}