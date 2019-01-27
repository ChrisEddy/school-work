//   author: Chris Eddy
#include <iostream>
#include <string>
using namespace std;

int main(){

    int ISBN;
    int checkSum = 0;
    int numArray [9];

    cout << "Enter the first 9 digits of an ISBN as integer: ";
    cin >> ISBN;

    string string_ISBN = to_string(ISBN);

    for (int i = 0; i < string_ISBN.size(); i++){
        numArray[i] = string_ISBN[i];
    }

    for(int x = 0; x < 9; x++){
        checkSum = checkSum + (numArray[x] * x);
    }

    checkSum = checkSum % 11;

    if(checkSum == 10){
        to_string(checkSum) = "X";
    }

    cout << "The ISBN-10 number is: " << ISBN << checkSum << "\n";

    return 0;
}