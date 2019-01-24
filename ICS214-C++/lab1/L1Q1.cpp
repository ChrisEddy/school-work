//   author: Chris Eddy
#include <iostream>
using namespace std;

int main(){
    float input;
    float a;
    const float b = 9.0 / 5.0;
    const float c = 32.0;

    cout << "Enter a degree in Celcius ";
    cin >> input;

    float result = (input * b) + c;

    cout << input << " Celcuis is " << result << " Fahrenheit" << "\n";

    return 0;
}