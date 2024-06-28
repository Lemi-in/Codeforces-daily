#include <iostream>
#include <vector>
using namespace std;

// Function to calculate the maximum number of winnable rounds
int calculateMaxWins(int numCards, int lowerLimit, int upperLimit, const vector<int>& cardValues) {
    int maxWins = 0;      // Initialize the maximum number of wins
    int currentSum = 0;   // Initialize the current sum of card values
    int startIdx = 0;     // Initialize the start index for the current subarray

    // Loop through each card in the array
    for (int endIdx = 0; endIdx < numCards; ++endIdx) {
        currentSum += cardValues[endIdx];  // Add the value of the current card to the sum
        
        // Adjust the start index to keep the sum within the upper limit
        while (currentSum > upperLimit && startIdx <= endIdx) {
            currentSum -= cardValues[startIdx];
            startIdx++;
        }
        
        // Check if the current sum is within the specified limits
        if (currentSum >= lowerLimit && currentSum <= upperLimit) {
            maxWins++;          // Increment the count of winnable rounds
            currentSum = 0;     // Reset the current sum for the next round
            startIdx = endIdx + 1;  // Move the start index to the next card
        }
    }
    
    return maxWins;  // Return the total number of winnable rounds
}

// Function to handle multiple test cases and print the results
void processTestCases() {
    int testCases;   // Number of test cases
    cin >> testCases;
    
    while (testCases--) {
        int numCards, lowerLimit, upperLimit;
        cin >> numCards >> lowerLimit >> upperLimit;  // Read the input values for each test case
        
        vector<int> cardValues(numCards);
        for (int i = 0; i < numCards; ++i) {
            cin >> cardValues[i];  // Read the values of the cards
        }
        
        // Calculate the result using the calculateMaxWins function and print it
        int result = calculateMaxWins(numCards, lowerLimit, upperLimit, cardValues);
        cout << result << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);  // Optimize input/output operations
    cin.tie(nullptr);
    
    processTestCases();  // Call the function to process test cases
    
 return 0;
}

//shady will copy 
