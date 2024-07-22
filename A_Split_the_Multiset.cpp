#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vl = vector<ll>;
#define int ll
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;
const ld EPS = 1e-9;

#define ff(i, s, e) for (int i = s; i < e; i++)
#define fr(i, s, e) for (int i = s; i >= e; i--)


void fastIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

void solve(){
    int n,k;
    cin>>n>>k;
        
    vector<int> arr;
    arr.push_back(n);
        
    int cnt=0;
    while(arr.size() < n)
    {
        int n=arr.back();
        arr.erase(arr.begin()+arr.size()-1);
        for(int i=0;i<min(k-1,n-1);i++)
        {
            arr.push_back(1);
        }
        arr.push_back(n-k+1);
        cnt++;
    }
        
    cout<<cnt<<endl;
}

signed main() {
    fastIO();

    int T = 1;
    cin >> T;
    while (T--) {
        solve();
    }
    
    return 0;
}