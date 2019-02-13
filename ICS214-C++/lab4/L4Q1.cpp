//   author: Chris Eddy

using namespace std;
#include <string>
#include <iostream>

bool isValid(const string& cardNumber);
int sumOfDoubleEvenPlace(const string& cardNumber);
int getDigit(int number);
int sumOfOddPlace(const string& cardNumber);
bool startsWith(const string& cardNumber, const string & substr);
bool hasValidPrefix(const string& cardNumber);

int main(){
    string cardNumber;

    cout << "Enter a credit card number" << endl;
    cin >> cardNumber;

    if(isValid(cardNumber)){
        cout << "Credit card is valid" << endl;
    }
    else{
        cout << "Credit card is invalid" << endl;
    }

    return 0;
}

// Return true if the card number is valid
bool isValid(const string& cardNumber){
    if(hasValidPrefix(cardNumber)){
        int result = getDigit(stoi(cardNumber));
        cout << "result: " << result << endl;
    }
}

// Get the result from Step 2
int sumOfDoubleEvenPlace(const string& cardNumber){

}

// return this number if it is a single digit, otherwise,
// return the sum of the two digits.
int getDigit(int number){
    int digit;
    if(number > 9){
        int x;
        number = number % 10;
        x = number;
        cout << "getDigit: " << x << " " << number << endl;
        digit = x + number;
        return digit;
    }
    else{
        return number;
    }
}

// Return sum of odd-place digits in the card number
int sumOfOddPlace(const string& cardNumber){

}

// Return true if substr is the prefix for cardNumber
bool startsWith(const string& cardNumber, const string & substr){

}

// test if cardNumber starts with (4, 5, 37, 6)
bool hasValidPrefix(const string& cardNumber){
    if(cardNumber[0] == '4' || cardNumber[0] == '5' || cardNumber[0] == '6'){
        return true;
    }
    else if(cardNumber[0] == '3' && cardNumber[1] == '7'){
        return true;
    }
    else{
        return false;
    }
}