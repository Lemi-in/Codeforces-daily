#include <iostream>
#include <string>
using namespace std;

// Function to check if a given string is valid
void checkString() {
    string input;
    cin >> input;
    bool isValid = true;

    // Check if the first character is '1'
    if (input[0] != '1') {
        isValid = false; // If not, the string is not valid
    } else {
        // Iterate over the characters of the string starting from index 1
        for (int index = 1; index < input.size(); ++index) {
            if (index != input.size() - 1) {
                // For characters in the middle of the string (excluding the last character)
                // Check if the character is '0'
                if (input[index] == '0') {
                    isValid = false; // If '0' is found, the string is not valid
                    break;
                }
            } else {
                // For the last character of the string
                // Check if it is greater than '8'
                if (input[index] > '8') {
                    isValid = false; // If greater than '8', the string is not valid
                    break;
                }
            }
        }
    }

    // Output the result based on the validity of the string
    if (isValid) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    int testCases;
    cin >> testCases;
    while (testCases--) {
        checkString(); // Process each test case
    }
    return 0;
}
