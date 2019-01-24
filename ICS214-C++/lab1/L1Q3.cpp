//   author: Chris Eddy
#include <iostream>
using namespace std;

int main(){
    const float KILO_CONVERT = 0.45359237;
    const float METER_CONVERT = 0.0254;
    float userWeight;
    float userHeight;
    float weightConverted;
    float heightConverted;
    float bmi;

    cout << "Enter weight in pounds: ";
    cin >> userWeight;

    weightConverted = userWeight * KILO_CONVERT;

    cout << "Enter height in inches: ";
    cin >> userHeight; 

    heightConverted = userHeight * METER_CONVERT;

    bmi = weightConverted / (heightConverted * heightConverted);

    cout << "BMI is: " << bmi << "\n";

    return 0;
}