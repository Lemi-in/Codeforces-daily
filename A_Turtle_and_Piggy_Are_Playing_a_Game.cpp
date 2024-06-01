#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int MAX_N = 1e9 + 10;

vector<bool> is_prime(MAX_N, true);
vector<int> prime_factors[MAX_N];

void sieve() {
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= MAX_N; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAX_N; j += i) {
                is_prime[j] = false;
            }
        }
    }
    for (int i = 2; i <= MAX_N; i++) {
        if (is_prime[i]) {
            prime_factors[i].push_back(i);
        }
    }
}

int max_score(int l, int r) {
    int max_factors = 0;
    int max_num = 0;
    for (int i = l; i <= r; i++) {
        int factors = 0;
        for (int j = 0; j < prime_factors[i].size(); j++) {
            factors += (i / prime_factors[i][j]) - (i / (prime_factors[i][j] * prime_factors[i][j]));
        }
        if (factors > max_factors) {
            max_factors = factors;
            max_num = i;
        }
    }
    return max_factors;
}

int main() {
    sieve();
    int t;
    cin >> t;
    while (t--) {
        int l, r;
        cin >> l >> r;
        cout << max_score(l, r) << endl;
    }
    return 0;
}