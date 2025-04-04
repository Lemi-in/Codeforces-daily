#include <iostream>
using namespace std;

bool isPowerOfTwo(long long n) {
    return n > 0 && (n & (n - 1)) == 0;
}

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        long long x;
        cin >> x;
        
        if (isPowerOfTwo(x)) {
            // If x is a power of 2, no solution exists
            cout << -1 << endl;
        } else if (x % 2 == 0) {
            // If x is even but not a power of 2, y = x-1 works
            cout << (x - 1) << endl;
        } else {
            // If x is odd, y = x-2 works
            cout << (x - 2) << endl;
        }
    }
    
    return 0;
}
