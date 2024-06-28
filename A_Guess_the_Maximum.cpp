#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        // Find the maximum value among all adjacent pairs
        int max_adjacent = -1;
        for (int i = 0; i < n - 1; ++i) {
            max_adjacent = max(max_adjacent, max(arr[i], arr[i + 1]));
        }

        // The maximum k at which Alice is guaranteed to win
        cout << max_adjacent - 1 << endl;
    }

    return 0;
}
