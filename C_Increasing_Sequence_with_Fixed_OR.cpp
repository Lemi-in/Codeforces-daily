#include <bits/stdc++.h>
#define int long long int

using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int testCases = 1;
    cin >> testCases;
    while (testCases--) {
        int number;
        cin >> number;
        int sequenceLength = 0;
        vector<int> sequence;
        vector<int> bitPositions;
        for (int i = 0; i < 61; i++) {
            if (number & (1LL << i)) {
                sequenceLength++;
                bitPositions.push_back((1LL << i));
            }
        }
        sequenceLength++;
        sequence.push_back(number);
        for (auto bitPosition : bitPositions) {
            if (number - bitPosition > 0) {
                sequence.push_back(number - bitPosition);
            }
        }

        reverse(sequence.begin(), sequence.end());
        cout << sequence.size() << endl;
        for (auto element : sequence) {
            cout << element << " ";
        }
        cout << endl;
    }
    return 0;
}