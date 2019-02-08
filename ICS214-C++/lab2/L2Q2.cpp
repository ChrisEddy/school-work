//   author: Chris Eddy
#include <iostream>
#include <string>
#include <iomanip> 
using namespace std;

int main(){

    string ISBN;
    int checkSum = 0;
    int numArray [9];

    cout << "Enter the first 9 digits of an ISBN as integer: ";
    cin >> ISBN;

    for(int i = 0; i <= ISBN.size(); i++){
        string y = ISBN.substr(i, 1);
        int value = atoi(y.c_str());
        checkSum = checkSum + (value * (i + 1));
    }

    checkSum = checkSum % 11;

    if(checkSum == 10){
        cout << setw( 8 ) << setfill( '0' ) << "The ISBN-10 number is: " << ISBN << "X" << "\n";
    }
    else{
        cout << setw( 8 ) << setfill( '0' ) << "The ISBN-10 number is: " << ISBN << checkSum << "\n";
    }

    return 0;
}